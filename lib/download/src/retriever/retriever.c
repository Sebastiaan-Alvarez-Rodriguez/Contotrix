#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include <haut/haut.h>
#include <errno.h>

#include "callbacks/callbacks.h"
#include "structs/retrieve.h"
#include "structs/html.h"
#include "retriever.h"

static inline char separator() {
#ifdef _WIN32
    return '\\';
#else
    return '/';
#endif
}

// Takes a url as parameter, and returns the page html on success, NULL otherwise
static char* GetWebPage(const char* myurl) {
    html_t html;    
    html.content = malloc(1024*sizeof(char));
    html.used = 0;
    html.len = 1024;

    CURL *curl = curl_easy_init();

    curl_easy_setopt(curl, CURLOPT_URL, myurl);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callback_write);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &html);
    curl_easy_setopt(curl, CURLOPT_FAILONERROR, 1);
    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L); //We stop trying to connect after 10s (probably dead link)
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 0);
    CURLcode curl_res = curl_easy_perform(curl);

    char* ret = NULL;
    if (curl_res == 0 ) {
        ret = malloc(html.used * sizeof(char)+1);
        memcpy(ret, html.content, html.used);
        ret[html.used] = '\0';
    } else {
        ret = NULL;
    }
    curl_easy_cleanup(curl);

    free(html.content);
    return ret;
}

static void to_file(const char* const directory, const char* const name, const char* const data, size_t datalen) {
    size_t dirlen = strlen(directory);
    size_t namelen = strlen(name);
    char* buf = malloc(dirlen+1+namelen+6);
    if (buf == 0) {
        fprintf(stderr, "Could not allocate more memory on this machine.\n");
        return;
    }
    char* head = buf;
    memcpy(head, directory, dirlen);
    head += dirlen;
    *head = separator();
    ++head;

    memcpy(head, name, namelen);
    head += namelen;

    memcpy(head, ".html", 5);
    head += 5;
    *head = '\0';

    FILE* fp = fopen(buf, "w");
    if (fp == 0x0) {
        printf("Errno was set to be: %i\n", errno);
        printf("Location: %s\n", buf);
        return;
    }
    fwrite(data, datalen, 1, fp);
    fclose(fp);
    free(buf);
}

// Takes 2 urls as parameter, and a function. First url is the (sub)page of a domain you want to get links from
// Second url is the base domain name (e.g. domain.test, if you want to get domain.test/subdir/test.html links)
// The function argument must handle extraction of any requested data, and concatenation using '\n'
// Returns found links with newlines ('\n') between them
char* parse(const char* myhtmlpage, const char* myurl, const char* const directory, const char* const num) {
    char* const html = GetWebPage(myhtmlpage);
    if (html == NULL)
        return NULL;
    const size_t len = strlen(html);
    to_file(directory, num, html, len);

    retrieve_t ret;
    retrieve_create(&ret, myurl, "");

    haut_t parser;
    haut_init(&parser);
    parser.userdata = &ret;
    parser.events.attribute = callback_link;

    haut_setInput(&parser, html, len);
    haut_parse(&parser);

    haut_destroy(&parser);

    char* links = NULL;
    if (ret.linksused != 0) {
        size_t bufsize = 0;
        for (size_t x = 0; x < ret.linksused; ++x)
            bufsize += ret.links[x].len+1;

        links = malloc(bufsize+1 * sizeof(char));
        char* head = links;
        for (size_t x = 0; x < ret.linksused; ++x) {
            memcpy(head, ret.links[x].content, ret.links[x].len);
            head += ret.links[x].len;
            *head = '\n';
            ++head;
        }

        *head = '\0';
    }
    retrieve_destroy(&ret);
    free(html);
    return links;
}
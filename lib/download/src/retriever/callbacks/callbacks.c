#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#include <haut/haut.h>
#include <haut/tag.h>

#include "callbacks.h"
#include "../structs/retrieve.h"
#include "../structs/html.h"

static int callback_contains_get_variable(const char* const str, size_t len) {
    for (size_t x = 0; x < len; ++x)
        if (str[x] == '?')
            return x;
    return -1;
}

size_t callback_write(char* buffer, size_t size, size_t nmemb, html_t* html) {
    const size_t realsize = size * nmemb;

    while (realsize > (html->len - html->used)) {
        void* const newBuffer = realloc(html->content, html->len * 2);
        if (!newBuffer) {
            fprintf(stderr, "Could not allocate more memory on this machine.\n");
            return -1;
        }
        html->content = newBuffer;
        html->len *= 2;
    }

    char* const writeHead = html->content + html->used;
    memcpy(writeHead, buffer, realsize);
    html->used += realsize;

    return realsize;
}

void callback_link(haut_t* p, strfragment_t* key, strfragment_t* value) {
    retrieve_t* ret = (retrieve_t*) p->userdata;

    if(haut_currentElementTag(p) == TAG_A && strfragment_icmp(key, "href") && value && value->data && value->size > 0) {
        if (value->data[0] == '#') //Self referencing url tag. Should skip
            return;
        if (value->size > 3 && strncmp(value->data, "tel", 3) == 0)
            return;
        if (value->size > 6 && strncmp(value->data, "mailto", 6) == 0)
            return;
        size_t size = (size_t) value->size;
        bool link_is_relative_base = value->data[0] == '/';
        bool link_is_relative_current = value->size > 4 && strncmp(value->data, "http", 4) != 0 && strncmp(value->data, "www.", 4) != 0;

        int tmp = callback_contains_get_variable(value->data, size);
        if (tmp != -1)
            size -= (size - tmp);
        else if (value->data[size-1] == '/')
            size -= 1;

        retrieve_add_url(ret, value->data, size, link_is_relative_base, link_is_relative_current);
    }
}

void callback_inner_text(haut_t* p, strfragment_t* text) {
    if (haut_currentElementTag(p) == TAG_TITLE)    
        retrieve_change_title((retrieve_t*) p->userdata, text->data, text->size);
}
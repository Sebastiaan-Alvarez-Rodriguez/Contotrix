#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#include "str.h"

#include "retrieve.h"

void retrieve_create(retrieve_t* ret, const char* const base_url, char* title) {
    str_create(&ret->base_url, base_url);
    str_create(&ret->title, title);
    ret->links = malloc(16*sizeof(str_t));
    ret->linksused = 0;
    ret->linkslen = 16;
}

void retrieve_add_url(retrieve_t* ret, const char* url, size_t len, bool is_relative) {
    if (ret->linksused == ret->linkslen) {
        str_t* const tmp = realloc(ret->links, ret->linkslen*2*sizeof(str_t));
        if (!tmp) {
            fprintf(stderr, "Could not allocate more memory on this machine.\n");
            return;
        }
        ret->links = tmp;
        ret->linkslen *= 2;
    }
    if (is_relative) {
        str_create_from(&ret->links[ret->linksused], &ret->base_url);
        str_append(&ret->links[ret->linksused], url, len);
    } else {
        str_create_n(&ret->links[ret->linksused], url, len);
    }
    ++ret->linksused;
}

void retrieve_change_title(retrieve_t* ret, const char* const title, size_t len) {
    str_change(&ret->title, title, len);
}

void retrieve_destroy(retrieve_t* ret) {
    str_destroy(&ret->base_url);
    str_destroy(&ret->title);
    for (size_t x = 0; x < ret->linksused; ++x)
        str_destroy(&ret->links[x]);
    free(ret->links);
}
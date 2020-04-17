#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#include "str.h"

void str_create(str_t* str, const char* const content) {
    str->len = strlen(content);
    str->content = malloc(str->len);
    memcpy(str->content, content, str->len);
}

void str_create_n(str_t* str, const char* const content, size_t len) {
    str->len = len;
    str->content = malloc(len);
    memcpy(str->content, content, len);
}

void str_create_from(str_t* str, const str_t* const other) {
    str->len = other->len;
    str->content = malloc(str->len);
    memcpy(str->content, other->content, str->len);
}

void str_append(str_t* str, const char* const content, size_t len) {
    char* tmp = realloc(str->content, str->len+len);
    if (!tmp) {
        fprintf(stderr, "Could not allocate more memory on this machine.\n");
        return;
    }
    str->content = tmp;
    memcpy(&str->content[str->len], content, len);
    str->len += len;
}

void str_change(str_t* str, const char* const content, size_t len) {
    char* tmp = realloc(str->content, len);
    if (!tmp) {
        fprintf(stderr, "Could not allocate more memory on this machine.\n");
        return;
    }
    str->content = tmp;
    str->len = len;
    memcpy(str->content,content, len);
}

void str_destroy(str_t* str) {
    free(str->content);
}
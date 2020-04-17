#ifndef STR_H
#define STR_H

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

// Structure to contain strings
typedef struct {
    char* content;
    size_t len;
} str_t;

void str_create(str_t* str, const char* const content);
void str_create_n(str_t* str, const char* const content, size_t len);
void str_create_from(str_t* str, const str_t* const other);

void str_append(str_t* str, const char* const content, size_t len);
void str_change(str_t* str, const char* const content, size_t len);

void str_destroy(str_t* str);

#endif
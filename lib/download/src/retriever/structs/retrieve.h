#ifndef RETRIEVE_H
#define RETRIEVE_H

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#include "str.h"

// Structure to communicate between caller and callback for collecting all info
typedef struct {
    str_t base_url, title;
    str_t* links;
    size_t linksused, linkslen;
} retrieve_t;

void retrieve_create(retrieve_t* ret, const char* const base_url, char* title);

void retrieve_add_url(retrieve_t* ret, const char* url, size_t len, bool is_relative);
void retrieve_change_title(retrieve_t* ret, const char* const title, size_t len);

void retrieve_destroy(retrieve_t* ret);

#endif
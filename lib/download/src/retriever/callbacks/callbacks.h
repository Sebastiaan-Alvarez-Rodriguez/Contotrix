#ifndef CALLBACKS_H
#define CALLBACKS_H

#include <stdlib.h>
#include <haut/haut.h>
#include "../structs/html.h"

// Callback to collect html and store it in a html_t structure
size_t callback_write(char* buffer, size_t size, size_t nmemb, html_t* html);

// Callback to collect links and store them in a link_t structure
void callback_link(haut_t* p, strfragment_t* key, strfragment_t* value);

// Callback to collect title of html page
void callback_inner_text(haut_t* p, strfragment_t* text);
#endif
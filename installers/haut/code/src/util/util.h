#ifndef UTIL_H
#define UTIL_H

#include <stdbool.h>

// Returns true if given string ends on given suffix, otherwise false
bool util_ends_with(const char* str, const char* suffix);
#endif
#include <string.h>
#include "util.h"


bool util_ends_with(const char* str, const char* suffix) {
    if (!str || !suffix)
        return false;
    size_t lenstr = strlen(str);
    size_t lensuffix = strlen(suffix);
    if (lensuffix > lenstr)
        return false;
    return strncmp(str + lenstr - lensuffix, suffix, lensuffix) == 0;
}
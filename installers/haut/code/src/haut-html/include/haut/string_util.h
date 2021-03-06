/*
 * Haut - a lightweight html tokenizer
 *
 * Micky Faas <micky@edukitty.org>
 * (C) 2017, Leiden University
 */

#ifndef STRING_UTIL_H
#define STRING_UTIL_H

/** 
 * This header defines some usefull basic function to deal with C-strings.
 * These functions are very simple and are used by Haut internally,
 * whenever possible, public API functions just use const char* for strings.
 */

#include <sys/types.h>
#include <stdbool.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * An non-mutable structure to safely store base pointer plus total length 
 */
typedef struct {
    const char* data;
    size_t size;
} strfragment_t;

void strfragment_set( strfragment_t* str, const char* buf, size_t len );
void strfragment_zero( strfragment_t* str);

bool strfragment_cmp( strfragment_t* str1, const char* str2 );
bool strfragment_ncmp( strfragment_t* str1, const char* str2, size_t len );
bool strfragment_icmp( strfragment_t* str1, const char* str2 );
bool strfragment_nicmp( strfragment_t* str1, const char* str2, size_t len );

/**
 * A mutable string type that supports growing
 */
typedef struct {
    char *data;
    size_t size;
    size_t capacity;
} strbuffer_t;

#include <uchar.h>


void strbuffer_init( strbuffer_t* d );

void strbuffer_free( strbuffer_t* d );

void strbuffer_clear( strbuffer_t* d );

size_t strbuffer_grow( strbuffer_t* d, size_t add );

size_t strbuffer_reserve( strbuffer_t* d, size_t total );

void strbuffer_copy( strbuffer_t* d, const strbuffer_t* src );

void strbuffer_ncopy( strbuffer_t* d, size_t dest_offset, const strbuffer_t* src, size_t src_offset, size_t length );

void strbuffer_copyFragment( strbuffer_t* d, size_t offset, strfragment_t* str );

void strbuffer_append( strbuffer_t* d, const char* str, size_t len );

void strbuffer_swap( strbuffer_t* str1, strbuffer_t* str2 );

strfragment_t strbuffer_toFragment( strbuffer_t* str );

/** 
 * Convert the Unicode codepoint @c to an UTF-8 string.
 * Expects a pointer to an uninitialized strbuffer structure in @d,
 * which is in turn allocated to the exact amount number bytes that the
 * codepoint @c expands to (1, 2, 3 or 4)
 * Returns true on success
 */
bool u32toUTF8( strbuffer_t* d, char32_t c );

bool u32toUTF8_at( strbuffer_t* d, int offset, char32_t c );

#ifdef __cplusplus
}
#endif

#endif


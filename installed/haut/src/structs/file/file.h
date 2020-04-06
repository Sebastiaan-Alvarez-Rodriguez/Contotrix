#ifndef FILE_H
#define FILE_H

#include <stdlib.h>

// Structure to store file contents in memory
typedef struct {
    char* content;
    size_t len;
    char* name;
} file_t;

// Create an empty file struct
file_t file_create();

// Insert file contents from a given file at path (e.g. 'test/path/') and filename (e.g. 'test.html')
// file is modified to contain file content
bool file_read_from_file(file_t* const file, const char* const path, const char* const filename);

// Free file structure
void file_free(file_t* const file);

#endif
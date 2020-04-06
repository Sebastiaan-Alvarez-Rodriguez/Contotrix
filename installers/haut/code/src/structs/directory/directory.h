#ifndef DIRECTORY_H
#define DIRECTORY_H

#include <stdlib.h>
#include <stdbool.h>
#include "structs/file/file.h"

#define DIRECTORY_CREATE_SIZE 2

// Structure to easily pass all file contents in a directory
typedef struct {
    file_t* files;
    size_t len, used;
} directory_t;

// Create empty directory structure
directory_t directory_create();

// Adds a file to the list of files
bool directory_add(directory_t* const dir, const file_t new_file);

// Reads all files ending on '.html' in a given directory
// Stores results in file structs in the directory struct
bool directory_read_html(directory_t* const dir, const char* const path);

// Frees a directory structure
void directory_free(directory_t* const dir);
#endif
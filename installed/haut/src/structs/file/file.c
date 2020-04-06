#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include "file.h"


file_t file_create() {
    file_t file;
    file.content = NULL;
    file.len = 0;
    file.name = NULL;
    return file;
}

bool file_read_from_file(file_t* const file, const char* const path, const char* const filename) {
    const size_t pathlen = strlen(path);
    char* fullpath = malloc(pathlen + 1 + strlen(filename) + 1);
    strcpy(fullpath, path);
    strcat(fullpath, "/");
    strcat(fullpath, filename);

    FILE* f = fopen(fullpath, "r");
    free(fullpath);
    if (f == NULL) // File open problems
        return false;

    if (fseek(f, 0L, SEEK_END) == 0) {
        long bufsize = ftell(f); // Get size of file
        char* tmp = file->content == NULL ? malloc(sizeof(char) * (bufsize + 1)) : realloc(file->content, sizeof(char) * (bufsize + 1));
        if (tmp == NULL)
            return false;

        file->content = tmp;
        file->len = bufsize+1;

        fseek(f, 0L, SEEK_SET);
        size_t used = fread(file->content, sizeof(char), bufsize, f);
        if (ferror(f) != 0) {
            fputs("Error reading file", stderr);
            return false;
        } else {
            file->content[used++] = '\0';
        }
    }
    fclose(f);
    char* const tmp = malloc(sizeof(char) * (strlen(filename)+1));
    if (tmp == NULL)
        return false;
    strcpy(tmp, filename);
    file->name = tmp;
    return true;
}

void file_free(file_t* const file) {
    free(file->content);
    free(file->name);
}
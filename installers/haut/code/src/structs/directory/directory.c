#define _GNU_SOURCE
#include <dirent.h>
#include <string.h>
#include <stdio.h>
#include "util/util.h"
#include "directory.h"

directory_t directory_create() {
    directory_t directory;
    directory.files = malloc(DIRECTORY_CREATE_SIZE * sizeof(file_t));
    directory.len = DIRECTORY_CREATE_SIZE;
    directory.used = 0;
    return directory;
}

bool directory_add(directory_t* const dir, file_t new_file) {
    const size_t len_old = dir->len;
    size_t used = dir->used;

    if (len_old == used) { // No more room available. Realloc to larger size
        file_t* tmp = realloc(dir->files, len_old*2 * sizeof(file_t));
        if (tmp == NULL) // Realloc failed, no more memory
            return false;
        dir->files = tmp;
        dir->len *= 2;
    }
    dir->files[used] = new_file;
    dir->used += 1;
    return true;
}

bool directory_read_html(directory_t* const dir, const char* const path) {
    DIR* const dp = opendir(path);

    if (dp != NULL) {
        struct dirent* ep;
        while ((ep = readdir(dp))) {
            const char* const filename = ep->d_name;
            if (ep->d_type != DT_DIR && util_ends_with(filename, ".html")) {
                file_t file = file_create();
                if (!file_read_from_file(&file, path, filename))
                    return false;
                if (!directory_add(dir, file))
                    return false;
            }
        }
        closedir(dp);
    } else {
        perror("Couldn't open the directory");
        return false;
    }
    return true;
}

void directory_free(directory_t* const dir) {
    for (size_t i = 0; i < dir->used; ++i)
        file_free(&dir->files[i]);
    free(dir->files);
}
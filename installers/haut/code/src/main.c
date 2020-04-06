#include <stdio.h>
#include <stdlib.h>
#include <haut/haut.h>
#include <time.h>

#include "util/util.h"
#include "structs/file/file.h"
#include "structs/directory/directory.h"

// Code to run speed tests
static void speed_test(directory_t d, size_t repeat) {
    haut_t parser;
    double total = 0;

    for (size_t i = 0; i < d.used; ++i) {
        file_t file = d.files[i];
        printf("Handling file %s", file.name);
        const clock_t start = clock();

        for (size_t rep = 0; rep < repeat; ++rep) {
            haut_init(&parser);
            haut_setInput(&parser, file.content, file.len);
            haut_parse(&parser);
            haut_destroy(&parser);
        }

        const clock_t end = clock();
        const double delta = (double)(end - start) / CLOCKS_PER_SEC;
        total += delta;
        printf(": %f seconds\n", delta);
    }
    printf("\nTotal time: %f seconds\n", total);
}

// Simple function to display information in case someone did not provide the right amount of parameters
static void usage(const char* name) {
    printf("Usage: %s <path> <repeat>\n<path> should specify a directory containing html files to test with\n<repeat> should specify repeat parse amount to test with\n", name);
    exit(-1);
}

int main(int argc, char* argv[]) {
    if (argc != 3)
        usage(argv[0]);
    
    directory_t d = directory_create();
    if (!directory_read_html(&d, argv[1])) {
        printf("Could not load in all html files... Is one testfile unreadable (insufficient permissions)?\n");
    } else {
        printf("Found %lu files\n", d.used);
        speed_test(d, strtoul(argv[2], NULL, 0));
        directory_free(&d);
    }
    return 0;
}
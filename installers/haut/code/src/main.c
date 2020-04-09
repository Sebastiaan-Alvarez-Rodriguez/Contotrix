#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <haut/haut.h>


// Code to run speed tests
static void speed_test(size_t repeat) {
    haut_t parser;
    //TODO: read stdin using either getline
    // http://man7.org/linux/man-pages/man3/getline.3.html
    // or fgets
    // https://stackoverflow.com/questions/7709452/
    for (size_t rep = 0; rep < repeat; ++rep) {
        haut_init(&parser);
        haut_setInput(&parser, file.content, file.len);
        haut_parse(&parser);
        haut_destroy(&parser);
    }
}

// Simple function to display information in case someone did not provide the right amount of parameters
static void usage(const char* name) {
    printf("Usage: %s <repeat>\n\t<repeat> should specify repeat parse amount to test with\n\tNote that stdin should provide html content\n", name);
    exit(-1);
}

int main(int argc, char* argv[]) {
    if (argc != 2)
        usage(argv[0]);
    speed_test(strtoul(argv[1], NULL, 0));
    return 0;
}
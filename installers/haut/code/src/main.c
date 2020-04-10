#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <haut/haut.h>
#include <haut/tag.h>

void callback_link(haut_t* p, strfragment_t* key, strfragment_t* value) {
    if(haut_currentElementTag(p) == TAG_A && strfragment_icmp(key, "href") && value && value->data && value->size > 0)
        ++*((size_t*) p->userdata);
}


// Code to run speed tests
static void speed_test(size_t repeat) {
    unsigned length;
    scanf("%u", &length);
    char* content = malloc(length * sizeof(char));
    // if (fgets(content, length+1, stdin) == NULL)
    //     return false;
    read(STDIN_FILENO, content, length);
    // char* head = content;
    // size_t len = 1024;
    // size_t used = 0;
    // char current;
    // while ((current = fgetc(head, len-used, stdin)) != EOF) {
    //     if (used == len) {
    //         char* tmp = realloc(content, len*2);
    //         if (tmp == NULL) {
    //             free(content);
    //             return false;
    //         }
    //         content = tmp;
    //         len *= 2;
    //     }
    //     content[used] = current;
    //     ++used;
    // }

    haut_t parser;

    for (size_t rep = 0; rep < repeat-1; ++rep) {
        haut_init(&parser);
        haut_setInput(&parser, content, length);
        haut_parse(&parser);
        haut_destroy(&parser);
    }

    size_t amount_links = 0;
    haut_init(&parser);
    parser.userdata = &amount_links;
    parser.events.attribute = callback_link;

    haut_setInput(&parser, content, length);
    haut_parse(&parser);
    haut_destroy(&parser);
    free(content);
    printf("%lu", amount_links);
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
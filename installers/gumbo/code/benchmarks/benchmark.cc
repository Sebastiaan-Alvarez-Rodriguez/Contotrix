#include <iostream>
#include <stdint.h>
#include <stdlib.h>
#include <string>

#include "gumbo.h"

static void search_for_links(GumboNode* node, size_t* amount_links) {
    if (node->type != GUMBO_NODE_ELEMENT)
        return;
    GumboAttribute* href = 0x0;
    if (node->v.element.tag == GUMBO_TAG_A && (href = gumbo_get_attribute(&node->v.element.attributes, "href")))
        ++(*amount_links);

    GumboVector* children = &node->v.element.children;
    for (unsigned i = 0; i < children->length; ++i)
        search_for_links(static_cast<GumboNode*>(children->data[i]), amount_links);
}


int main(int argc, char** argv) {
    if (argc != 2) {
        std::cout << "Usage: "<<argv[0]<<"<repeats>\n";
        exit(EXIT_FAILURE);
    }

    size_t repeat;
    try {
        repeat = std::stoull(argv[1]);
    } catch(...) {
        std::cout << "Could not convert '"<<argv[1]<<"' to number\n";
        exit(EXIT_FAILURE);
    }

    unsigned length;
    std::cin.read((char*) &length, 4);
    char* content = new char[length];
    std::cin.read(content, length);

    for (size_t i = 0; i < repeat-1; ++i) {
        GumboOutput* output = gumbo_parse(content);
        gumbo_destroy_output(&kGumboDefaultOptions, output);
    }

    size_t amount_links = 0;
    GumboOutput* output = gumbo_parse(content);
    search_for_links(output->root, &amount_links);
    gumbo_destroy_output(&kGumboDefaultOptions, output);
    free(content);

    std::cout << amount_links;
}
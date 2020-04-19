#include <iostream>
#include <sstream>
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

size_t strtoull_precpp11(const char* const arg) {
    std::stringstream sstream(arg);
    size_t ans = 0;
    sstream >> ans;
    return ans;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cout << "Usage: "<<argv[0]<<" <htmlsize> <repeats>\n";
        exit(EXIT_FAILURE);
    }

    size_t htmlsize, repeat;
    try {
        htmlsize = strtoull_precpp11(argv[1]);
        repeat = strtoull_precpp11(argv[2]);
    } catch(...) {
        std::cout << "Could not convert '"<<argv[1]<<"' or '"<<argv[2]<<"' to number\n";
        exit(EXIT_FAILURE);
    }

    char* content = new char[htmlsize];
    std::cin.read(content, htmlsize);
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
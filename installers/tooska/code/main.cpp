#include <fstream>
#include <iostream>
#include <stdint.h>
#include <stdlib.h>
#include <string>

#include <html/html_document.h>
#include <html/html_node.h>


int main(int argc, char** argv) {
    if (argc != 3) {
        std::cout << "Usage: "<<argv[0]<<" <htmlsize> <repeats>\n";
        exit(EXIT_FAILURE);
    }

    size_t htmlsize, repeat;
    try {
        htmlsize = std::stoull(argv[1]);
        repeat = std::stoull(argv[2]);
    } catch(...) {
        std::cout << "Could not convert '"<<argv[1]<<"' or '"<<argv[2]<<"' to number\n";
        exit(EXIT_FAILURE);
    }

    char* content = new char[htmlsize];
    std::cin.read(content, htmlsize);
    for (size_t i = 0; i < repeat-1; ++i) {
        tooska::html::html_document document;
        document.set_text(content);
    }
    tooska::html::html_document document;
    document.set_text(content);
    auto links = document.get_by_tag_name("a");
    size_t found = 0;
    for (const auto& x : links)
        if (x->has_attr("href"))
            ++found;

    std::cout << found;
    return 0;
}
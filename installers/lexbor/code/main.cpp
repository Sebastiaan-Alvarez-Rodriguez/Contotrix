#include <iostream>
#include <stdint.h>
#include <stdlib.h>
#include <string>
#include <stdio.h>

#include <lexbor/html/html.h>
#include <lexbor/dom/dom.h>


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
        lxb_html_parser_t* parser = lxb_html_parser_create();
        lxb_status_t status = lxb_html_parser_init(parser);
        // if (status != LXB_STATUS_OK)
        //     return 1;
        
        lxb_html_document_t* document = lxb_html_parse(parser, (const lxb_char_t*) content, htmlsize);
        // if (document == NULL)
        //     return 1;
        lxb_html_parser_destroy(parser);
        lxb_html_document_destroy(document);
    }


    lxb_html_parser_t* parser = lxb_html_parser_create();
    lxb_status_t status = lxb_html_parser_init(parser);
    // if (status != LXB_STATUS_OK)
    //     return 1;
    lxb_html_document_t* document = lxb_html_parse(parser, (const lxb_char_t*) content, htmlsize);
    // if (document == NULL)
    //     return 2;
    lxb_html_parser_destroy(parser);
    lxb_dom_collection_t* collection = lxb_dom_collection_make(&document->dom_document, 64);
    // if (collection == NULL)
    //     return 3;
    status = lxb_dom_elements_by_tag_name(lxb_dom_interface_element(document->body), collection, (const lxb_char_t*) "a", 1);
    // if (status != LXB_STATUS_OK)
    //     return 4;

    size_t amount_links = 0;
    for (size_t x = 0; x < lxb_dom_collection_length(collection); ++x) {
        lxb_dom_element_t* element = lxb_dom_collection_element(collection, x);
        if (lxb_dom_element_has_attribute(element, (const lxb_char_t*) "href", 4))
            ++amount_links;
    }
    std::cout << amount_links;
    lxb_dom_collection_destroy(collection, true);
    lxb_html_document_destroy(document);

    free(content);
}
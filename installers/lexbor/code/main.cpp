#include <dirent.h>
#include <fstream>
#include <iostream>
#include <stdint.h>
#include <stdlib.h>
#include <string>

#include <lexbor/html/html.h>

std::string getContents(const std::string& path) {
    std::ifstream in(path, std::ios::in | std::ios::binary);
    if (!in) {
        std::cout << "File " << path << " couldn't be read!\n";
        exit(EXIT_FAILURE);
    }

    std::string contents;
    in.seekg(0, std::ios::end);
    contents.resize(in.tellg());
    in.seekg(0, std::ios::beg);
    in.read(&contents[0], contents.size());
    in.close();
    return contents;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cout << "Usage: "<<argv[0]<<" <data> <repeats>\n";
        exit(EXIT_FAILURE);
    }

    DIR* dir;
    struct dirent* file;

    if ((dir = opendir(argv[1])) == NULL) {
        std::cout << "Couldn't open directory '"<<argv[1]<<"'.\n";
        exit(EXIT_FAILURE);
    }

    size_t repeat;
    try {
        repeat = std::stoull(argv[2]);
    } catch(...) {
        std::cout << "Could not convert '"<<argv[2]<<"' to number\n";
        exit(EXIT_FAILURE);
    }

    while ((file = readdir(dir)) != NULL) {
        std::string filename(file->d_name);
        if (filename.length() > 5 && filename.compare(filename.length() - 5, 5, ".html") == 0) {
            std::string path = argv[1];
            path.append("/");
            path.append(filename);

            const std::string contents = getContents(path);

            for (size_t i = 0; i < repeat; ++i) {
                lxb_status_t status;
                lxb_html_document_t *document;

                /* Initialization */
                document = lxb_html_document_create();
                if (document == NULL) {
                    std::cout << "Failed to create HTML Document for file " << filename << "\n";
                    continue;
                }

                /* Parse HTML */
                status = lxb_html_document_parse(document, (lxb_char_t*)contents.c_str(), contents.size());
                if (status != LXB_STATUS_OK) {
                    std::cout << "Failed to parse HTML for file " << filename << "\n";
                    continue;
                }

                // /* Print Incoming Data */
                // PRINT("HTML:");
                // PRINT("%s", (const char *) html);

                // /* Print Result */
                // PRINT("\nHTML Tree:");
                // serialize(lxb_dom_interface_node(document));

                /* Destroy document */
                lxb_html_document_destroy(document);
            }
       }
    }
    closedir(dir);
    return 0;
}
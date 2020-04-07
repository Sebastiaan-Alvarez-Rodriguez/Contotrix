#include <dirent.h>
#include <fstream>
#include <iostream>
#include <stdint.h>
#include <stdlib.h>
#include <string>

#include <html/html_document.h>

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
                tooska::html::html_document document;
                document.set_text(contents);
            }
       }
    }
    closedir(dir);
    return 0;
}
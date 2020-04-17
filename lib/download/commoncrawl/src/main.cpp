#include <iostream>
#include <fstream>

#include "sha/sha.h"

void usage(const char* const progName) {
    std::cout<< "Usage: " << progName << " <inputfile> <outputpath>\n"
    << "<inputfile>   Path to .warc file to take HTML content from\n"
    << "<outputpath>  Path to directory to store HTML content\n";
    exit(-1);
}

inline bool startswith(const std::string& src, const std::string& prefix) {
    if (src.size() < prefix.size())
        return false;
    for (size_t x = 0; x < prefix.size(); ++x)
        if (src.at(x) != prefix.at(x))
            return false;
    return true;
}

inline bool startswith_ignorespace(const std::string& src, const std::string& prefix) {
    size_t start;
    for(start = 0; start < src.size() && src.at(start) == ' '; ++start);
    if (start == src.size())
        return false;
    return startswith(src.substr(start), prefix);
}

// Generates html files from warc file, returns amount of pages generated
size_t generate(const std::string& inputfile, const std::string& outputpath) {
    std::ifstream file(inputfile, std::ios::in);
    if (!file.is_open())
        exit(1);

    size_t generated = 0;
    std::string line;
    std::ofstream page_info(outputpath+"page_info.csv");
    while(!file.eof()) {
        while(std::getline(file, line) && line != "WARC-Type: response\r");
        while(std::getline(file, line) && !startswith(line, "WARC-Target-URI: "));
        if (line.size() <= 18) //only header name and 1 carriage return
            continue;
        const std::string curr_url = line.substr(17, line.size()-17-1);
        const std::string shastring = sha::sha256(curr_url);

        while(std::getline(file, line) && !startswith_ignorespace(line, "<!DOCTYPE"));
        if (!line.find("<html")) {
            while(std::getline(file, line) && line == "\r");
            if (std::getline(file, line) && !startswith_ignorespace(line, "<html"))
                continue;
        }

        std::ofstream outfile(outputpath+shastring+".html", std::ios::out);
        while(std::getline(file, line) && !startswith(line, "WARC/1.0")) {
            outfile << line << '\n';
        }
        outfile.close();
        ++generated;
        page_info << shastring << ',' << curr_url << '\n';
    }
    file.close();
    return generated;
}

int main(int argc, char const *argv[]) {
    if (argc != 3)
        usage(argv[0]);
    std::cout << generate(argv[1], argv[2]);
    return 0;
}
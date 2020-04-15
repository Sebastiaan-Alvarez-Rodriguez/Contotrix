#include <haut/haut.h>
#include <deque>
#include <set>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>

#include "sha/sha.h"
#include "tree/tree.h"
#include "retriever/retriever.h"

static inline char separator() {
#ifdef _WIN32
    return '\\';
#else
    return '/';
#endif
}

//Takes a list of urls, separated by '\n', and returns a set containing these urls in form std::string
static std::set<std::string> segment(const char* const sentence) {
    std::set<std::string> ret;

    std::stringstream ss(sentence);
    std::string to;
    
    while(std::getline(ss,to,'\n'))
        ret.insert(to);
    return ret;
}

static std::string baseurl(const std::string url) {
    std::string base;
    std::string prefix = "";
    if (url.compare(0, 7, "http://") == 0) {
        prefix = "http://";
        base = url.substr(7);
    } else if (url.compare(0, 8, "https://") == 0) {
        prefix = "https://";
        base = url.substr(8);
    } else {
        base = url;
    }
    
    size_t pos = base.find('/');
    if (pos == std::string::npos)
        return prefix.append(base);
    else
        return prefix.append(base.substr(0, pos));
    
}

// Fetch an unvisited url, in a Breadth First Search pattern. 
// Returns true on success, false if the queue gets empty before finding an unvisited url.
static bool fetch(std::string& visit_url, Tree& visited, std::deque<std::string>& to_visit) {
    do {
        if (to_visit.empty())
            return false;
        visit_url = to_visit.front();
        to_visit.pop_front();
        ;
    } while (!visited.insert(visit_url)); 
    // Note: insert(), right above this line, only returns true if the url did not yet exist.
    // So, this loops continues until an unvisited url is found (which is then inserted in visited)
    // or until there are no more urls to try
    return true;
}


//With set difference -> Up to O(n)
// If I check difference between visited and to_visit every iteration
// But I do too much work then... The to_visit set is always legitimate, but it is too when I just merge...
static void crawl(const std::string& start_url, const std::string& directory, unsigned long long stop_after) {
    Tree visited;

    std::deque<std::string> to_visit;
    to_visit.push_front(start_url);

    std::string tmp = directory + separator() + "sha256_to_name.txt";
    std::ofstream file(tmp, std::ios::out | std::ios::app);

    unsigned long long x;
    for (x = 0; x < stop_after; ++x) {
        std::string visit_url;
        if (!fetch(visit_url, visited, to_visit))
            break;

        // std::cout << "Visiting url "<< x <<": " << visit_url << '\n';
        
        std::string name = sha::sha256(visit_url);
        file << visit_url << ' ' << name << '\n';
        char* urllinks = parse(visit_url.c_str(), baseurl(visit_url).c_str(), directory.c_str(), name.c_str());
        if (urllinks != NULL) {
            auto linkset = segment(urllinks);
            free(urllinks);
            // std::cout << "Found "<<linkset.size()<<" links"<<std::endl;
            for (const auto& url : linkset)
                to_visit.push_back(url); //No need to check if url was visited already. fetch() function does that already
        }
    }
    file.close();
    std::cout << x;
}


// Simple function to display information in case someone did not provide the right amount of parameters
static void usage(const char* name) {
    std::cout << name << " <web-entrypoint> <data-dir> <stop-after>" << std::endl;
    std::cout<< R"HERE(
    <web-entrypoint> should specify a websitewhere we will start crawling
    <data-dir> specifies a directory to store websites in
    <stop-after> specifies after how many websites we stop crawling
)HERE";
    exit(-1);
}

int main(int argc, char* argv[]) {
    if (argc != 4)
        usage(argv[0]);
    else
        crawl(argv[1], argv[2], std::strtoull(argv[3], NULL, 0));
    return 0;
}
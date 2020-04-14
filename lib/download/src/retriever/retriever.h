#ifndef RETRIEVER_H
#define RETRIEVER_H

#ifdef __cplusplus
extern "C" {
#endif

char* parse(const char* myhtmlpage, const char* myurl, const char* const directory, const char* const num);
#ifdef __cplusplus
}
#endif
#endif
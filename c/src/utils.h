#ifndef UTILS_H
#define UTILS_H
#include <string.h>

static inline void utils_swap(void* a, void* b, size_t size) {
    char temp[size];
    memcpy(temp, a, size);
    memcpy(a, b, size);
    memcpy(b, temp, size);
}
 
#endif

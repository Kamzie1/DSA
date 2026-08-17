#ifndef VECTOR_H
#define VECTOR_H

#include <stddef.h>

/*
 * This is an int vector data structure.
 * You can define VECTOR_CAPACITY_STRATEGY to customize its dynamic growth.
 * I couldn't decide if I should expose the struct, so I made it customizable.
*/

#ifdef DSA_EXPOSED

    typedef struct {
        int* data;
        size_t size;
        size_t capacity;
    } intVector_t;

    void vector_init(intVector_t* vec, size_t capacity);

#else 

    typedef struct vector_impl intVector_t;

#endif

// Status Codes
#define BAD_ALLOC -1
#define SUCCESS 0
#define OUT_OF_RANGE 1

// Allocations
intVector_t* vector_create(size_t capacity);
void vector_free(intVector_t* vec);
intVector_t* vector_copy(intVector_t* vec);

// Capacity
int vector_empty(intVector_t* vec);
size_t vector_size(intVector_t* vec);
size_t vector_capacity(intVector_t* vec);
size_t vector_max_size(void);
int vector_reserve(intVector_t* vec, size_t new_capacity);

// Modifiers
int vector_push_back(intVector_t* vec, int element);
void vector_clear(intVector_t* vec);
void vector_update(intVector_t* vec, int element, size_t pos);
int vector_get(intVector_t* vec, size_t pos);
int* vector_at(intVector_t* vec, size_t pos);
int vector_insert(intVector_t* vec, int element, size_t pos);
void vector_erase(intVector_t* vec, size_t pos);

// Operations
size_t vector_find(intVector_t* vec, int element, size_t start);
#endif

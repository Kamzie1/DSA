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
    } vector_t;

    void vector_init(vector_t* vec, size_t capacity);

#else 

    typedef struct vector_impl vector_t;

#endif

// Status Codes
#define BAD_ALLOC -1
#define SUCCESS 0
#define OUT_OF_RANGE 1

// Allocations
vector_t* vector_create(size_t capacity);
void vector_free(vector_t* vec);
vector_t* vector_copy(vector_t* vec);

// Capacity
int vector_empty(vector_t* vec);
size_t vector_size(vector_t* vec);
size_t vector_capacity(vector_t* vec);
size_t vector_max_size(void);
int vector_reserve(vector_t* vec, size_t new_capacity);

// Modifiers
int vector_push_back(vector_t* vec, int element);
void vector_clear(vector_t* vec);
void vector_update(vector_t* vec, int element, size_t pos);
int vector_get(vector_t* vec, size_t pos);
int* vector_at(vector_t* vec, size_t pos);
int vector_insert(vector_t* vec, int element, size_t pos);
void vector_erase(vector_t* vec, size_t pos);

// Operations
size_t vector_find(vector_t* vec, int element, size_t start);
#endif

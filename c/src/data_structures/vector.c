#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "utils.h"

#define DSA_EXPOSED
#include "data_structures/vector.h"

#ifndef VECTOR_CAPACITY_STRATEGY
#define VECTOR_CAPACITY_STRATEGY 2;
#endif

static inline size_t get_new_capacity(size_t old_capacity);

void vector_init(vector_t* vec, size_t capacity){
    if(vec == NULL){
        vec = (vector_t*)malloc(sizeof(vector_t));
    }
    vec->data = (int*)malloc(capacity * sizeof(int));
    vec->size = 0;
    vec->capacity = capacity;
}

vector_t* vector_create(size_t capacity){
    vector_t* vec = (vector_t*)malloc(sizeof(vector_t));
    if(vec == NULL){
        return NULL;
    }
    vec->data = (int*)malloc(capacity * sizeof(int));
    vec->size = 0;
    vec->capacity = capacity;
    return vec;
}

void vector_free(vector_t* vec){
    assert(vec != NULL && "Vector pointer must not be NULL");
    free(vec->data);
    free(vec);
    vec = NULL;
}

vector_t* vector_copy(vector_t* vec){
    assert(vec != NULL && "Vector pointer must not be NULL");
    vector_t* vec_copy= (vector_t*)malloc(sizeof(vector_t));
    vec_copy->data = (int*)malloc(vec->capacity * sizeof(int));
    memcpy(vec_copy->data, vec->data, vec->capacity);
    vec_copy->capacity = vec->capacity;
    vec_copy->size = vec->size;
    return vec_copy;
}

// Capacity
int vector_empty(vector_t* vec){
    assert(vec != NULL && "Vector pointer must not be NULL");
    return vec->size == 0;
}
size_t vector_size(vector_t* vec){
    assert(vec != NULL && "Vector pointer must not be NULL");
    return vec->size;
}
size_t vector_capacity(vector_t* vec){
    assert(vec != NULL && "Vector pointer must not be NULL");
    return vec->capacity;
}
size_t vector_max_size(void){
    return SIZE_MAX;
}
int vector_reserve(vector_t* vec, size_t new_capacity){
    assert(vec != NULL && "Vector pointer must not be NULL");
    assert(new_capacity >= vec->capacity && "New capacity must be greater than the old one.");

    int* new_data = (int*)realloc(vec->data, new_capacity * sizeof(int));
    if(new_data == NULL){
        return BAD_ALLOC;
    }
    vec->data = new_data;
    vec->capacity = new_capacity;
    return SUCCESS;
}

// Modifiers
int vector_push_back(vector_t* vec, int element){
    assert(vec != NULL && "Vector pointer must not be NULL");
    if(vec->size >= vec->capacity){
       size_t new_capacity = get_new_capacity(vec->capacity);
       int status = vector_reserve(vec, new_capacity);
       if(status != SUCCESS){
           return status;
       }
    }
    vec->data[vec->size] = element;
    vec->size++;
    return SUCCESS;
}
void vector_clear(vector_t* vec){
    assert(vec != NULL && "Vector pointer must not be NULL");
    vec->size = 0;
}
void vector_update(vector_t* vec, int element, size_t pos){
    assert(vec != NULL && "Vector pointer must not be NULL");
    assert(pos<vec->size && "Out of Range error");
    vec->data[pos] = element;
}
int vector_get(vector_t* vec, size_t pos){
    assert(vec != NULL && "Vector pointer must not be NULL");
    assert(pos<vec->size && "Out of Range error");

    return vec->data[pos];
}
int* vector_at(vector_t* vec, size_t pos){
    assert(vec != NULL && "Vector pointer must not be NULL");
    assert(pos<vec->size && "Out of Range error");

    return &vec->data[pos];
}
int vector_insert(vector_t* vec, int element, size_t pos){
    assert(vec != NULL && "Vector pointer must not be NULL");
    if(pos >= vec->size){
        return OUT_OF_RANGE;
    }
    size_t new_capacity = (vec->size >= vec->capacity) ? get_new_capacity(vec->capacity) : vec->capacity;
    int* new_data =(int*)malloc(new_capacity * sizeof(int));
    if(new_data == NULL){
        return BAD_ALLOC;
    }
    new_data[pos] = element;
    if(pos == 0){
        memcpy(new_data + 1, vec->data, vec->size);
    }
    else{
        memcpy(new_data, vec->data, pos-1);
        memcpy(new_data + pos + 1, vec->data + pos, vec->size - pos + 1);
    }
    free(vec->data);
    vec->data = new_data;
    vec->capacity = new_capacity;
    vec->size++;
    return SUCCESS;
}
void vector_erase(vector_t* vec, size_t pos){
    assert(vec != NULL && "Vector pointer must not be NULL");
    assert(vec != NULL && "Out of range error");
    utils_swap(&vec->data[pos], &vec->data[vec->size-1], sizeof(int));
    vec->size--;
}

// Operation
size_t vector_find(vector_t* vec, int element, size_t start){
    assert(vec != NULL && "Vector pointer must not be NULL");
    for(size_t i = start; i < vec->size; i++){
        if(vec->data[i] == element){
            return i;
        }
    }
    return vector_max_size();
}

// Private
static inline size_t get_new_capacity(size_t old_capacity){
    return old_capacity == 0 ? 4 : old_capacity * VECTOR_CAPACITY_STRATEGY;
}

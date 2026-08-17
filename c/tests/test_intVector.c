#include <signal.h>
#include <assert.h>
#include <stdio.h>

#include "test_utils.h"

#define DSA_EXPOSED
#define VECTOR_CAPACITY_STRATEGY 2
#include "data_structures/intVector.h"


void test_creation_and_capacity(void) {
    printf("Running test_creation_and_capacity:  ");
    
    intVector_t* vec = vector_create(5);
    assert(vec != NULL);
    
    assert(vector_size(vec) == 0);
    assert(vector_capacity(vec) == 5);
    assert(vector_empty(vec) == 1);
    
    // Test reserving memory
    assert(vector_reserve(vec, 20) == SUCCESS);
    assert(vector_capacity(vec) == 20);
    
    vector_free(vec);
    printf("\033[32mPASSED\033[0m\n");
}

void test_push_and_find(void) {
    printf("Running test_push_and_find: ");
    
    intVector_t* vec = vector_create(2);
    assert(vec != NULL);
    
    // Push elements (should trigger dynamic resizing)
    assert(vector_push_back(vec, 10) == SUCCESS && "push_back failed");
    assert(vector_push_back(vec, 20) == SUCCESS);
    assert(vector_push_back(vec, 30) == SUCCESS); 
    
    assert(vector_size(vec) == 3);
    assert(vector_empty(vec) == 0);
    assert(vector_capacity(vec) >= 3);
    
    // Verify elements exist at the correct expected positions
    assert(vector_find(vec, 10, 0) == 0 && "find doesn't work");
    assert(vector_find(vec, 20, 0) == 1);
    assert(vector_find(vec, 30, 0) == 2);
    
    // Test find with a starting offset
    assert(vector_find(vec, 10, 1) == (size_t)-1); // Shouldn't find 10 if we start at pos 1
    
    vector_free(vec);
    printf("\033[32mPASSED\033[0m\n");
}

void test_update_and_clear(void) {
    printf("Running test_update_and_clear: ");
    
    intVector_t* vec = vector_create(5);
    vector_push_back(vec, 100);
    vector_push_back(vec, 200);
    
    // Update existing element
    vector_update(vec, 999, 1);
    assert(vector_find(vec, 999, 0) == 1);
    assert(vector_find(vec, 200, 0) == (size_t)-1); // 200 should be overwritten
    
    // Test clear
    vector_clear(vec);
    assert(vector_size(vec) == 0);
    assert(vector_empty(vec) == 1);
    // Capacity should remain unchanged after a clear
    assert(vector_capacity(vec) >= 2); 
    
    vector_free(vec);
    printf("\033[32mPASSED\033[0m\n");
}

void test_insert_and_erase(void) {
    printf("Running test_insert_and_erase: ");
    
    intVector_t* vec = vector_create(5);
    vector_push_back(vec, 10);
    vector_push_back(vec, 30);
    
    // Insert in the middle
    assert(vector_insert(vec, 20, 1) == SUCCESS);
    assert(vector_size(vec) == 3);
    
    // Verify internal shift: [10, 20, 30]
    assert(vector_find(vec, 20, 0) == 1);
    assert(vector_find(vec, 30, 0) == 2);
    
    // Erase from the middle
    vector_erase(vec, 1);
    assert(vector_size(vec) == 2);
    
    // Verify internal shift: [10, 30]
    assert(vector_find(vec, 30, 0) == 1);
    assert(vector_find(vec, 10, 0) == (size_t)-1);
    
    
    vector_free(vec);
    printf("\033[32mPASSED\033[0m\n");
}

void test_error_handling(void) {
    printf("Running test_error_handling: ");
    

    signal(SIGABRT, assert_catcher);

    TEST_ASSERT(vector_push_back, NULL, 10); // This SHOULD trigger the assert

    intVector_t* vec = vector_create(2);
    vector_push_back(vec, 10);

    TEST_ASSERT(vector_size,NULL);       
    TEST_ASSERT(vector_capacity,NULL);       
    TEST_ASSERT(vector_free,NULL);
    TEST_ASSERT(vector_empty,NULL);
    TEST_ASSERT(vector_reserve,NULL, 1);
    TEST_ASSERT(vector_reserve,vec, 1);
    TEST_ASSERT(vector_clear,NULL);
    TEST_ASSERT(vector_update,NULL, 1, 1);
    TEST_ASSERT(vector_get,NULL, 1);
    TEST_ASSERT(vector_get,vec, 3);
    TEST_ASSERT(vector_at,NULL, 1);
    TEST_ASSERT(vector_at,vec, 4);
    TEST_ASSERT(vector_find,NULL, 1, 0);
    
    vector_free(vec);

    signal(SIGABRT, SIG_DFL);

    printf("\033[32mPASSED\033[0m\n");
}

void test_copy(void) {
    printf("Running test_copy: ");
    
    intVector_t* original = vector_create(5);
    vector_push_back(original, 1);
    vector_push_back(original, 2);
    vector_push_back(original, 3);
    
    intVector_t* clone = vector_copy(original);
    assert(clone != NULL);
    assert(vector_size(clone) == 3);
    
    // Modify the clone to ensure deep copy
    vector_update(clone, 99, 0);
    
    // Original should remain unchanged
    assert(vector_find(original, 1, 0) == 0);
    assert(vector_find(clone, 99, 0) == 0);
    
    vector_free(original);
    vector_free(clone);
    printf("\033[32mPASSED\033[0m\n");
}

int main(void) {
    printf("Starting Int Vector Test Suite\n");
    printf("--------------------------------\n");
    
    test_creation_and_capacity();
    test_push_and_find();
    test_update_and_clear();
    test_insert_and_erase();
    test_error_handling();
    test_copy();

    printf("--------------------------------\n");
    return 0;
}

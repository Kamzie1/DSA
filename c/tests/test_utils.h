#ifndef TEST_UTILS_H
#define TEST_UTILS_H

#include <setjmp.h>
#include <signal.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

jmp_buf jump_buffer;
int saved_stderr_fd = -1;


#define TEST_ASSERT(test_func, ...)                         \
if (setjmp(jump_buffer) == 0) {                             \
                                                            \
    TEST_ASSERT_INTERNAL(test_func, __VA_ARGS__);           \
                                                            \
    printf("\033[31mFAILED\033[0m (Assert did not fire)\n");\
    exit(1);                                                \
}                                                           \

#define TEST_ASSERT_INTERNAL(test_func, ...)  \
    saved_stderr_fd = dup(STDERR_FILENO);     \
    int null_fd = open("/dev/null", O_WRONLY);\
    dup2(null_fd, STDERR_FILENO);             \
    close(null_fd);                           \
                                              \
    test_func(__VA_ARGS__);                   \
                                              \
    dup2(saved_stderr_fd, STDERR_FILENO);     \
    close(saved_stderr_fd);                   \
    saved_stderr_fd = -1;                     \

static inline void assert_catcher(int sig) {
    if (sig == SIGABRT) {
        if (saved_stderr_fd != -1) {
            dup2(saved_stderr_fd, STDERR_FILENO);
            close(saved_stderr_fd);
            saved_stderr_fd = -1;
        }
        longjmp(jump_buffer, 1); 
    }
}

#endif

include(FetchContent)
FetchContent_Declare(googletest 
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG v1.18.0
    GIT_SHALLOW ON
    EXCLUDE_FROM_ALL
    SYSTEM)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

file(GLOB_RECURSE TESTS CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")

add_executable(my_tests ${TESTS})
target_link_libraries(my_tests PRIVATE ${DEBUG_NAME} gtest gtest_main)
target_compile_options(my_tests PRIVATE -g -Og -pedantic -Wall -Wextra)

include(GoogleTest)
gtest_discover_tests(my_tests)

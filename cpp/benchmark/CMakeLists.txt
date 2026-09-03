include(FetchContent)
FetchContent_Declare(
    googlebenchmark
    GIT_REPOSITORY https://github.com/google/benchmark.git
    GIT_TAG v1.9.5
)
set(BENCHMARK_ENABLE_TESTING OFF CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googlebenchmark)

file(GLOB_RECURSE BENCHMARKS CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")

add_executable(my_benchmarks ${BENCHMARKS})
target_link_libraries(my_benchmarks PRIVATE ${BENCHMARK_NAME} benchmark::benchmark benchmark::benchmark_main)
target_compile_options(my_benchmarks PRIVATE -Wall -Wextra -pedantic -march=native -Ofast -DNDEBUG)


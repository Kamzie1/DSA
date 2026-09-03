cmake_minimum_required(VERSION 3.28)
project(DSA)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

option(BUILD_TESTS "Build tests" OFF)
option(BUILD_BENCHMARKS "Build benchmarks" OFF)
option(RELEASE "Build release ready" ON)

# Get all cpp files
file(GLOB_RECURSE SRCS CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

if(RELEASE)
    add_library(${PROJECT_NAME} STATIC ${SRCS})

    target_compile_options(${PROJECT_NAME} PRIVATE -Wall -Wextra -pedantic -O3 -DNDEBUG)
    target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_23)
    target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_SOURCE_DIR}/include)
endif()

include(CTest)
if(BUILD_TESTS)
    enable_testing()
    set(DEBUG_NAME "${PROJECT_NAME}_debug")
    add_library(${DEBUG_NAME} STATIC ${SRCS})

    target_compile_options(${DEBUG_NAME} PRIVATE -Wall -Wextra -pedantic -g -Og -DDEBUG)
    target_compile_features(${DEBUG_NAME} PUBLIC cxx_std_23)
    target_include_directories(${DEBUG_NAME} PUBLIC ${CMAKE_SOURCE_DIR}/include)

    add_subdirectory(tests)
endif()

if(BUILD_BENCHMARKS)
    set(BENCHMARK_NAME "${PROJECT_NAME}_benchmark")
    add_library(${BENCHMARK_NAME} STATIC ${SRCS})

    target_compile_options(${BENCHMARK_NAME} PRIVATE -Wall -Wextra -pedantic -march=native -Ofast -DNDEBUG)
    target_compile_features(${BENCHMARK_NAME} PUBLIC cxx_std_23)
    target_include_directories(${BENCHMARK_NAME} PUBLIC ${CMAKE_SOURCE_DIR}/include)

    add_subdirectory(benchmark)
endif()

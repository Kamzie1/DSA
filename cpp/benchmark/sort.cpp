#include <benchmark/benchmark.h>
#include <vector>
#include <random>
#include <algorithm>
#include "sort.hpp"

static void GenerateRandomData(std::vector<int>& data) {
    static std::mt19937 generator(42);
    std::uniform_int_distribution<int> distribution(1, 10000);
    std::generate(data.begin(), data.end(), [&]() { return distribution(generator); });
}

static void BmStdSort(benchmark::State& state) {
    size_t size = state.range(0);
    std::vector<int> data(size);

    for (auto _ : state) {
        state.PauseTiming();
        GenerateRandomData(data);
        state.ResumeTiming();

        std::sort(data.begin(), data.end());
        
        benchmark::DoNotOptimize(data.data());
    }
    state.SetComplexityN(state.range(0));
}

static void BmBubbleSort(benchmark::State& state) {
    size_t size = state.range(0);
    std::vector<int> data(size);

    for (auto _ : state) {
        state.PauseTiming();
        GenerateRandomData(data);
        state.ResumeTiming();

        dsa::sorting_algorithm::BubbleSort(data.begin(), data.end());
        
        benchmark::DoNotOptimize(data.data());
    }
    state.SetComplexityN(state.range(0));
}

BENCHMARK(BmStdSort)->RangeMultiplier(2)->Range(8, 8 << 10)->Complexity(benchmark::oNLogN);
BENCHMARK(BmBubbleSort)->RangeMultiplier(2)->Range(8, 8 << 10)->Complexity(benchmark::oNSquared);

#include <gtest/gtest.h>
#include "random"
#include <algorithm>
#include <vector>
#include <deque>
#include "sort.hpp"

// Utils
namespace {

struct SortConfig {
    std::size_t size;
    int min_val;
    int max_val;
    int seed;
};
std::ostream& operator<<(std::ostream& os, const SortConfig& config) {
    return os << "{ size: " << config.size 
              << ", min: " << config.min_val 
              << ", max: " << config.max_val 
              << ", seed: " << config.seed << " }";
}

template <class Container>
class SortingAlgorithmTest : public ::testing::TestWithParam<SortConfig>{
protected:
    std::mt19937 rng;
    using T = Container::value_type;
    Container original;
    Container expected;

    void SetUp() override {
        SortConfig config = GetParam();
        
        std::uniform_int_distribution<T> distr(config.min_val, config.max_val);
        rng.seed(config.seed);

        original.resize(config.size);
        std::generate(original.begin(), original.end(), [&]() { return distr(rng); });

        expected = original;
        std::sort(expected.begin(), expected.end());
    }};

// Tests
using SortingAlgorithmTestVector = SortingAlgorithmTest<std::vector<int>>;
TEST_P(SortingAlgorithmTestVector, MatchesStdSortOnRandomData) {
    dsa::Sort(original.begin(), original.end());

    EXPECT_EQ(original, expected);
}

using SortingAlgorithmTestQueue = SortingAlgorithmTest<std::deque<int>>;
TEST_P(SortingAlgorithmTestQueue, MatchesStdSortOnRandomData) {
    dsa::Sort(original.begin(), original.end());

    EXPECT_EQ(original, expected);
}

INSTANTIATE_TEST_SUITE_P(
    RandomDataTests,
    SortingAlgorithmTestVector,
    ::testing::Values(
        SortConfig{1000, -1000, 1000, 42},      // Standard random spread
        SortConfig{500, 0, 10, 1984},           // Lots of duplicate values
        SortConfig{100000, -50000, 50000, 1337} // Massive array stress test
    )
);

INSTANTIATE_TEST_SUITE_P(
    RandomDataTests,
    SortingAlgorithmTestQueue,
    ::testing::Values(
        SortConfig{1000, -1000, 1000, 42},      // Standard random spread
        SortConfig{500, 0, 10, 1984},           // Lots of duplicate values
        SortConfig{100000, -50000, 50000, 1337} // Massive array stress test
    )
);
} // namespace

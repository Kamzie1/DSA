#ifndef SORT_H
#define SORT_H

#include <iterator>
#include <concepts>

namespace dsa {
    namespace internal{
        template<std::random_access_iterator RandomIt, typename Compare>
        requires std::strict_weak_order<Compare, std::iter_value_t<RandomIt>, std::iter_value_t<RandomIt>>
        void BubbleSort(RandomIt begin, RandomIt end, Compare comp){
            if (begin == end){
                return;
            }
            auto k = end - 1;
            while(true){
                auto hopka = begin;
                for(auto it=begin;it!=k;++it){
                    if(comp(*(it+1), *it)){
                        std::iter_swap(it, it+1);
                        hopka = it;
                    }
                }
                k = hopka;
                if(hopka == begin){
                    break;
                }
            }
        }

    } // namespace internal
    
    namespace sorting_algorithm {
        template<std::random_access_iterator RandomIt>
        void BubbleSort(RandomIt begin, RandomIt end){
            internal::BubbleSort(begin, end, std::less<>{});     
        }

        template<std::random_access_iterator RandomIt, typename Compare>
        requires std::strict_weak_order<Compare, std::iter_value_t<RandomIt>, std::iter_value_t<RandomIt>>
        void BubbleSort(RandomIt begin, RandomIt end, Compare comp){
            internal::BubbleSort(begin, end, comp);     
        }
        
    } // namespace sorting_algorithm 
    
    template<std::random_access_iterator RandomIt>
    void Sort(RandomIt begin, RandomIt end){
        dsa::sorting_algorithm::BubbleSort(begin, end);
    }

    /// Implement custom Algorithm choice via reflections, when it is supported
    // template <auto Algorithm, std::random_access_iterator RandomIt>
    // void Sort(RandomIt begin, RandomIt end);
    
} // namespace dsa

#endif // SORT_H

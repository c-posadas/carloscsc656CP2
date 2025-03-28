#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

#include "sums.h"

void 
setup(int64_t N, double A[])
{
   printf(" inside sum_indirect problem_setup, N=%lld \n", N);
   // Initialize the array A with random numbers in the range 0..N-1
   for (int64_t i = 0; i < N; ++i) {
      A[i] = lrand48() % N;  // Assign a random value between 0 and N-1
   }
}

double
sum(int64_t N, double A[])
{
   printf(" inside sum_indirect perform_sum, N=%lld \n", N);
   double result = 0;
   int64_t indx = A[0]; // Start with the first index

   for (int64_t i = 0; i < N; ++i) {
      result += A[indx];  // Add value at the index specified by indx
      indx = A[indx];     // Update indx to the next value in the array
   }

   return result;
}


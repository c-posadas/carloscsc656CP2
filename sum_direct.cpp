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
   printf(" inside direct_sum problem_setup, N=%lld \n", N);
   // Initialize the array A with values 0..N-1 (or any other initial setup needed)
   for (int64_t i = 0; i < N; ++i) {
      A[i] = i;
   }
}

double
sum(int64_t N, double A[])
{
   printf("Inside direct_sum perform_sum, N=%lld \n", N);

   double result = 0;
   for (int64_t i = 0; i < N; ++i) {
      result += A[i]; // Perform the sum
   }

   return result;
}
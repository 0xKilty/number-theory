#include <stdio.h>

long long fast_exp(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b & 1) {
            res *= a;
        }
        a *= a;
        b >>= 1;
    }
    return res;
}


int main() {
    printf("%lld\n", fast_exp(31415, 69));
    return 0;
}
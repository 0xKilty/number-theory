/*
TODO:
- Fermats little theorm mod exp
- Find order function
- Diffie Hellman brute force
*/

#include <stdio.h>
#include <time.h>

int is_prime(int n) {
    int i = 2; 
    while (i <= n / 2) { 
        if (n % i == 0)
            return 0; 
        else
            i++; 
    } 
    return 1; 
}

int gcd(int a, int b){
    int temp;
    while (b != 0) {
        temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int eulers_totient(unsigned int n) {
    unsigned int result = 1;
    for (int i = 2; i < n; i++)
        if (gcd(i, n) == 1)
            result++;
    return result;
}

int mod_exp(int base, int power, int mod) {
    int temp = base;
    int res = 1;
    for (int i = 0; i < 32 - __builtin_clz(power); i++) {
        if ((power >> i) & 1) {
            res = (res * temp) % mod;
        }
        printf("%d %d\n", temp, i);
        temp = (temp * temp) % mod;
    }
    return res;
}

int main(int argc, char** argv) {
    clock_t start_time = clock();

    printf("%d\n", mod_exp(3, 15791304, 89));

    double elapsed_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;

    printf("%f\n", elapsed_time);

    return 0;
}
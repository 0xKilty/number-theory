#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LINE_LENGTH 1024
#define MAX_COLUMNS 2

struct Pair {
    long long a;
    long long b;
};

long long regular_exp(long long a, long long b) {
    long long res = 1;
    for (int i = 0; i < a; i++) {
        res *= a;
    }
    return res;
}

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

int get_number_of_rows(FILE *file) {
    char line[MAX_LINE_LENGTH];
    int num_rows = 0;
    while (fgets(line, MAX_LINE_LENGTH, file) != NULL) {
        num_rows++;
    }
    rewind(file);
    return num_rows;
}

void read_csv_file(FILE *file, struct Pair *pairs) {
    char line[MAX_LINE_LENGTH];
    int index = 0;
    while (fgets(line, MAX_LINE_LENGTH, file) != NULL) {
        long long first, second;
        if (sscanf(line, "%lld,%lld", &first, &second) != 2) {
            fprintf(stderr, "Error parsing line: %s\n", line);
            continue;
        }

        pairs[index].a = first;
        pairs[index].b = second;
        index++;
    }
}

int main() {    
    FILE *file = fopen("../data/random_numbers.csv", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    int num_rows = get_number_of_rows(file);
    struct Pair *pairs = (struct Pair *)malloc(num_rows * sizeof(struct Pair));
    read_csv_file(file, pairs);

    clock_t start = clock();
    for (int i = 0; i < num_rows; i++) {
        printf("%lld ^ %lld = %lld\n", pairs[i].a, pairs[i].b, fast_exp(pairs[i].a, pairs[i].b));
    }
    clock_t end = clock();
    double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Time taken: %f seconds\n", cpu_time_used);

    free(pairs);

    fclose(file);

    return 0;
}

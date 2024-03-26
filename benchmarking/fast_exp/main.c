#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024
#define MAX_COLUMNS 2

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
    
    char filename[] = "../data/random_numbers.csv";
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Could not open file %s\n", filename);
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';

        char *token;
        char *rest = line;
        int column_count = 0;
        while ((token = strtok_r(rest, ",", &rest)) != NULL) {
            printf("Value: %s\n", token);
            column_count++;
            if (column_count >= MAX_COLUMNS)
                break;
        }
    }

    fclose(file);

    return 0;
}
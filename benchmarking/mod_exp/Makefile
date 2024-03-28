CC=gcc
CFLAGS=-Wall
LIBS=-lgmp

all: main

main: main.c
	$(CC) $(CFLAGS) -o main main.c $(LIBS)

.PHONY: run
run: main
	./main

.PHONY: clean
clean:
	rm -f main

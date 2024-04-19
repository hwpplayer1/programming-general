.POSIX:
CC = cc
CFLAGS = -g -Wall -Werror -Wextra
LDFLAGS =

BIN = sample
OBJ = main.o

all: $(BIN)

$(BIN): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $(OBJ)

clean:
	rm -f $(BIN) *.o

.SUFFIXES: .c .o
.c.o:
	$(CC) $(CFLAGS) -c $<

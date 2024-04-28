.POSIX:
CC = cc
CFLAGS = -g -Wall -Werror -Wextra
LDFLAGS =
LDLIBS =

BIN = sample
OBJ = main.o

all: $(BIN)

$(BIN): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $(OBJ) $(LDLIBS)

clean:
	rm -f $(BIN) *.o

.SUFFIXES: .c .o
.c.o:
	$(CC) $(CFLAGS) -c $<

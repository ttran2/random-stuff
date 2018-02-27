CPP=c++
CPPFLAGS=

.PHONY: all clean

all:	sudoku

clean:
	rm -f *~ *.o sudoku

sudoku.o:	sudoku.cpp sudoku.h
	$(CPP) $(CPPFLAGS) -o sudoku.o -c sudoku.cpp

sudoku:	main.cpp sudoku.o
	$(CPP) $(CPPFLAGS) -o sudoku main.cpp sudoku.o


#ifndef __SUDOKU_H__
#define __SUDOKU_H__

#include <string>
#include <iostream>
#include <sstream>

#define SIZE 9

class Game
{
public:
	Game(void) {}
	~Game(void) {}
	void print_position(void);
	bool load_position(void);
	bool is_correct(void);
	bool is_solved(void);

private:
	bool _verify_board(bool bypass_zeroes);
	int board[SIZE][SIZE];
	int possibles[SIZE][SIZE];
	int variants[SIZE][SIZE];
};

#endif

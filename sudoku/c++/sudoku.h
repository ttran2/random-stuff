#ifndef __SUDOKU_H__
#define __SUDOKU_H__

#define SIZE 9

#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

class Poss
{
public:
	Poss(int x, int y, int n)
	{
		this->x = x;
		this->y = y;
		this->n = n;
	}

	int x, y, n;
	bool operator<(const Poss &a) const { return n < a.n; }
};


class GameState
{
public:
	int board[SIZE][SIZE];
	int x, y, move;
	GameState& operator=(GameState &a)
		{
			memcpy(&board, &a.board, sizeof(int) * SIZE * SIZE);
			x = a.x;
			y = a.y;
			move = a.move;
			return *this;
		}
};


class Game
{
public:
	Game(void) {}
	~Game(void) {}
	void print_position(void);
	bool load_position(void);
	bool is_correct(void);
	bool is_solved(void);
	void compute_possibilities(void);
	bool solve(void);

private:
	bool _verify_board(bool fail_on_zeroes);
	int _compute_possibilities(int x, int y);
	GameState gs;
	int variants[SIZE][SIZE];
	vector<Poss> nposs;
	vector<GameState> move_stack;
};

#endif

#include "sudoku.h"

using namespace std;

void Game::print_position(void)
{
	int i, j;
	for(i = 0; i < SIZE; i++)
	{
		for(j = 0; j < SIZE; j++)
		{
			cout << this->board[i][j] << " ";
			if(!((j + 1) % 3))
				cout << " ";
		}
		if(!((i + 1) % 3))
			cout << endl;
		cout << endl;
	}
}


bool Game::load_position(void)
{
	int i, j;
	string line;

	i = 0;
	while(getline(cin, line))
	{
		if(line.empty())
			continue;
		stringstream stream(line);
		for(j = 0; j < SIZE; j++)
		{
			if((stream >> this->board[i][j]).fail())
				return false;
			if(board[i][j] < 0 || board[i][j] > SIZE)
				return false;
		}
		// more than SIZE numbers in a row --> misshapen
		if(stream.rdbuf()->in_avail())
			return false;
		i++;
	}
	if(i != SIZE)
		return false;
	return true;
}


bool Game::_verify_board(bool fail_on_zeroes)
{
	int map;
	int i, j, ii, jj;

	// rows
	for(i = 0; i < SIZE; i++)
	{
		map = 0;
		for(j = 0; j < SIZE; j++)
			if(this->board[i][j])
				if((map >> this->board[i][j]) & 1)
					return false;
				else
					map |= 1 << this->board[i][j];
			else
				if(fail_on_zeroes)
					return false;
	}

	// columns
	for(i = 0; i < SIZE; i++)
	{
		map = 0;
		for(j = 0; j < SIZE; j++)
			if(this->board[j][i])
				if((map >> this->board[j][i]) & 1)
					return false;
				else
					map |= 1 << this->board[j][i];
			else
				if(fail_on_zeroes)
					return false;
	}

	// squares
	for(ii = 0; ii < SIZE / 3; ii++)
		for(jj = 0; jj < SIZE / 3; jj++)
		{
			map = 0;
			for(i = ii * 3; i < ii * 3 + 3; i++)
				for(j = jj * 3; j < jj * 3 + 3; j++)
					if(this->board[i][j])
						if((map >> this->board[i][j]) & 1)
							return false;
						else
							map |= 1 << this->board[i][j];
					else
						if(fail_on_zeroes)
							return false;
		}

	return true;
}


bool Game::is_correct(void)
{
	return this->_verify_board(false);
}


bool Game::is_solved(void)
{
	return this->_verify_board(true);
}

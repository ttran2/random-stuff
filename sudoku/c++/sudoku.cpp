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
	int m;
	int i, j, ii, jj;

	// rows
	for(i = 0; i < SIZE; i++)
	{
		m = 0;
		for(j = 0; j < SIZE; j++)
			if(this->board[i][j])
				if((m >> this->board[i][j]) & 1)
					return false;
				else
					m |= 1 << this->board[i][j];
			else
				if(fail_on_zeroes)
					return false;
	}

	// columns
	for(i = 0; i < SIZE; i++)
	{
		m = 0;
		for(j = 0; j < SIZE; j++)
			if(this->board[j][i])
				if((m >> this->board[j][i]) & 1)
					return false;
				else
					m |= 1 << this->board[j][i];
			else
				if(fail_on_zeroes)
					return false;
	}

	// squares
	for(ii = 0; ii < SIZE / 3; ii++)
		for(jj = 0; jj < SIZE / 3; jj++)
		{
			m = 0;
			for(i = ii * 3; i < ii * 3 + 3; i++)
				for(j = jj * 3; j < jj * 3 + 3; j++)
					if(this->board[i][j])
						if((m >> this->board[i][j]) & 1)
							return false;
						else
							m |= 1 << this->board[i][j];
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


int Game::_compute_possibilities(int x, int y)
{
	int m = 0x1ff;
	int n = 0;
	int i, j;

	// rows + columns
	for(i = 0; i < SIZE; i++)
	{
		if(this->board[i][y])
			m &= ~(1 << (this->board[i][y] - 1));
		if(this->board[x][i])
			m &= ~(1 << (this->board[x][i] - 1));
	}

	// squares
	for(i = x - (x % 3); i < x - (x % 3) + 2; i++)
		for(j = y - (y % 3); j < y - (y % 3) + 2; j++)
		{
			if(this->board[i][j])
				m &= ~(1 << (this->board[i][j] - 1));
		}

	// compute number of possibilities
	for(i = 0; i < SIZE; i++)
		if(1 & (m >> i))
			n++;

	this->nposs.push_back(Poss(x, y, n));
	return m;
}


void Game::compute_possibilities(void)
{
	int i, j;
	this->nposs.clear();
	for(i = 0; i < SIZE; i++)
		for(j = 0; j < SIZE; j++)
		{
			if(this->board[i][j] == 0)
				this->variants[i][j] = this->_compute_possibilities(i, j);
			else
				this->variants[i][j] = 0;
		}
	sort(nposs.begin(), nposs.end());
}


inline int extract_number(int a)
{
	int i = 0;
	while(!(a & 1))
	{
		i++;
		a >>= 1;
	}
	return i + 1;
}


bool Game::solve(void)
{
	while(!this->is_solved())
	{
		this->compute_possibilities();
		if(!this->nposs.empty())
			if(this->nposs[0].n == 1)
			{
				this->board[this->nposs[0].x][this->nposs[0].y] = extract_number(this->variants[this->nposs[0].x][this->nposs[0].y]);
			}
			else
			{
				return false;
			}
	}
	return true;
}

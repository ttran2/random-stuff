#include "sudoku.h"
#include <cstring>

using namespace std;

int main(int argc, char *argv[])
{
	Game g;
	bool solve_opt = false;
	bool solvable_position = false;
	bool success;

	// handle options
	if(argc > 1)
		if(strcmp(argv[1], "--solve") == 0)
			solve_opt = true;


	// load position
	if(!g.load_position())
	{
		cout << "error" << endl;
		return 1;
	}

	// print position
	g.print_position();

	// decide whether the position is solved, correct or incorrect
	if(g.is_correct())
		if(g.is_solved())
			cout << "solved" << endl;
		else
		{
			cout << "correct" << endl;
			solvable_position = true;
		}
	else
		cout << "incorrect" << endl;

	if(solve_opt && solvable_position)
	{
		success = g.solve();
		g.print_position();
		if(success)
			cout << "solved" << endl;
		else
			cout << "FAIL: I am too dumb to solve this!" << endl;
	}

	return 0;
}

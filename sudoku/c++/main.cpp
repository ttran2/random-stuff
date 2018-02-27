#include "sudoku.h"

using namespace std;

int main(void)
{
	Game g;

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
			cout << "correct" << endl;
	else
		cout << "incorrect" << endl;

	return 0;
}

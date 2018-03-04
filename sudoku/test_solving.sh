#!/bin/bash

TOOL=${1:-sudoku.py}
if ! [[ $TOOL =~ ^/ ]]; then
	TOOL="./$TOOL"
fi

SOLVING_OPTION=--solve

FAILED=0

for testcase in `ls solving_tests`; do
	RESULT=`$TOOL $SOLVING_OPTION < solving_tests/$testcase | tail -n 1`
	if [ "$RESULT" = "solved" ]; then
		echo "solving test :: `basename $testcase .dat` :: PASS"
	else
		echo "solving test :: `basename $testcase .dat` :: FAIL"
		(( FAILED += 1 ))
	fi
done

exit $FAILED

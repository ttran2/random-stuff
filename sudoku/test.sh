#!/bin/bash

TOOL=${1:-sudoku.py}
if ! [[ $TOOL =~ ^/ ]]; then
	TOOL="./$TOOL"
fi

FAILED=0

for testtype in `ls tests`; do
	for i in tests/$testtype/*.dat; do
		RESULT=`$TOOL < $i | tail -n 1`
		if [ "$RESULT" = "$testtype" ]; then
			echo "$testtype :: `basename $i .dat` :: PASS"
		else
			echo "$testtype :: `basename $i .dat` :: FAIL"
			(( FAILED += 1 ))
		fi
	done
done

exit $FAILED

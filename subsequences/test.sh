#!/bin/bash

TOOL=${1:-subsequences.py}

if ! [[ $TOOL =~ ^/ ]]; then
	TOOL="./$TOOL"
fi

FAILED=0

for i in tests/*.dat; do
	OUT=`$TOOL < $i`
	GOLDEN=tests/`basename $i .dat`.golden
	diff -q <(echo $OUT) $GOLDEN &>/dev/null
	if [ $? -eq 0 ]; then
		echo "`basename $i .dat` : PASS"
	else
		echo "`basename $i .dat` : FAIL"
		echo -e "\\tCorrect output: `cat $GOLDEN`"
		echo -e "\\tYour output:    $OUT"
		(( FAILED += 1 ))
	fi
done

exit $FAILED

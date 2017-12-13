#!/bin/bash

TOOL=${1:-game15}
if ! [[ $TOOL =~ ^/ ]]; then
	TOOL="./$TOOL"
fi

FAILED=0

for i in tests/*.dat; do
	RESULT=`$TOOL < $i | tail -n 1`
	SHOULD_BE=`basename $i | sed 's/_.*//'`
	if [ "$RESULT" = "$SHOULD_BE" ]; then
		echo "`basename $i .dat` : PASS"
	else
		echo "`basename $i .dat` : FAIL"
		(( FAILED += 1 ))
	fi
done

exit $FAILED

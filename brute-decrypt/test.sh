#!/bin/bash

FILE=${1:-brute_decrypt_v2}

echo "Testing '$FILE'..."

for txtFile in texts/plain/text_*.txt; do
	#txtTitle=${txtFile##*/}
	#txtTitle=${txtTitle%.txt}
	txtTitle=$(basename $txtFile .txt)
	#CORRECT=$( cat $txtFile )
	echo $txtFile

	for encrFile in texts/encrypted/$txtTitle.*.encr; do
		#diff -q <( cat $encrFile | ./$FILE 2> /dev/null ) $txtFile &>/dev/null
		diff -q <( ./$FILE < $encrFile 2> /dev/null ) $txtFile &>/dev/null

		if [ $? -eq 0 ]; then
			echo "$encrFile : PASS"
		else
			echo "$encrFile : FAIL"
			#echo -e "\\tCorrect output:\n$(cat $txtFile)"
			#echo -e "\t\tYour output:\n$OUTPUT"
		fi

	done

done

#!/usr/bin/env bash
SIZE=200000
SECONDS=0
TEST_CASES=10
for((i=0;i<$TEST_CASES;i++))
do 
	echo "case $i:"
    python3 gen.py "$SIZE" > input.in
    cat input.in
    python3 tested.py < input.in
done
duration=$SECONDS
avg=$(echo "$duration / $TEST_CASES" | bc -l)
printf "Average of %.2f seconds elapsed per test cases" $avg
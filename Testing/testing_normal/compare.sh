#!/usr/bin/env bash
SIZE_BIG=1000
SIZE_SMALL=5
SECONDS=0
TEST_CASES=100
for((i=0;i<$TEST_CASES;i++))
do 
	echo "case $i:"
    python3 gen.py "$SIZE_SMALL" > small.in
    python3 gen.py "$SIZE_BIG" > big.in
    diff -w <(python3 tested.py < small.in) <(python3 brute_force.py < small.in)||break
    diff -w <(python3 tested.py < big.in) <(python3 brute_force.py < big.in)||break
done
duration=$SECONDS
avg=$(echo "$duration / $TEST_CASES" | bc -l)
printf "Average of %.2f seconds elapsed per test cases" $avg
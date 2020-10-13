#!/bin/bash

read -p "Enter a number: " var

tmp=1
count=0
while [ $count -lt $var ];do
	count=$(echo "$count + 1" | bc)
	tmp=$(echo "$tmp * $count" | bc)
	

done

echo "Factorial=  "$tmp""
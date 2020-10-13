#!/bin/bash

read -p "Enter N limit: " n 

count=0
sum=0
while [ $count -le $n ];do
	if [ `echo "$count % 2"|bc` -eq 0 ];then
		sum=$(echo "$sum+1" | bc)
		
	fi
	

	count=$(echo "$count + 1"| bc)
done

echo "sum = $sum"
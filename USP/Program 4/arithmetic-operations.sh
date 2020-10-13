#!/bin/bash


	read -p "Enter a Two Numbers: " num1 num2
	echo "$num1 $num2"

    read -p "Choose operation: +,-,/,* " choice
    
    case $choice in
    	"+" )
		echo "$num1 + $num2="
    	echo "$num1 + $num2" | bc	;;
    	"-" )
		echo "$num1 - $num2="
		echo "$num1 - $num2" | bc	;;
		"*" )
   		echo "$num1 * $num2="
		echo "$num1 * $num2" | bc	;;
		"/" )
		echo "$num1 / $num2="
		echo "scale=2;$num1 / $num2" | bc	;;
		"%" )
		echo "$num1 % $num2="
		echo "scale=2;$num1 % $num2" | bc	;;
    esac

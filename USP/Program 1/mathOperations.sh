echo "Enter Two numbers--->\nEnter First number: "
read number1
echo "Enter Second number: "
read number2
add=`expr $number1 + $number2`
sub=`expr $number1 - $number2`
div=`expr $number1 / $number2`
mult=`expr $number1 \* $number2`
echo "Sum: $add\nDifference: $sub\nDivision: $div\nMultiplication: $mult"
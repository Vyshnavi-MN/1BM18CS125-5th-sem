echo "Enter a number"
read num
if test $num -gt 0
then
    echo "Number is positive"
elif test $num -lt 0
then
    echo "Number is negative"
else
    echo "Number is zero"
fi

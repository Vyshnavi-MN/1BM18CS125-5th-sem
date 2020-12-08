a=$#
echo "Number of arguments are" $a
x=$*
c=$a
res=''
while [ 1 -le $c ]
do
c=`expr $c - 1`
shift $c
res=$res' '$1
set $x
done
echo "Arguments in reverse order $res"
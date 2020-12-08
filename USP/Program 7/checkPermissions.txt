if [ $# -ne 2 ]
then
echo "pass 2 argument"
exit
fi
echo "enter file name"
read f1
echo "enter the second file name"
read f2
p1=`ls -l $f1 | cut -c 2-10`
p2=`ls -l $f2 | cut -c 2-10`
if [ $p1 = $p2 ]
then
echo "permissions are same"
echo "$p1"
else
echo "permissions are different"
echo "permission of file $f1 is $p1"
echo "permission of file $f2 is $p2"
fi
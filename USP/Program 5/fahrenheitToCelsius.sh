clear
echo -n "Enter temperature (F) : "
read tf
tc=$(echo "scale=2;(5/9)*($tf-32)"|bc)
echo "$tf F ---> $tc C"

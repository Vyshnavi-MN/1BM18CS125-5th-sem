echo "Enter basic salary: "
read basicSalary
da=`expr $basicSalary + $basicSalary \* 20 / 100`
hra=`expr $basicSalary + $BasicSalary \* 30 / 100`
grossSalary=`expr $da + $hra`
echo "Gross Salary = $grossSalary"

read a
read b
read c

if [ $a -eq $b ] && [ $b -eq $c ] && [ $c -eq $a ]
then
	echo "EQUILATERAL"
else
	if [ $a -eq $b ] || [ $b -eq $c ] || [ $c -eq $a ]
	then
		echo "ISOSCELES"
	else
		echo "SCALENE"
	fi
fi

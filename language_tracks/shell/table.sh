echo "enter a number"
read num1
for var in 1 2 3 4 5 6 7 8 9 10
do
	echo "$(($num1 * var))"
done

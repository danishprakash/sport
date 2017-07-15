var=1

while [ $var -le 100 ]
do
	if [ $((var%2)) != 0 ]; then
		echo $var
	fi
	var=$((var+1))
done

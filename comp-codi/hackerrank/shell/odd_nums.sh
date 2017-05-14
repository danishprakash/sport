for VAR in {1..99}
do
    let a=$((VAR/"2"))
    if ["$a" -ne "0"]
    then
        echo $VAR
    fi
done

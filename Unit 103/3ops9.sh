user=x
while [ $user = x ]
do
echo "Choose from options 1, 2, or 3"
echo "1. Hello World"
echo "2. Ping a website or ip address:"
echo "3. Run iconfig"

read input 
if [ $input = 1 ]
    then echo"Hello World"
    elif [ $input = 2 ]
        then
            echo "Enter website or ip addressto ping"
            read address
            ping -c 5 $address
    elif [ $input = 3 ] 
        then
            ifconfig
            esle
                echo "Invaild entry"
    fi
    echo "Do you want to play again: Y/N
    read user
done
    echo "Good work"
              
#!/bin/bash
#set -x
set -o errexit
#set -o nounset

print()
{
    if [[ "$1" -eq 3 ]];then echo -n "Pling"
    elif [[ "$1" -eq 5 ]];then echo -n "Plang"
    elif [[ "$1" -eq 7 ]];then echo -n "Plong"
    fi
}

raindrops1()
{
    if ! [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Usage: ${0} <number>"
    exit 1      
    fi

    declare -i number="$1"
    declare -a prime=(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
    declare -a finall
    #if [[ $number -eq 12 ]]; then echo "OK, ${prime[0]}"; else echo "NO, ${prime[1]}"; fi   
    for i in ${prime[@]}; do
        #echo -e "$i \n"
        #echo -e "${prime[$i]} \n"
        while [[ $number%$i -eq 0 ]]; do
            finall+=("$i")
            #echo "$i"
            print "$i"
            let number=$number/$i
            for j in ${prime[@]}; do
                if [[ $number -eq $j ]]; then 
                    finall+=("$number")
                    #echo "$number"  
                    print "$number"                  
                    break  
                fi
            done               
        done   
    done
echo -e "\n ${finall[@]}"
#test="test1"

}
raindrops2()
{
    raindrops1 "$@"
    echo "${finall[@]}"
    echo "${finall[0]}"
    echo "$test"

}
main()
{
    raindrops2 "$@"
}
main "$@"
#print "$1"

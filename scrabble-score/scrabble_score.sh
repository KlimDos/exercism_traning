#!/bin/bash
#set -x
set -o errexit
set -o nounset

scrabble ()
{
    declare -a one=(A E I O U L N R S T a e i o u l n r s t)
    declare -a two=(D G d g)
    declare -a three=(B C M P b c m p)
    declare -a four=(F H V W Y f h v w y)
    declare -a five=(K k)
    declare -a eight=(J X j x)
    declare -a ten=(Q Z q z)
    #echo ${one[$1]}
    
    word="$1"
    length=${#1}
    i=0
    result=0
    while [ $i -lt $length ];do
        #echo $i
        char=${word:$i:1}
        if [[ " ${one[*]} " == *" $char "* ]]; then
            let result+=1
        elif [[ " ${two[*]} " == *" $char "* ]]; then
            let result+=2
        elif [[ " ${three[*]} " == *" $char "* ]]; then
            let result+=3
        elif [[ " ${four[*]} " == *" $char "* ]]; then
            let result+=4
        elif [[ " ${five[*]} " == *" $char "* ]]; then
            let result+=5
        elif [[ " ${eight[*]} " == *" $char "* ]]; then
            let result+=8
        elif [[ " ${ten[*]} " == *" $char "* ]]; then
            let result+=10
        fi
        #echo "$char ++"
        let i+=1
    done
    echo $result
}

main ()
{
    scrabble "$@"
}
main "$@"
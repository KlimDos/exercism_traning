#!/bin/bash
#set -x
#set -o errexit
#set -o nounset

input_handler ()
{
    if [[ -z "$1" ]] || [[ $# -gt 1 ]] || ! [[ "$1" =~ ^[[:digit:]]+$ ]]; then
        echo -e "Error: invalid input"
        exit 1
    fi
}

invariant ()
{
    input_handler "$@"

    num_len=${#1}
    length="$num_len"
    for ((i=0; i < ${#1}; i++)); do
    {
        let result+="(${1:i:1}**$num_len)"
        
    }      
    done
    echo $result    
}

main ()
{
    if [[ $(invariant "$@") == "$1" ]]; then echo "true"; else echo "false"; fi
}
main "$@"
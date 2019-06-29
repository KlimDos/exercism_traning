#!/bin/bash
#set -x
set -o errexit
#set -o nounset

gcount()
{
    if [[ $1 -gt 62  ]]; then
        NUM=$(echo "2 ^ $(($1-1))" | bc)        
        echo -e "$NUM"
    else      
        echo -e "$((2**$(($1-1))))" 
    fi   
    exit 0  
}

grains ()
{
    if [[ -z "$1" ]] || [[ $# -gt 1 ]] || ! [[ "$1" =~ ^([1-9]|[1-5][0-9]|6[0-4])$ ]] && [[ "$1" != "total" ]]; then
        echo -e "Error: invalid input"
        exit 1
    fi
    
    if [[ "$1" = "total" ]]; then 
        total=0
        for i in {0..63}; do
            NUM=$(gcount "$(($i+1))")
            total=$(echo "$total+$NUM" | bc)    
        done
        echo $total  
        exit 0      
    else
        gcount "$@"
        exit 0
    fi
    exit 0    
}

main()
{
    grains "$@"
}
main "$@"
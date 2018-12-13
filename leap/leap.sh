#!/bin/bash
#set -x
#set -o errexit
#set -o nounset

leap ()
{
    if [[ "$#" -eq 0 ]] || [[ "$#" -gt 1 ]] || ! [[ "$1" =~ ^[0-9]+$ ]]; then
        echo "Usage: ${0} <year>"
        exit 1      
    fi

    if [[ $1%4 -eq 0 ]] && [[ $1%100 -ne 0 ]] || [[ $1%400 -eq 0 ]]; 
    then 
        echo "true"
    else echo "false"
    fi
    
}
main ()
{
    leap "$@"
}
main "$@"
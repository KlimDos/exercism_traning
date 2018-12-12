#!/bin/bash
#set -x
#set -o errexit
#set -o nounset

error_handler()
{
    if [ "$#" -eq 0 ]; then
        echo "Usage: ./${0%.*} <greetee>"
        exit 1      
    elif [ "$#" -eq 1 ]; then
        echo "Hello, $1"
    else 
        exit 1
    fi
}

main()
{
    error_handler "$@"
}
main "$@"
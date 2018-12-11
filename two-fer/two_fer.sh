#!/bin/bash
#for debug
#set -x
# exit when there is an error
#set -o errexit
# when it tries to use an unset variable
#set -o nounset

two_fer ()
    {
       #var1="${1:-you}"     
       echo "One for ${1:-you}, one for me."
    }

main ()
{
    two_fer "$*"
}
main "$*"
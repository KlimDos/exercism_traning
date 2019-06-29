#!/bin/bash
#set -x
main ()
{
    for file; do
        echo -e "--$file \n"
    done
}
main "$@"
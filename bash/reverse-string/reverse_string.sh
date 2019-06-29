#!/bin/bash
#set -x
# This option will make the script exit when there is an error
#set -o errexit
# This option will make the script exit when it tries to use an unset variable
#set -o nounset

function hello ()
  {
    echo -e "Hello, World!"
    exit 0
  }

reverse ()
  {
    local var1
    var1="$1"
    echo -e "$1" "\n"
    #last_char=${var1##}
    length=${#var1}
    last_char=${var1:$length-1:1}
    #echo -e $last_char
    while [ $length -ne 0 ]
    do
      last_char=${var1:$length-1:1}
      echo -n "$last_char"   
      if [ -n "$var1" ]
      then
        var1=${var1:0:-1}
      fi
    length=${#var1}
    done
    echo -e "\n"
  } 

main() {
  # A string variable containing only the FIRST argument passed to the script,
  # you can use input="$@" to get a string with ALL arguments
  #input=$1

  # Add your code here  
reverse "$*"

}


# Calls the main function passing all the arguments to it via '$@'
# The argument is in quotes to prevent whitespace issues
main "$@"
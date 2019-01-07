#!/bin/bash
#set -x
#set -o errexit
#set -o nounset

input_handler() {
	if [[ -z "$1" ]] || [[ $# -gt 1 ]] || ! [[ "$1" =~ ^[1-9][0-9]*$ ]]; then
		echo -e "Error: Only positive numbers are allowed"
		exit 1
	fi
}

collatz() {
	n="$1"
    round=0
	while [ $n -ne 1 ]; do
		{
			if [ $(($n % 2)) -eq 0 ]; then let n=$n/2; else	let n=$n*3+1; fi
            let round+=1
		}
	done
    echo $round
}
main() {
	input_handler "$@"
	collatz "$@"
}
main "$@"

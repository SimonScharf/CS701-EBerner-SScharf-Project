#!/bin/bash


input_file="$1"

if [ \! -f "$input_file" ]; then
    echo "Error: input file \"$input_file\" inaccessible" >&2
    exit 1
fi

#sudo -v simply requests a password so that sudo tcpdump can run in background
#and already have sudo permissions. (since background tcpdump & cannot read from stdin)
sudo -v

while read url count; do
    output_filename="$(echo "$url" | awk -F "." '{ print $2 }')"
    echo "I'm going to fetch $url $count times"

    for i in $(seq $count); do
        echo -e "\n\ninteration $i will be saved in ${output_filename}${i}.txt\n"
    	sudo tcpdump -n > ${output_filename}Data${i}.txt &
    	tcpdump_pid="$!"

     	curl -o /dev/null $url 
	    if test "$?" != "0"; then
            echo "the curl command failed with: $res"
    	else
            echo "the curl command ran successfully"
	    fi
        kill $tcpdump_pid
    done
done < $input_file

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
    website_name="$(echo "$url" | awk -F "." '{ print $2 }')"
    echo -e "\nI'm going to fetch $url $count times"
    pathname_prefix=REQUESTS/${website_name}/DATA/${website_name}

    for i in $(seq $count); do
        echo "iteration $i will be saved in ${pathname_prefix}Data${i}.txt"
    	sudo tcpdump -n > ${pathname_prefix}Data${i}.txt 2> /dev/null &
        tcpdump_pid="$!"
        
        #if [ "$website_name" == "amazon" ] || [  "$website_name" == "chase" ] || [ "$website_name" == "google" ] || [ "$website_name" == "wikipedia" ] ; then
                sleep 5
	#fi

     	curl &> /dev/null $url 
	    if test "$?" != "0"; then
            echo "the curl command failed with: $res"
    	else
            echo "the curl command ran successfully"
	    fi
        
        sudo kill $tcpdump_pid &> /dev/null
        #echo "I am going to check if there are processes being run"
        #this next line make sure that all tcpdump processes are killed
        ps auxww | grep tcpdump | awk '{ print $2 }' | xargs sudo kill &> /dev/null


        python3 tcpOutputParser.py ${pathname_prefix}Data${i}.txt > ${pathname_prefix}CleanedData${i}.txt 
        echo "cleaned data will be saved in ${pathname_prefix}CleanedData${i}.txt" 
        #python3 plot.py ${pathname_prefix}CleanedData${i}.txt ${website_name} ${i} > REQUESTS/${website_name}/PLOTS/${website_name}${i}_DataPoints.txt
    done

done < $input_file

#!/bin/bash


sudo tcpdump -n > UnknownDemoData.txt 2> /dev/null &
tcpdump_pid="$!"

echo "Enter URL for prediction model...."
read unknownURL

echo "curling ${unknownURL}...."
curl -H @headers $unknownURL &>/dev/null

sudo kill $tcpdump_pid &> /dev/null
ps auxww | grep tcpdump | awk '{ print $2 }' | xargs sudo kill &> /dev/null


echo -e "Cleaning tcpdump packet data....\n"
python3 tcpOutputParser.py UnknownDemoData.txt > CleanedUnknownDemoData.txt

echo -e "Bucketizing cleaned data....\n"
python3 bucketize.py CleanedUnknownDemoData.txt > BucketizedDemoData.txt 

echo -e "Predicting website....\n"
python3 mlpWebsitePredictor.py BucketizedDemoData.txt




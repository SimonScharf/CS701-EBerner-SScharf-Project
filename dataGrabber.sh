#!/bin/bash
read url

curl $url > /dev/null 
res=$?
if test "$res" != "0"; then
   echo "the curl command failed with: $res";
else echo "the curl command ran successfully with: $res";
fi

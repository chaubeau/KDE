#!/bin/bash
#chaubeau@gmail.com

#you need to set the MYSQL variable according to the environment
MYSQL='/home/mysql/mysql/bin/mysql --defaults-extra-file=/home/mysql/mysql/etc/user.root.cnf'
concurrent_number=$1

TMP_FIFO_FILE=./$$.fifo
mkfifo "$TMP_FIFO_FILE"
exec 6<>"$TMP_FIFO_FILE"

rm ./$$.fifo
for ((j=0;j<${concurrent_number};j++))
do
        echo
done >&6

cat test.sql|while read i
do
     read -u6
     {
        #TEST CASE 
		$MYSQL -e "begin;$i;select sleep(3);commit;"
     }&
done

echo >&6
wait
exec 6>&-

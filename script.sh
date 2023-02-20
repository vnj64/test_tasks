#!bin/bash

IP="-- enter your ip server --"
PATH="-- enter path to directory --"
for ((i=1; i<=20; i++))
do
scp -С /home/sirius/prog.py vf140@fs$i@$IP:/$PATH
sudo systemctl restart myservice.service
done


#! /bin/bash

python simulation.py > result.txt

sed -i "s/ /;/g"  result.txt
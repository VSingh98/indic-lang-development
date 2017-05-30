#! /bin/bash

if [ $# != 1 ]; 
then
    echo "usage: ./normalize.sh [dir]"
    echo "error"
    exit 10
fi

files=($(ls $1))

for file in ${files[@]}
do
    python \
        ../indicnlp/normalize/indic_normalize.py \
        ${PWD}/$1/${file} \
        ${PWD}/$1/${file}.norm \
        hi \
        True

done

find $1 -type f ! -name "*.norm" -delete


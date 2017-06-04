ext1=$1
ext2=$2
find -type f -name '*.ext1' -print0 | while read -d $'\0' f; do mv "$f" "${f%.txt}"; done

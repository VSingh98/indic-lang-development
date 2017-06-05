if test $# -ne 1 || test ! -d $1
then
    echo pass valid directory
    exit 1
fi

dirName=$1

for file in `ls $dirName`
do
    sed -i 's/[][(){}/.,`~!@#$%^&*-+=?;:\r]/ /g' $dirName/$file

done

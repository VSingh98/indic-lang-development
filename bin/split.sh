for dir in $@
do
    if test -d $dir
    then
        cd $dir

        rm -rf pieces
        mkdir pieces

        siz=$(wc -c <*.txt)
        ratio=$((siz/5+1))

        echo dir is $dir
        echo size is $siz
        echo ratio is $ratio

        split -b $ratio *.txt ./pieces

    fi

done

cwd=$PWD
for dir in $@
do
    if test -d $dir
    then
        cd $dir
        dir=`basename $dir`
        datfile="${dir}_data.txt"
        touch $datfile

        for file in `ls`
        do
            if test $file != $datfile
            then
                tr '\n' ' ' < $file >> $datfile
                rm -f $file
            fi
        done

    fi

    cd $cwd
done

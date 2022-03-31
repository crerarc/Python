#!/bin/bash
# File to compress pdf/ps file(s) into a pdf file
# Copyright 2021 Crerar Christie
#
# Script tries to compress files and puts the smaller into a
# created folder called Z_Keep and the larger into Z_Remove.
# Note - the original file may end up being smaller than the
# compressed file.

SQUEEZE=1050000
DIR_CUR="$(pwd)"

DIR_KEEP="$DIR_CUR/Z_KEEP"
mkdir $DIR_KEEP
echo "Created $DIR_KEEP"
DIR_RMV="$DIR_CUR/Z_RMV"
mkdir $DIR_RMV
echo "Created $DIR_RMV"

for f in *.pdf
    do
    echo
    f_us=${f// /_}
    if [[ $f != $f_us ]] ;then
        mv "$f" "$DIR_CUR/$f_us"
        echo "Moved $f to $f_us"
        echo
    fi

    FILESIZE=$(stat -c%s "$f_us")
    echo "File: $f_us"
    echo "Original Size  : $FILESIZE bytes"

        if [[ $FILESIZE -gt $SQUEEZE ]] ;then
            ps2pdf -dPrinted=false -dPDFSETTINGS=/ebook $f_us 1_$f_us
            # To preserve quality of images, use the following...
            # ps2pdf -dPrinted=false -dPDFSettings=/ebook -dAutoFilterColorImages=false \
            #        -dColorImageFilter=/FlateEncode -dPDFsettings=/prepress $f_us 1_$f_us
            pid=$!
            wait $pid

            FILESIZE2=$(stat -c%s "1_$f_us")
            echo "Compressed Size: $FILESIZE2 bytes"
            if [[ $FILESIZE2 -ge $FILESIZE ]] ;then
                mv "1_$f_us" "$DIR_RMV/lrgr_$f_us"
                mv "$f_us" "$DIR_KEEP/$f_us"
                echo "No Compression -> Move to lrgr_ file"
            else
                mv "1_$f_us" "$DIR_KEEP/1_$f_us"
                mv "$f_us" "$DIR_RMV/$f_us"
                echo "Compressed -> Moved to Z_KEEP"
            fi

        else

            mv "$f_us" "$DIR_KEEP/$f_us"
            echo "-> Too small to Compress"

        fi
        
    done


#!/bin/bash
#vim /etc/ImageMagick-6/policy.xml
SRC=$1
DEST=$2
echo "Operating on $SRC"
echo "Store results in $DEST" 

#check if source file exists
if [ ! -f "./$SRC" ]; then
  echo "Cannot find source file $SRC"
  exit 1
fi

#check destination folder
if [ ! -d "./$2" ]; then
  mkdir $2
fi

pdfimages -f 3 -png $SRC "./$DEST/$SRC"

file_count=0
#crop all image in destination directory
for file in ./$DEST/*
do
    if [ -f $file ]; then
        echo "Cropping $file"
        convert $file -crop 5088x3288 ./$DEST/$file_count.png
        file_count=$((file_count+1))
    fi
done

echo "removing temporary results"
rm ./$DEST/$SRC*
echo "all set"

exit 0

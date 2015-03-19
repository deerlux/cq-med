#!/bin/sh
for item in SampleType TestName NormalValueDescription DiseaseRelated; do
    echo "select $item from test;" | sqlite3 $1 | sort -u > $item.txt
done



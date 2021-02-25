#! /usr/bin/env bash

mkdir petclinic

for i in `seq 1 10`; do
    prefix="petclinic/$(date '+%Y-%m-%d-%H-%M-%S')"

    locust -f petclinic.py \
        -H $PETCLINIC_URL --headless \
        -u 100 -r 10 -t 2m \
        --html "$prefix.html" --csv $prefix --csv-full-history
done

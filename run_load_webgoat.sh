#! /usr/bin/env bash

mkdir webgoat7

for i in `seq 1 10`; do
    prefix="webgoat7/$(date '+%Y-%m-%d-%H-%M-%S')"

    locust -f webgoat7.py \
        -H $WEBGOAT_URL --headless \
        -u 100 -r 10 -t 2m \
        --html "$prefix.html" --csv $prefix --csv-full-history
done

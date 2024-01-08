#!/bin/sh

while true
do
  kubectl top node | sed '1d' | awk 'NF > 0 { OFS=","; cmd = "date -u +%Y-%m-%d-%H:%M:%S"; cmd | getline timestamp; close(cmd); print timestamp, $1, $2, $3, $4, $5 }'
  sleep 5
done


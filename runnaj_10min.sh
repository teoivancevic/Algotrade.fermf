#!/bin/bash
time=$(date +%s)
echo $time

for i in {1..100}; do
	python3 graph.py
done

#!/bin/bash

files=$(find -type f | wc -l)
echo "Files in $(pwd) = ** $files **"

dirs=$(find -type d | wc -l )
dirs=`expr $dirs - 1`
echo "Directories in $(pwd) = ** $dirs **"
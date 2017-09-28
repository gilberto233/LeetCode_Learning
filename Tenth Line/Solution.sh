#!/bin/bash

filepath="file.txt"

gawk 'FNR == 10 {print }' $filepath

# It's about a matter in gawk using.

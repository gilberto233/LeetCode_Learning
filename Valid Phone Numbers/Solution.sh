#!/bin/bash
filepath="file.txt"

gawk '/^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/' $filepath

# This script intense to increase your acknowledge of regular expression.

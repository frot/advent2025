#!/bin/bash

sed -e 's/L\(.*\)/\1-lax/' -e 's/R\(.*\)/\1+lax/' $1 |dc -e '0sx[lx1+sx]sb[d100%d0=b]sa50' -f- -e 'lxp'

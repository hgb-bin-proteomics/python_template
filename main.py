#!/usr/bin/env python3

# SCRIPT NAME
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

# version tracking
__version = "1.0.0"
__date = "2024-03-11"

# REQUIREMENTS
# pip install pandas

###### PARAMETERS #######

param_1 = 1
param_2 = 2

#########################

"""
DESCRIPTION:
A description of the script [multiplies two integers].
USAGE:
main.py [-f1 --factor1]
        [-f2 --factor2]
required arguments:
    -f1 int, --factor1 int
        First factor of multiplication.
optional arguments:
    -f2 int, --factor2
        Second factor of multiplication.
        Default: 2
    -h, --help
        Show this help message and exit.
    --version
        Show program's version number and exit.
"""

#########################

# import packages
import argparse
import pandas as pd

####### FUNCTIONS #######

def my_product(x: int, y: int) -> int:
    return x * y

##### MAIN FUNCTION #####

def main(argv = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f1", "--factor1",
                        dest = "f1",
                        required = True,
                        help = "First factor of multiplication.",
                        type = int)
    parser.add_argument("-f2", "--factor2",
                        dest = "f2",
                        default = 2,
                        help = "Second factor of multiplication.",
                        type = int)
    args = parser.parse_args(argv)

    p = my_product(args.f1, args.f2)
    print(f"The product of {args.f1} * {args.f2} = {p}")

    return p

######## SCRIPT #########

if __name__ == "__main__":

    m = main()

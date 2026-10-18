#! /usr/bin/env python3

# ------------------------------------------------------------
# Name: Sabrina Akter
# Course: HSC 4933 - Introduction to Biocomputing
# Assignment: compare_freq_2026.py Homework
# Date: October 18, 2026
#
# Description:
# This program tests the difference between two proportions.
# It accepts both "Yes" and "y" to continue the program.
# It also checks that nobs1 <= n1 and nobs2 <= n2.
# If the inputs are invalid, the program asks for new values.
# ------------------------------------------------------------

import math

print("Test the difference between nobs1/n1 and nobs2/n2.")

choice: str = 'yes'

while choice.upper() == 'YES' or choice.upper() == 'Y':

    nobs1: int = int(input("Enter nobs1:"))
    n1: int = int(input("Enter n1:"))
    nobs2: int = int(input("Enter nobs2:"))
    n2: int = int(input("Enter n2:"))

    # Check that the observed values do not exceed the total values
    while nobs1 > n1 or nobs2 > n2:
        print("Error: nobs1 must be <= n1 and nobs2 must be <= n2.")

        nobs1 = int(input("Enter nobs1:"))
        n1 = int(input("Enter n1:"))
        nobs2 = int(input("Enter nobs2:"))
        n2 = int(input("Enter n2:"))

    p1: float = nobs1 * 1.0 / n1
    p2: float = nobs2 * 1.0 / n2
    p: float = (nobs1 + nobs2) * 1.0 / (n1 + n2)

    print(p)

    s: float = math.sqrt(p * (1 - p) * (1.0 / n1 + 1.0 / n2))

    print(s)

    if nobs1 > 30 and n1 - nobs1 > 30 and nobs2 > 30 and n2 - nobs2 > 30:
        z: float = (p1 - p2) / s
        cdf: float = (1.0 + math.erf(z / math.sqrt(2.0))) / 2.0

        if p1 > p2:
            cdf = 1 - cdf

    else:
        z: float = (abs(p1 - p2) - 0.5 / n1 - 0.5 / n2) / s

        if z < 0:
            z = 0

        print(z)

        cdf: float = (1.0 + math.erf(z / math.sqrt(2.0))) / 2.0
        cdf = 1 - cdf

        print(cdf)

    cdf = cdf * 2

    print("Z=%.3f,p-value(two-tail)=%f" % (z, cdf))

    choice = input("Continue? [Yes/No]")
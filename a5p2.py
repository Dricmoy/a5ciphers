#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2025 Dricmoy Bhattacharjee
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 5 Problem 2 Student Solution
January 2025
Author: Dricmoy Bhattacharjee
"""

from sys import flags
import numpy as np
def evalDecipherment(text1: str, text2: str) -> [float, float]:
    """
    Evaluate the key accuracy and decipherment accuracy of text2 w.r.t. text1.
    text1 is the original plaintext, and text2 is an attempted decipherment of a ciphertext created from text1.
    """
    text1 = text1.lower()
    text2 = text2.lower()

    unique_cipher_chars = set([char for char in text1 if char.isalpha()])
    total_cipher_chars = len(unique_cipher_chars)
    
    accurate_keys = 0
    accurate_set = set()
    for char1, char2 in zip(text1, text2):
        if char1.isalpha() and char2.isalpha():
            if char1 == char2 and char1 not in accurate_set:
                accurate_keys += 1
                accurate_set.add(char1)
                
    key_accuracy = accurate_keys / total_cipher_chars if total_cipher_chars != 0 else 0

    correct_decipherment = 0
    total_decipherable_chars = 0

    for char1, char2 in zip(text1, text2):
        if char1.isalpha():  # Only consider alphabetical characters
            total_decipherable_chars += 1
            if char1 == char2:
                correct_decipherment += 1

    # Decipherment accuracy is the ratio of correct decipherments to total decipherable characters
    decipherment_accuracy = correct_decipherment / total_decipherable_chars if total_decipherable_chars != 0 else 0

    return [key_accuracy, decipherment_accuracy]

def test():
    "Run tests"
    np.testing.assert_array_almost_equal(evalDecipherment("this is an example", "tsih ih an ezample") , [0.7272727272727273, 0.7333333333333333])
    np.testing.assert_almost_equal(evalDecipherment("the most beautiful course is 331!", "tpq munt bqautiful cuurnq in 331!") , [0.7142857142857143, 0.625])
if __name__ == '__main__' and not flags.interactive:
    test()

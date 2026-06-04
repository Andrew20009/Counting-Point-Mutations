Counting Point Mutations
OVERVIEW
This program reads two string (s, t) of DNA sequence from a text file and counts the mismatches of its sequences.
It is a solution to the "Counting Point Mutations" Rosalind problem (ID: HAMM). The tool is simple, efficient, and ideal for practicing file handling and string processing in Python.

FEATURES

Reads DNA strings from a file (rosalind_hamm.txt)
Automatically converts input to uppercase
Creates count for mismatches (Point Mutations)
Checks the mismatches between two strings
Prints the number of mismatches
Fast and memory-efficient — works well with long sequences
Clean, well-commented code with proper functions and docstrings

IMPORTANT NOTE

!!!Please put the Input txt with name rosalind_hamm.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!


EXAMPLE
Input (rosalind_hamm.txt):  GAGCCTACTAACGGGAT
                            ATCGTAATGACGGCCT
Output:7

HOW IT WORKS

The program reads the DNA strings from the file.
It cleans the input (removes whitespace and converts to uppercase).
It counts all the mismatches between two strings
Finally, it prints the number.


TECHNOLOGIES USED

Python
File txt
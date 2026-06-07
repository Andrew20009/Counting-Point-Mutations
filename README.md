# Counting Point Mutations

## OVERVIEW
This program reads two strings **(s, t)** of DNA sequence from a text file and counts the mismatches of its sequences.
It is a solution to the **"Counting Point Mutations"** Rosalind problem **(ID: HAMM)**. The tool is simple, efficient, and ideal for practicing file handling and string processing in Python.

---

## FEATURES
- Reads DNA strings from a file <u>(rosalind_hamm.txt)</u>
- Automatically converts input to **uppercase**
- Creates count for <u>mismatches (Point Mutations)</u>
- Checks the mismatches between **two strings**
- Prints the number of mismatches
- Fast and memory-efficient — works well with long sequences
- Clean, well-commented code with proper functions and docstrings

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the Input txt with name rosalind_hamm.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!**</u>

---

## EXAMPLE
**Input** (rosalind_hamm.txt):
```
GAGCCTACTAACGGGAT
ATCGTAATGACGGCCT
```
**Output:**
```
7
```

---

## HOW IT WORKS
1. The program reads the <u>two DNA strings</u> from the file
2. It cleans the input (removes whitespace and converts to **uppercase**)
3. It counts all the <u>mismatches between two strings</u>
4. Finally, it prints the number

---

## TECHNOLOGIES USED
- **Python**
- **File I/O** (txt)

def hamming_distance(s, t): # Calculates the number of characters where two DNA strings differ
    count = 0 # Counter for mismatches in strings

    for a, b in zip(s, t): # Compare character pairs by position
        if a != b: # If characters differ, increase the counter
            count += 1

    return count # Return the total number of mismatches in two strings


file_path = "rosalind_hamm.txt" # Path to the input file
lines = [] # List to store lines from the file

with open(file_path) as f: # Open the input file for reading
    for line in f:
        cleaned = line.strip().upper() # Remove whitespace and convert to uppercase
        lines.append(cleaned)


s = lines[0] # First DNA string (s)
t = lines[1] # Second DNA string (t)


try:
    result = hamming_distance(s, t) # Compute the Hamming distance
    print(result) # Print the result

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found!")
    print("Put file rosalind_hamm.txt in the same folder as code.")
except Exception as e:
    print(f"Error Occurred: {e}")

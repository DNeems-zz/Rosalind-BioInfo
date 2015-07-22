""""
Complementing a Strand of DNA 

Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset:
AAAACCCGGT

Sample Output:
ACCGGGTTTT
"""

import sys
from RosSupFunc import FastaRead
from RosSupFunc import FastaWrite
from string import maketrans

# Define a main() function that prints a little greeting.
def main():
  [name,value]=FastaRead(sys.argv[1])
  Results=list()
  for entries in value:
    Results.append(entries[::-1].upper().translate(maketrans('ACGT', 'TGCA')))
  FastaWrite(name,Results,'Ex3_Output.txt')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

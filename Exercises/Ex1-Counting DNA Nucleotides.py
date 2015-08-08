""""
Counting DNA Nucleotides

Problem

A string is simply an ordered collection of symbols selected from some 
alphabet and formed into a word; the length of a string is the number 
of symbols that it contains.  An example of a length 21 DNA string 
(whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is
"ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:
20 12 17 21
"""

import sys
from SupportMod.RosSup_Func import FastaRead
from SupportMod.RosSup_Func import FastaWrite

# Define a main() function that prints a little greeting.
def main():
  [name,value]=FastaRead(sys.argv[1])
  DNABases=['a','c','g','t'];
  Results=list()
  for entries in value:
    Results.append([entries.lower().count(nt) for nt in DNABases])
  FastaWrite(name,Results,'Ex1_Output.txt')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

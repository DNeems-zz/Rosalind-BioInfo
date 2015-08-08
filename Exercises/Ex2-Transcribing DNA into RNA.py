""""
Transcribing DNA into RNA

Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u 
is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset:
GATGGAACTTGACTACGTAAATT

Sample Output:
GAUGGAACUUGACUACGUAAAUU
"""

import sys
from SupportMod.RosSup_Func import FastaRead
from SupportMod.RosSup_Func import FastaWrite

# Define a main() function that prints a little greeting.
def main():
  [name,value]=FastaRead(sys.argv[1])
  Results=list()
  for entries in value:
    Results.append(entries.upper().replace('T','U'))
  FastaWrite(name,Results,'Ex2_Output.txt')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

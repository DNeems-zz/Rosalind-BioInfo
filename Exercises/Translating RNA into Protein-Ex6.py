""""
Translating RNA into Protein
Problem

The 20 commonly occurring amino acids are abbreviated by 
using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). 
Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string
 will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into 
the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""

import sys
from SupportMod.RosSup_Func import FastaRead
from SupportMod.RosSup_Func import FastaWrite
from SupportMod.RosSup_Dict import DNA_AA_Dict
# Define a main() function that prints a little greeting.
def main():
  [name,value]=FastaRead(sys.argv[1])
  for Entries in zip(value,name):
  	protein=list()
  	for pos in range(0,len(Entries[0]),3):
  		protein.append(DNA_AA_Dict[Entries[0][pos:pos+3].lower().replace('u','t')])
  	FastaWrite(Entries[1],protein,'Ex6_Output.txt',False)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

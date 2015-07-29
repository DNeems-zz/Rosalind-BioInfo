# -*- coding: utf-8 -*-

"""" 
RNA Splicing

Problem

After identifying the exons and introns of an RNA string, we only need to
delete the introns and concatenate the exons to form a new string ready for
translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons
of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset:
>Rosalind_10 
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACA
TGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG 
>Rosalind_12 
ATCGGTCGAA 
>Rosalind_15
ATCGGTCGAGCGTGT 

Sample Output:
MVYIADKQHVASREAYGHMFKVCA
"""


import sys
from SupportMod.RosSup_Func import FastaRead
from SupportMod.RosSup_Func import FastaWrite
from SupportMod.RosSup_Func import Translate
from SupportMod.keyboard import keyboard
# Define a main() function that prints a little greeting.
def main():
  [name,value]=FastaRead(sys.argv[1])
  BaseSeq=value[0]
  for N,V in zip(name[1:],value[1:]):
    BaseSeq=BaseSeq[:BaseSeq.find(V)]+BaseSeq[BaseSeq.find(V)+len(V):]
  FastaWrite(name[0],Translate(BaseSeq),'Ex13_Output.txt')
 

    #SharedString(V,V)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

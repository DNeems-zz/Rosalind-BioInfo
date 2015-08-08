# -*- coding: utf-8 -*-

"""" 
Open Reading Frames

Problem

Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset

>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
Sample Output

MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""


import sys
from SupportMod.RosSup_Func import FastaRead
from SupportMod.RosSup_Func import FastaWrite
from SupportMod.RosSup_Func import Translate
from SupportMod.RosSup_Func import ReverseComp

from SupportMod.keyboard import keyboard
# Define a main() function that prints a little greeting.
def main():
  [name,value]=FastaRead(sys.argv[1])
  for V,N in zip(value,name):
    ORFs=[]
    for pos in range(0,len(V)):
      if V[pos:pos+3].lower()=='atg':
        ORFs.append(Translate(V[pos:]).split(' ')[0])
    V=ReverseComp(V)
    for pos in range(0,len(V)):
      if V[pos:pos+3].lower()=='atg':
        ORFs.append(Translate(V[pos:]).split(' ')[0])
   
    ORFs=list(set([vORF for vORF in ORFs if vORF[-1] != '*']))
    FastaWrite(name[0],ORFs,'Ex14_Output.txt',True,True)
 

    #SharedString(V,V)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

# -*- coding: utf-8 -*-

""""Finding a Spliced Motif

Problem

A subsequence of a string is a collection of symbols contained in order
(though not necessarily contiguously) in the string (e.g., ACG is a
subsequence of TATGCTAAGATC). The indices of a subsequence are the positions
in the string at which the symbols of the subsequence appear; thus, the
indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

As a substring can have multiple locations, a subsequence can have multiple
collections of indices, and the same index can be reused in more than one
appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT
in 8 different ways.

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a
subsequence of s. If multiple solutions exist, you may return any one.

Sample Dataset
>Rosalind_14 ACGTACGTGACG 
>Rosalind_18 GTA 

Sample Output
3 8 10 
"""    
import sys  
from SupportMod.RosSup_Func import FastaRead

def main():
  [name,value]=FastaRead(sys.argv[1])
  String=value[0]
  Sub_String=value[1]
  MatchPos=[String.index(Sub_String[0],1)]
  for char in Sub_String[1:]:
    MatchPos.append(String[MatchPos[-1]:].index(char,1)+MatchPos[-1])
  with open('Ex27_Output.txt', 'a') as f:
    f.write(' '.join([str(el+1) for el in MatchPos])+'\n')


 # This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()

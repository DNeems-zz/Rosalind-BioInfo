# -*- coding: utf-8 -*-

""""Transitions and Transversions

Problem

For DNA strings s1 and s2 having the same length, their
transition/transversion ratio R(s1,s2) is the ratio of the total number of
transitions to the total number of transversions, where symbol substitutions
are inferred from mismatched corresponding symbols as when calculating Hamming
distance (see “Counting Point Mutations”).

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).

Sample Dataset

>Rosalind_0209 
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT 

>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT 

Sample Output
1.21428571429 
"""   
import sys  
from SupportMod.RosSup_Func import FastaRead

def main():
  [name,value]=FastaRead(sys.argv[1])
  Transversion=0
  Transitions=0
  for s1,s2 in zip(value[0],value[1]):
    if s1 != s2:
      if s1 is 'A' or s1 is 'G':
        if s2 is 'C' or s2 is 'T':
          Transversion+=1
        else:
          Transitions+=1
      else:
        if s2 is 'A' or s2 is 'G':
          Transversion+=1
        else:
          Transitions+=1
  with open('Ex26_Output.txt', 'a') as f:
    f.write(str( Transitions/(Transversion*1.0))+'\n')

  



  
 # This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()

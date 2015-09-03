# -*- coding: utf-8 -*-

""""Genome Assembly as Shortest Superstring

Problem

For a collection of strings, a larger string containing every one of the
smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a
collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA
format (which represent reads deriving from the same strand of a single linear
chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a
unique way to reconstruct the entire chromosome from these reads by gluing
together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus
corresponding to a reconstructed chromosome).

Sample Dataset

>Rosalind_56 ATTAGACCTG 
>Rosalind_57 CCTGCCGGAA 
>Rosalind_58 AGACCTGCCG
>Rosalind_59 GCCGGAATAC 

Sample Output
ATTAGACCTGCCGGAATAC """     
import sys   
from SupportMod.RosSup_Func import FastaRead
import math
def main():
  [name,value]=FastaRead(sys.argv[1])
  V=value.pop(0)
  Superstring=V
  V=[V]
  name.pop(0)
  z=0
  while len(value)>0:
    seq = value[0]
    n=name[0]
    MidPoint=int(math.floor(len(seq)/2.0))
    #print Superstring
    if seq in Superstring:  
      V.append(value.pop(0))
      name.pop(0)
    elif seq[MidPoint:] in Superstring:
      Superstring=seq+Superstring[Superstring.index(seq[MidPoint:])+len(seq[MidPoint:]):]
    elif seq[:MidPoint] in Superstring:
      Superstring=Superstring[:Superstring.index(seq[:MidPoint])]+seq
      V.append(value.pop(0))
      name.pop(0)
    else:
      value.append(value.pop(0))
      name.append(name.pop(0))
  for v in V:
    print v in Superstring
  with open('Ex28_Output.txt', 'a') as f:
    f.write(Superstring+'\n')

 # This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()

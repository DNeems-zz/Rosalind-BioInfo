# -*- coding: utf-8 -*-

""""  Consensus and Profile

Problem

A matrix is a rectangular table of values divided into rows and columns. An
m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to
indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n.
Their profile matrix is a 4×n matrix P in which P1,j represents the number of
times that 'A' occurs in the jth position of one of the strings, P2,j
represents the number of times that C occurs in the jth position, and so on
(see below).

A consensus string c is a string of length n formed from our collection by
taking the most common symbol at each position; the jth symbol of c therefore
corresponds to the symbol having the maximum value in the j-th column of the
profile matrix. Of course, there may be more than one most common symbol,
leading to multiple possible consensus strings.

DNA Strings
A T C C A G C T
G G G C A A C T
A T G G A T C T
 A A G C A A C C
T T G G A A C T
A T G C C A T T
_______________
A T G G C A C T

Profile
A 5 1 0 0 5 5 0 0
C 0 0 1 4 2 0 6 1
G 1 1 6 3 0 1 0 0
T 1 5 0 0 0 1 1 6
__________________
  A T G C A A C T Consensus   
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)

Sample Dataset:
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT


Sample Output:

ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""


import sys
from SupportMod.RosSup_Func import FastaRead
import numpy as np

from SupportMod.keyboard import keyboard
# Define a main() function that prints a little greeting.
def main():
  [name,value]=FastaRead(sys.argv[1])
  Freq_Dict={'A': [0 for unused in range(len(value[0]))],
  'C': [0 for unused in range(len(value[0]))],
  'G': [0 for unused in range(len(value[0]))],
  'T': [0 for unused in range(len(value[0]))]}
  for V,N in zip(value,name):
    V=V.upper()
    for pos,char in enumerate(V):
       Freq_Dict[char][pos]+=1
  Consensus=''
  Bases=['A','C','G','T']
  for pos in range(len(value[0])):
    Max=np.argmax([Freq_Dict['A'][pos],Freq_Dict['C'][pos],Freq_Dict['G'][pos],Freq_Dict['T'][pos]])
    Consensus+=Bases[Max]
  with open('Ex15_Output.txt', 'a') as f:
    f.write(Consensus +'\n')
    f.write('A: ' +' '.join([str(freq) for freq in Freq_Dict['A']])+'\n')
    f.write('C: ' +' '.join([str(freq) for freq in Freq_Dict['C']])+'\n')
    f.write('G: ' +' '.join([str(freq) for freq in Freq_Dict['G']])+'\n')
    f.write('T: ' +' '.join([str(freq) for freq in Freq_Dict['T']])+'\n')

 # This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()

""""
Counting Point Mutations

Problem



Given two strings s and t of equal length, the Hamming distance between s and t,
 denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output:
7
"""

import sys
from RosSupFunc import FastaRead
from RosSupFunc import FastaWrite

# Define a main() function that prints a little greeting.
def main():
  [name,value]=FastaRead(sys.argv[1])
  HammingDist=0
  for Orig,New in zip(value[0],value[1]):
    if Orig!=New:
      HammingDist+=1
  FastaWrite([name[0]],[HammingDist],'Ex4_Output.txt')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

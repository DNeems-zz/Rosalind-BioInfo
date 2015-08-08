# -*- coding: utf-8 -*-

"""" Enumerating Gene Orders

Problem

A permutation of length n is an ordering of the positive integers {1,2,...,n}. For
example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all
such permutations (in any order). 

Sample Dataset:
3

Sample Output:
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

"""

import sys
import itertools
# Define a main() function that prints a little greeting.

def main():
  n= (open(sys.argv[1]).readline().strip().split(' '))
  for value in n:
   N=int(value)
   Perumtaions=list()
   for perm in itertools.permutations(range(1,N+1)):
    Perumtaions.append(' '.join([str(p) for p in perm]))
   with open('Ex11_Output.txt', 'a') as f:
    f.write('Seed Number (n): '+ str(N) +'\n')
    f.write('Number of Perumtaions: '+ str(len(Perumtaions)) +'\n')
    for P in Perumtaions:
      f.write(P+'\n')
  # f.write('Offspring Rate (k): '+k +'\n')
  # f.write('Mature Rabbits: '+str(Mature_Num) +'\n')
  # f.write('New Born Rabbits: '+str(Immature_Num) +'\n')
  # f.write('Total Rabbits: '+str(Mature_Num+Immature_Num) +'\n')   
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

# -*- coding: utf-8 -*-

"""" Enumerating Oriented Gene Orderings 

Problem

A signed permutation of length n is some ordering of the positive integers
{1,2,…,n} in which each integer is then provided with either a positive or
negative sign (for the sake of simplicity, we omit the positive sign). For
example, π=(5,−3,−2,1,4) is a signed permutation of length 5.

Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a
list of all such permutations (you may list the signed permutations in any
order).

Sample Dataset:
2

Sample Output:
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1
""" 
import sys
from SupportMod.RosSup_Func import Cross
import itertools
# Define a main() function that prints a little greeting.
def main():
  n= (open(sys.argv[1]).readline().strip().split(' '))
  Num = int(n[0])
  Enumerations=list()
  for perm in itertools.product('01',repeat=Num):
    Modifier=list()
    for p in perm:
      if int(p)==0:
        Modifier.append(1)
      else:
        Modifier.append(-1)
    Input_Set=[n*m for n,m in zip(range(1,Num+1),Modifier)]
    for perm in itertools.permutations(Input_Set):
      Enumerations.append(perm)
  with open('Ex23_Output.txt', 'a') as f:
    f.write(str(len(Enumerations))+'\n')  
    for E in Enumerations:
      f.write(' '.join([str(i) for i in E])+'\n')
  
  #  
  #  for GT_pair,Num in zip(GT,Freq):
  #    f.write(GT_pair[0]+'-'+GT_pair[1]+':'+' '+ str(Num) +'\n')
  #  f.write('Expected Number of  Dominant Phenotype: '+str(Expected_Domintant*2)+'\n')

  
  #[n,k]= (open(sys.argv[1]).readline().strip().split(' '))
 

  
 # This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()

# -*- coding: utf-8 -*-

""""Enumerating k-mers Lexicographically

Problem

Assume that an alphabet A has a predetermined order; that is, we write the
alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the
English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t
in the lexicographic order (and write s<Lext) if the first symbol s[j] that
doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a
positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered
lexicographically.

Sample Dataset

T A G C 
2 

Sample Output

TT TA TG TC AT AA AG AC GT GA GG GC CT CA CG CC """  
import sys 
import operator
import itertools


def main():
  f=open(sys.argv[1])
  char=f.readline().strip().split()
  n=int(f.readline())
  Seq=list()
  SORT_ORDER={}
  for Pos in range(len(char)):
    SORT_ORDER[char[Pos]]=Pos

  for P in itertools.product(char,repeat=n):
     Seq.append(''.join([el for el in P]))
  Ordered_List=sorted(Seq,key=lambda val: SORT_ORDER[val[0]])
  with open('Ex25_Output.txt', 'a') as f:
    for entry in Ordered_List:
      f.write(entry+'\n')



  
 # This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()

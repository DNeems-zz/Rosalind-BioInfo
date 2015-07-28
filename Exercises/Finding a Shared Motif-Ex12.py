# -*- coding: utf-8 -*-

""""
Finding a Shared Motif

Problem

A common substring of a collection of strings is a substring of every member
of the collection. We say that a common substring is a longest common
substring if there does not exist a longer common substring. For example, "CG"
is a common substring of "ACGTACGT" and "AACCGGTATA", but it is not as long as
possible; in this case, "GTA" is a longest common substring of "ACGTACGT" and
"AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple
example, "AA" and "CC" are both longest common substrings of "AACC" and
"CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in
FASTA format.

Return: A longest common substring of the collection. (If multiple solutions
exist, you may return any single solution.)

Sample Dataset:
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output:
AC

"""

import sys
from SupportMod.RosSup_Func import FastaRead
from SupportMod.RosSup_Func import FastaWrite
# Define a main() function that prints a little greeting.
def SharedString(str1,str2,SharedLen=2):
   CommonSeq=['']
   for StartPos in range(len(str1)):
    Found_End=False 
    for EndPos in range(StartPos+2,len(str1)+1):
      if str1[StartPos:EndPos] in str2:        
        if EndPos==len(str1):
         Found_End=True
         EndPos+=1
        else:
         Found_End=False
      else:
        Found_End=True
      if Found_End and str1[StartPos:EndPos-1] in str2:
        if not any([str1[StartPos:EndPos-1] in lcs for lcs in CommonSeq]):
          CommonSeq.append(str1[StartPos:EndPos-1])
   Max_CommonSeq=[]
   MaxLen=max([len(seq1) for seq1 in CommonSeq])
   [Max_CommonSeq.append(seq) for seq in CommonSeq if len(seq)>=MaxLen]
   return Max_CommonSeq,CommonSeq[1:]

def main():
  [name,value]=FastaRead(sys.argv[1])
  LCS=SharedString(value[0],value[1])
  LCS=LCS[1]
  for V in value[2:]:
    New_LCS=[]
    for lcs in LCS:
      A=SharedString(lcs,V)
      [New_LCS.append(a) for a in A[1]]
    LCS=list(set(New_LCS[:]))
  ML=max([len(lcs) for lcs in LCS])
  Max_LCS=[]
  [Max_LCS.append(lcs) for lcs in LCS if len(lcs)==ML]
  with open('Ex12_Output.txt', 'a') as f:
   f.write('LCS:'+'\n')
   for lcs in Max_LCS:
    f.write(lcs+'\n')


    #SharedString(V,V)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

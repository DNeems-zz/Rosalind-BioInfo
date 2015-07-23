"""" Locating Restriction Sites

Problem


Figure 2. Palindromic recognition site A DNA string is a reverse palindrome if
it is equal to its reverse complement. For instance, GCATGC is a reverse
palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having
length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24 
TCAATGCATGCGGGTCTATATGCAT 

Sample Output

4 6 
5 4
6 6 
7 4
17 4
18 4
20 6
21 4 """

import sys
from SupportMod.RosSup_Func import FastaRead
from SupportMod.RosSup_Func import FastaWrite
from SupportMod.RosSup_Func import ReverseComp
# Define a main() function that prints a little greeting.

def PalindromeSeq(Seq):
	return Seq==ReverseComp(Seq)


def main():
  [name,value]=FastaRead(sys.argv[1])
  with open('Ex10_Output.txt', 'a') as f:
    for Entries in zip(value,name):
  	  f.write(Entries[1]+'\n')
  	  DNA=Entries[0]
  	  for sPos in range(len(DNA)):
  	  	End=min(sPos+16,len(DNA)+1)
  		for ePos in range(sPos+4,End):
  			if len(DNA[sPos:ePos])>3:
  				if PalindromeSeq(DNA[sPos:ePos]):
  					f.write(str(sPos+1)+' ')
  					f.write(str(len(DNA[sPos:ePos]))+'\n')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

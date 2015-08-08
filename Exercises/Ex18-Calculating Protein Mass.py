# -*- coding: utf-8 -*-

""""  Calculating Protein Mass

In a weighted alphabet, every symbol is assigned a positive real number called
a weight. A string formed from a weighted alphabet is called a weighted
string, and its weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid
alphabet is the monoisotopic mass of the corresponding amino acid.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

Sample Dataset:
SKADYEK

Sample Output:
821.392
"""


import sys
from SupportMod.RosSup_Func import FastaRead
from SupportMod.RosSup_Dict import AA_Weight
# Define a main() function that prints a little greeting.
def main():
  [name,value]=FastaRead(sys.argv[1])
  Mass=0
  for V in value:
    for aa in V:
      Mass+=AA_Weight[aa]
    with open('Ex18_Output.txt', 'a') as f:
      f.write('Mass: '+str(Mass)+'\n')


  
 # This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()

# -*- coding: utf-8 -*-

""""  Finding a Protein Motif  Problem

To allow for the presence of its varying forms, a protein motif is represented
by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino
acid except X." For example, the N-glycosylation motif is written as
N{P}[ST]{P}.

You can see the complete description and features of a particular protein by
its access ID "uniprot_id" in the UniProt database, by inserting the ID number
into

http://www.uniprot.org/uniprot/uniprot_id Alternatively, you can obtain a
protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta For example, the data for
protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its
given access ID followed by a list of locations in the protein string where
the motif can be found.

Sample Dataset:
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output:
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""


import sys
from SupportMod.RosSup_Func import FastaRead
from SupportMod.RosSup_Func import FastaWrite

import urllib2
# Define a main() function that prints a little greeting.
def main():
  F=open(sys.argv[1])
  name=[]
  value=[]
  Input_Name=[]
  for line in F:
    [N,V]=FastaRead('http://www.uniprot.org/uniprot/'+line.strip()+'.fasta',fromFile=False,fromUrl=True)
    Input_Name.append(line.strip())
    name.append(N[0])
    value.append(V[0])
  for N,V in zip(Input_Name,value):
    Motiff_Pos=[]
    for pos in range(len(V)-3):
      if V[pos]=='N' and V[pos+1]!='P' and any([V[pos+2]=='S',V[pos+2]=='T']) and V[pos+3]!='P':
        Motiff_Pos.append(pos+1)
        print V[pos:pos+4]
    if len(Motiff_Pos)!=0:
      FastaWrite(N,Motiff_Pos,'Ex16_Output.txt')
 
  #[name,value]=FastaRead(sys.argv[1])

  
 # This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()

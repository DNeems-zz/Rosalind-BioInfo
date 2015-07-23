import sys
def FastaRead(filename):
  F=open(filename)
  Names=list()
  Values=list()
  for line in F:
  	if line[0]=='>':
  		Names.append(line[1:].strip())
  		Values.append('')
  	else:
  		Values[-1]=Values[-1]+line.strip()
  return [Names,Values]

def FastaWrite(Names,Values,filename='Default.txt',OutputSpace=True):
	with open(filename, 'a') as f:
		if type(Names)!=list:
			Names=[Names]
		if type(Values)==int or type(Values)==float:
			Values=[Values]
		elif type(Values[0])!=list:
			Values=[Values]

		for n,v in zip(Names,Values):
		  f.write('>'+n+'\n')
		  if type(v)==str:
				f.write(v+'\n')
		  elif type(v)==list:
		  	if OutputSpace:
				f.write(' '.join([str(val) for val in v])+'\n')
			else:
				f.write(''.join([str(val) for val in v])+'\n')				
		  elif type(v)==int or type(v)==float:
				f.write(str(v)+'\n')
		f.close()

def Count(DNA):
  DNABases=['a','c','g','t'];
  return [DNA.lower().count(nt) for nt in DNABases]

def Transcribe(DNA):
	return DNA.upper().replace('T','U')

def ReverseComp(DNA):
	from string import maketrans
	return DNA[::-1].upper().translate(maketrans('ACGT', 'TGCA'))

def Cross(*args):
	import itertools
	CrossPairs=list()
	for Inp in args:
		Alleles=list(set([a.lower()for a in Inp]))
		AllelePair=list()
		for A in Alleles:
			AllelePair.append('')
			for I in Inp:
				if I.lower() == A:
					AllelePair[-1]=AllelePair[-1]+I
		CrossPairs.append(list())
		for i in itertools.product(*AllelePair):
			CrossPairs[-1].append(''.join(i))
	Genotypes=list()
	for i in itertools.product(*CrossPairs):
		Genotypes.append(''.join(sorted(sorted(''.join(i)), key=str.lower)))
	uGenotypes=list(set(Genotypes))
	GenoType_Feq=list()
	for uG in uGenotypes:
		GenoType_Feq.append(tuple([uG,Genotypes.count(uG)]))
	return Genotypes,GenoType_Feq
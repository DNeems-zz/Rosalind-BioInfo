# -*- coding: utf-8 -*-

"""" Mortal Fibonacci Rabbits

Problem


Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they
die after three months. Recall the definition of the Fibonacci numbers from
“Rabbits and Recurrence Relations”, which followed the recurrence relation
Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one
month and produces a single pair of offspring (one male, one female) each
subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic
programming solution in the case that all rabbits die out after a fixed number
of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live
for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.

Sample Dataset:
6 3 

Sample Output:
4

""" 
import sys 

# Define a main() function that prints a little greeting.
def main():
  [n,k]= (open(sys.argv[1]).readline().strip().split(' '))
  month=int(n)
  lifespan=int(k)
  maturation_time=1
  Initial_Rabbits=1
  Num_Rabbits=list()
  [Num_Rabbits.append(0) for t in range(month)]
  Num_Rabbits[1]=Initial_Rabbits
  for t in range(1,month-1):
    New_Rabbits=sum(Num_Rabbits[1:lifespan])
    for pos in range(len(Num_Rabbits)-2,-1,-1):
      Num_Rabbits[pos+1]=Num_Rabbits[pos]
    Num_Rabbits[0]=New_Rabbits
  print Num_Rabbits
  with open('Ex21_Output.txt', 'a') as f:
    f.write('Month of Trial (n): '+ str(n) +'\n')
    f.write('Lifespan (k): '+ str(k) +'\n')
    f.write('Rabbits at end of Trial:' +str(sum(Num_Rabbits[:lifespan])))



  
 # This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()

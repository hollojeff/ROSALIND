#!/usr/bin/python

dna = input()

dna = dna.replace('A', 'x').replace('T', 'A').replace('x', 'T')
dna = dna.replace('C', 'x').replace('G', 'C').replace('x', 'G')

print(dna[::-1])

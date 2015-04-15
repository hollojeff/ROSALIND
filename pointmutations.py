#!/usr/bin/python

strand1 = input()
strand2 = input()
hamming = 0
i = 0
while i<len(strand1):
	if strand1[i] != strand2[i]:
		hamming += 1
	i +=1

print(hamming)
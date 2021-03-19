#! /usr/bin/env python3

# set the name of DNA sequence file
filename = 'dna.txt'

#open the input file
infile = open(filename, 'r')

# read the file
dna_sequence = infile.read()
dna_sequence = dna_sequence.rstrip()
#print(dna_sequence)

# close the file
infile.close()
#print(dna_sequence)

# print DNA sequence length
seqlen = len(dna_sequence)
print( "Sequence length: " + str(seqlen))

# print count of A's in sequence
numA = dna_sequence.count('A')
numC = dna_sequence.count('C')
numG = dna_sequence.count('G')
numT = dna_sequence.count('T')

# print The number of A's in file is
print ("Freq of A:", round(numA/seqlen, 3))
print ("Freq of C:", round(numC/seqlen, 3)) 
print ("Freq of G:", round(numG/seqlen, 3)) 
print ("Freq of T:", round(numT/seqlen, 3)) 
print ("Freq of G+C:", round((numG+numC)/seqlen, 3))

Freq_A = round(numA/seqlen, 3)
Freq_C = round(numC/seqlen, 3)
Freq_G = round(numG/seqlen, 3)
Freq_T = round(numT/seqlen, 3)

print(bool(1==(Freq_A + Freq_C + Freq_G + Freq_T)))

# save script as my first output
# outfile = open('my_first_output.txt', 'w')
# outfile.write('DNA sequence' + dna_sequence)
# outfile.write('Sequence length'+ str(seqlen) + 'nt')
# outfile.write("Number of A's:"+ str(numA))
# outfile.close()
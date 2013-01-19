'''
Created on Jan 19, 2013
Converts a text file containing a list of primes for use with factorit
@author: jbao
'''

import os,sys

def txtconvert(infile,outfile):
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    readpath = os.path.join(dirname, infile)
    writepath = os.path.join(dirname, outfile)
    
    f = open(readpath, 'r')
    g = open(writepath, 'w')

    primetext=f.read()
    primelist=primetext.split()
    
    writeprimes(primelist,g)
        
    f.close()
    g.close()

# writes a list of primes to a file where each prime is separated by a linebreak
def writeprimes(primelist,openfile):
    # if list is ordered and every second number is a prime
    if primelist[0]=='1' and primelist[2]=='2':
        parameter = -1
        for prime in primelist:
            if parameter == 1:
                openfile.write(prime+'\n')
            parameter = parameter*(-1)
    # if all the numbers are prime
    else:
        for prime in primelist:
            openfile.write(prime+'\n')
        

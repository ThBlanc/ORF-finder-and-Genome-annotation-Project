
def getStandardCode():
"""
This function gives the standard genetic code in the form of a dictionary. Author : Thomas Blanc
Args : None
Returns : The function returns a dictionary containing the amino acids coded by each codons (codons are used as keys.)
"""

    table={}
    base1="TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG"
    base2="TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG"
    base3="TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG"
    AAs="FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"

    for i in range(0,len(AAs)):
        codon=base1[i]+base2[i]+base3[i]
        aa=AAs[i]
        table[codon]=aa
    return table

def getGeneticCode(transl_table=4):
"""Returns a dictionary with the coding table corresponding to the number"""
    table={}

    if transl_table==4:
        base1="TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG"
        base2="TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG"
        base3="TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG"
        AAs="FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"

    for i in range(0,len(AAs)):
        codon=base1[i]+base2[i]+base3[i]
        aa=AAs[i]
        table[codon]=aa
    return table

def isDNA(seq):
    flag=""
    for nuc in seq:
        if nuc in ["A","T","G","C","a","t","g","c"]:
            flag=True
        else:
            flag=False
            return flag
    return flag

def oneWord(seq,start,wlen):
    w=seq[start:start+wlen]
    return w

def countWord(seq,word):
    cpt=0
    wlen=len(word)
    for i in range (len(seq)):
        v=oneWord(seq,i,wlen)
        if v==word:
            cpt=cpt+1
    return cpt

def isCodonStart (seq,pos):
    w=oneWord(seq,pos,3)
    if w == "ATG" or w =="atg":
        return True
    else:
        return False

def isCodonStop (seq,pos):
    w=oneWord(seq,pos,3)
    if w in ["TAA","taa","TAG","tag","TGA","tga"]:
        return True
    else:
        return False

def isGene(seq):
    i=0
    ww=False
    while i<len(seq):
        w=isCodonStart(seq,i)
        if w==True:
            ww=w
        x=isCodonStop(seq,i)
        if ww==True and x==True:
            return True
        i=i+3
    return False


def isGene3(seq):
    frame=[]
    for i in range (len(seq)):
        w=isCodonStart(seq,i)
        if w==True:
            frame.append(i%3)
            for j in range (i,len(seq)):
                x=isCodonStop(seq,j)
                if x==True:
                    if i%3==frame[]:
                        return
    return

seq='TGATGTTCCATTACCAGTACAACAAACTATGATTCCATTACCAGTACA'
flag = isGene3(seq) # True
print flag




#Functions used to invert the dna strand.
def brincomp(seq):
    comp = ""
    for i in range(len(seq)):
        if seq[i] == "A":
            comp = comp + "T"
        if seq[i] == "C":
            comp = comp + "G"
        if seq[i] == "G":
            comp = comp + "C"
        if seq[i] == "T":
            comp = comp + "A"
    return comp


def invert(seq):
    comp = brincomp (seq)
    print comp
    revers=comp[::-1]
    #revers = ""
    """
    for i in range(len(seq)):
        if i != 0 :
            revers = revers + comp[-i]
        if i == 0 :
    """
    print revers

    #end of reverse Functions.
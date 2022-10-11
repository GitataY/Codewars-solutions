**
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
**

#My solution 

def DNA_strand(dna):
    output = ''
    for str in dna:
        if str == 'A':
            output += 'T' 
        elif str == 'T':
            output += 'A'
        if str == 'C':
            output += 'G'
        elif str == 'G':
            output += 'C'
    return output

# function
def dna_complement(dna_seq):
    # Judge if dna_seq is valid
    dna_list = ['A', 'T', 'C', 'G', 'a', 't', 'c', 'g']
    if dna_seq == '':
        return None
    for x in dna_seq:
        if x not in dna_list:
            return None
    
    # Complement dna_seq
    dna_complement_result = ''
    dna_complement_dict = {'A': 'T', 'a': 'T', 'T': 'A', 't': 'A',
                           'C': 'G', 'c': 'G', 'G': 'C', 'g': 'C'}
    for x in dna_seq:
        dna_complement_result += dna_complement_dict[x]
    return dna_complement_result


# main
print('Input string 1: ATCGatcg')
s1 = dna_complement('ATCGatcg')
print('Output string 1: {}'.format(s1))
print('Input string 2: ABCD')
s2 = dna_complement('ABCD')
print('Output string 2: {}'.format(s2))

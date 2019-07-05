'''
The mirror
For wiring settings: http://users.telenet.be/d.rijmenants/en/enigmatech.htm#reflector
Jakob Mckinney
25/01/2019
'''

CIPHER_DICT = {'A': 'E', 'B': 'N', 'C': 'K', 'D': 'Q', 'E': 'A', 'F': 'U', 'G': 'Y', 'H': 'W', 'I': 'J', 'J': 'I', 
               'K': 'C', 'L': 'O', 'M': 'P', 'N': 'B', 'O': 'L', 'P': 'M', 'Q': 'D', 'R': 'X', 'S': 'Z', 'T': 'V', 
               'U': 'F', 'V': 'T', 'W': 'H', 'X': 'R', 'Y': 'G', 'Z': 'S'} #Reflector B Thin used in Kriegsmarine M4

CIPHER_DICT_2 = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P', 'J': 'X', 
               'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 
               'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'}  #Reflector B used by wehrmacht and luftwaffe


def get_reflector():
    '''
    Returns the cipher_dict
    '''
    
    return CIPHER_DICT
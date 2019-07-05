'''
An Enigma Scrambler or Enigma Rotor
Jakob Mckinney
25/01/2019
'''


CIPHER_DICT = {'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': '', 'L': '', 'M': '', 'N': '', 'O': '', 'P': '', 'Q': '', 'R': '', 'S': '', 'T': '', 'U': '', 'V': '', 'W': '', 'X': '', 'Y': '', 'Z': ''}
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ALPHABET_1 = ['J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N', 'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W']
ALPHABET_2 = ['N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B', 'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T']
ALPHABET_3 = ['F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P', 'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V']


class Scrambler:
    ''' A class for a Scrambler '''
    
    def __init__(self, init_condition, rotate=1, position=1):
        ''' 
        Initialises Scrambler class 
        '''
        self.position = position
        self.rotation = rotate
        self.cipher_dict = CIPHER_DICT.copy()
        self.set_alpha(int(init_condition))
        
        if position > 1:
            self.revolution = 1

        
    def set_alpha(self, init_condition):
        '''
        Calls the correct set_alpha method, depending on
        the init_condition set by user
        '''
        if self.position == 1:
            self.set_alpha_one(ALPHABET_1[init_condition])
        elif self.position == 2:
            self.set_alpha_two(ALPHABET_2[init_condition])
        else:
            self.set_alpha_three(ALPHABET_3[init_condition])

        
    def set_alpha_one(self, init_condition):
        ''' 
        Sets the cipher alphabet for scrambler from given
        condition
        '''
        start = ALPHABET_1.index(init_condition)
        
        # Iterates through the alphabet setting the Scrambler alphabet
        for i in range(0, 26):
            self.cipher_dict[ALPHABET[i]] = ALPHABET_1[start]
            start = (start + 1) % 26
            
        
    def set_alpha_two(self, init_condition):
        ''' 
        Sets the cipher alphabet for scrambler from given
        condition
        '''
        start = ALPHABET_2.index(init_condition)
        
        # Iterates through the alphabet setting the Scrambler alphabet
        for i in range(0, 26):
            self.cipher_dict[ALPHABET[i]] = ALPHABET_2[start]
            start = (start + 1) % 26
            
        
    def set_alpha_three(self, init_condition):
        ''' 
        Sets the cipher alphabet for scrambler from given
        condition
        '''
        start = ALPHABET_3.index(init_condition)
        
        # Iterates through the alphabet setting the Scrambler alphabet
        for i in range(0, 26):
            self.cipher_dict[ALPHABET[i]] = ALPHABET_3[start]
            start = (start + 1) % 26     
            
            
    def encrypt_letter(self, letter):
        ''' 
        Encrypts given letter by looking it up in the cipher
        dictionary, calls rotate method and returns ecrypted letter
        '''
        
        return self.cipher_dict[letter]
        
        
    def rotate(self):
        ''' 
        Finds the alphabet index of the letter currently assigned to 'A'
        then adds the given rotation amount and uses the set_alpha method
        to set the cipher_dict to the new conditions. The first Scrambler
        will always rotate, the second will rotate when the first has rotated
        26 times and the third will rotate when the second has rotated 26 times
        '''
        if self.position == 1 or self.revolution == 0:
            init_cond = self.cipher_dict['A']
            new_index = (ALPHABET.index(init_cond) + self.rotation) % 26
            self.previous_dict = self.cipher_dict
            self.set_alpha(new_index)
        
        if self.position == 2:
            self.revolution = (self.revolution + 1) % 26
        elif self.position == 3:
            self.revolution = (self.revolution + 1) % 676
            
                    
    def reverse_letter(self, letter):
        ''' 
        Works the opposite to encryption, so if A is passed in encrypt
        and B is returned, then here if B is passed then A will be returned
        '''
        keys = list(self.cipher_dict.keys())
        values = list(self.cipher_dict.values()).index(letter)
        new_letter = keys[values]
        
        return new_letter
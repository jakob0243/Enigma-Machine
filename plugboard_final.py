'''
A Plugboard
Jakob Mckinney
25/01/2019
'''

CIPHER_DICT = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class Plugboard:
    ''' A class for a plugboard '''
    
    def __init__(self):
        '''
        Initialises Plugboard class 
        '''
        self.cipher_dict = CIPHER_DICT
        self.set_plugboard() # Sets the plugboard
        
        
    def set_plugboard(self):
        '''
        Calls the get_settings method, which returns list of chars to swap,
        then iterates through these swapping them in self.cipher_dict each time
        '''
        
        swapping_list = self.get_settings()
        
        for chars in swapping_list:
            self.cipher_dict[chars[0]], self.cipher_dict[chars[1]] = chars[1], chars[0]
            print("Chars {0} and {1} swapped...".format(chars[0], chars[1]))
        
    
    def get_settings(self):
        '''
        Asks user what characters are to be swapped on the plugboard and returns
        a list where each item is a pair of characters to be swapped on the plugboard
        '''
        to_change = []
        
        changing = input("Do you want to enter settings? Y? ")
            
        # Asks for pair of chars to swap, stops if nothing entered
        while changing.upper() != '':
            changing = input("(Leave blank to move on)\nEnter two letters? ")
            if changing != '' and len(changing) == 2 and changing.isalpha():
                to_change.append(changing.upper())
                
        return to_change
    
    
    def pass_letter(self, letter):
        '''
        Passes the letter through the plugboard and returns the
        new letter
        '''
        
        return self.cipher_dict[letter.upper()]
    
    
    def reverse_letter(self, letter):
        '''
        Works the opposite to pass_letter, so if A is passed to pass_letter
        and B is returned, then here if B is passed then A will be returned
        '''
        keys = list(self.cipher_dict.keys())
        values = list(self.cipher_dict.values()).index(letter)
        new_letter = keys[values] 
        
        return new_letter
'''
An Enigma Machine
Jakob Mckinney
25/01/2019
'''
from plugboard_final import Plugboard
from scrambler_final import Scrambler
from mirror_final import get_reflector


class Enigma:
    ''' A class for an Enigma machine '''
    
    def __init__(self):
        '''
        Initalises the enigma system
        '''
        one, two, three = self.get_start_positions()
        self.plugboard = Plugboard()
        self.scrambler_one = Scrambler(one, 1, 1)
        self.scrambler_two = Scrambler(two, 1, 2) 
        self.scrambler_three = Scrambler(three, 1, 3)
        self.reflector = get_reflector()
        
        
    def get_start_positions(self):
        '''
        Asks for the start positions of the rotors/scramblers
        and returns them
        '''
        one = input("First rotor position, index? ")
        two = input("Second rotor start position, index? ")
        three = input("Third rotor start position, index? ")
        
        return one, two, three
        
        
    def encrypt_letter(self, letter):
        ''' 
        Encrypts letter by sending it through the plugboard
        and then the Scrambler. Returns the encrypted letter
        '''
        # Passes letter through the plugboard
        letter = self.plugboard.pass_letter(letter)
        # Passes the letter through the 3 Scramblers
        letter = self.scrambler_one.encrypt_letter(letter)
        letter = self.scrambler_two.encrypt_letter(letter)
        letter = self.scrambler_three.encrypt_letter(letter)
        # Passes the letter through the reflector
        letter = self.reflector[letter]
        # Passes the letter backwards through the Scramblers
        letter = self.scrambler_three.reverse_letter(letter)
        letter = self.scrambler_two.reverse_letter(letter)
        letter = self.scrambler_one.reverse_letter(letter)
        # Finally passes the letter backwards through the plugboard
        letter = self.plugboard.reverse_letter(letter)
        
        # Rotates the Scramblers
        self.scrambler_one.rotate()
        self.scrambler_two.rotate()
        self.scrambler_three.rotate()
        
        return letter # Returns the encrypted letter
    
    
    
if __name__ == "__main__":
    
    e = Enigma()
    while True:
        w = ""
        x = input("Word: ")
        for char in x:
            w += e.encrypt_letter(char)
            
        print(w)
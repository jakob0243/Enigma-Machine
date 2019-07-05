# Enigma-Machine

	- Used to encrypt messages in WWII
	- Instructions:
		- Run enigma.exe
		- For rotor positions enter a number between 1 and 3 for each
		  use each number only once, specifies which order to have the
		  rotor/scramblers in.
		- "Do you want to enter settings? Y?" is asking if you want to
		  change the settings for the plugboard, type "Y" if yes.
		- To enter characters that you want to swap enter them as a 
		  string of two upper case characters that you want to swap,
		  e.g. if you want to swap 'A' and 'B' type "AB"
		- "Word: " is asking for a word that you want to encrypt, enter
		  the word here and it will print the encryption of the word below
		- To decrypt restart engima.exe and enter the same settings as used
		  to encrypt the word and then when it asks for a word to encrypt,
		  enter the encrypted word and the decryption of that word will
		  be printed below.
	- Example:
		- First rotor position, index? 1
		- Second rotor start position, index? 2
		- Third rotor start position, index? 3
		- Do you want to enter settings? Y? Y
		- Enter two letters? AE
		- Enter two letters? IO
		- Enter two letters? UY
		- Enter two letters?
		- Word: ENIGMAWORKS
		- IIRDLNXJYHH

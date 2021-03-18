"""Word Finder: finds random words from a dictionary."""
from random import choice



class WordFinder:
    '''creates a class instance of wordfinder with a method for retuning one random word
    from the text file that was specified when the class was defined'''

    def __init__(self, path):
        file = open(path)
        self.words = self.parse(file)
        print(f'{len(self.words)} words read')
 
    def  parse(self, file):
        return [w.strip() for w in file]

    def random(self):
        '''
        Method that returns a random word from the list of words.
        '''
        return choice(self.words)
   

class RandomWordFinder(WordFinder):
    def parse(self, file):
        '''
        Method that returns a random word from a list of words but omits blank lines
        or words that begin with a special character.        
        '''
        return [w.strip() for w in file if w.strip() and not w.startswith('#')]

    


    

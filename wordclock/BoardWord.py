'''
Created on 26.04.2020

@author: cabral
'''
class BoardWord:
    
    def __init__(self, word, row, column):
        self.word = word
        self.row = row
        self.column = column
        
    def __str__(self):
        return self.word
    
    def __hash__(self):
        return hash((self.word, self.row, self.column))

    def __eq__(self, other):
        return (self.word, self.row, self.column) == (other.word, other.row, other.column)
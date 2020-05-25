'''
Created on 26.04.2020

@author: cabral
'''
class LayoutWord:
    
    def __init__(self, word, row, column):
        self.word = word
        self.row = row
        self.column = column
        
    def __str__(self):
        return self.word
    

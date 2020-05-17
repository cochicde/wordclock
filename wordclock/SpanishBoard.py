'''
Created on Apr 24, 2020

@author: cabral
'''

from wordclock import Board
from wordclock.BoardWord import BoardWord

class SpanishBoard(Board):
    
    def __init__(self):
        super().__init__("Spanish")
        
        self.firstWords = [
            BoardWord("ES", 0, 0), 
            BoardWord("SON", 0, 1)]
        
        self.secondWords = [
            BoardWord("LA", 0, 5), 
            BoardWord("LAS", 0, 5)]
        
        self.hourWords = [BoardWord("UNA", 0, 8), 
                          BoardWord("DOS", 1, 0), 
                          BoardWord("TRES", 1, 4), 
                          BoardWord("CUATRO", 2, 0), 
                          BoardWord("CINCO", 2, 6), 
                          BoardWord("SEIS", 3, 0),  
                          BoardWord("SIETE", 3, 5), 
                          BoardWord("OCHO", 4, 0), 
                          BoardWord("NUEVE", 4, 4),  
                          BoardWord("DIEZ", 5, 2), 
                          BoardWord("ONCE", 5, 7), 
                          BoardWord("DOCE", 6, 0)]
        
        self.unionWords = [BoardWord("Y", 6, 5),  
                           BoardWord("MENOS", 6, 6)]
        
        self.minutes = [BoardWord("CINCO", 8, 6),
                        BoardWord("DIEZ", 7, 7), 
                        BoardWord("CUARTO", 9, 5), 
                        BoardWord("VEINTE", 7, 1), 
                        BoardWord("VEINTICINCO", 8, 0), 
                        BoardWord("MEDIA", 9, 0)]
        
        self.allWords = self.firstWords + self.secondWords + self.hourWords + self.unionWords + self.minutes
        
    #Given a time, it returns a ([]BoardWord, int) where the second element is the 1-minute grain (0 - 4) 
    def get_words_and_points_from_time(self, time):
        minute = time.minute
        hour = time.hour
        words_to_return = []
        
        if (hour > 11): #from 13 to 23, it will keep from 1 to 11 
            hour = hour - 12
   
        hour_index = hour - 1 #Hour 1 is a position 0
        union_index = 0
        minute_index = int(minute / 5)
        
        if (minute_index > 6): #from 35 to 55 this will require the next hour and "MENOS"
            minute_index = 12 - minute_index #wrap to the possible six options
            union_index = 1 #MENOS
            hour_index += 1 #use the next hour
            
        is_plural = int(hour_index != 0) 
        
        words_to_return.append(self.firstWords[is_plural])
        words_to_return.append(self.secondWords[is_plural])
        words_to_return.append(self.hourWords[hour_index])
        if(minute_index != 0):
            words_to_return.append(self.unionWords[union_index])
            words_to_return.append(self.minutes[minute_index - 1])
        
        return (words_to_return, minute % 5)
        

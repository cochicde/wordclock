
import datetime 
import calendar

#we don't use the official datetime because we need to be able to set fields to None
class OwnDatetime:
    
    def __init__(self, year, month, day, hour, minute, second):
        self.values = [year, month, day, hour, minute, second]
        
        # The following code  is used to test if the provided values are in their valid range
        # Default valid values are given if None were provided
        if year == None:
            year = 2020
        if month == None:
            month = 1
        if day == None:
            day = 1
        if hour == None:
            hour = 0
        if minute == None:
            minute = 0
        if second == None:
            second = 0    
        
        # If invalid values are provided, the next call will raise an exception
        datetime.datetime(year, month, day, hour, minute, second)
        
    # Two periods are similar if both have the same fields defined.
    # This is needed because if starting and finishing dates of a period are not similar, 
    # a time slot cannot be calculated
    def check_similar(self, second):
        for i in range(len(self.values)):
            if (self.values[i] == None) != (second.values[i] == None):
                return False
        
        return True
    
    def substract_time_s(self, second):
        
        # instead of 2020 it must be the current year, but since this is called 
        # every cycle we don't want to add another call,
        # and the cases it won't be precise are in leap year and in February this is not a big thing 
        year = self.values[0] if self.values[0] != None else 2020
        month = self.values[1] if self.values[1] != None else 12
        max_days_of_month = calendar.monthrange(year, month)[1]
        
        
        own_datetime = datetime.datetime(self.values[0] if self.values[0] != None else 2020,  
                                self.values[1] if self.values[1] != None else 12,
                                self.values[2] if self.values[2] != None else max_days_of_month,
                                self.values[3] if self.values[3] != None else 23,
                                self.values[4] if self.values[4] != None else 59,
                                self.values[5] if self.values[5] != None else 59)
        
        second_datetime = datetime.datetime(second.values[0] if second.values[0] != None else 2020,  
                                second.values[1] if second.values[1] != None else 12,
                                second.values[2] if second.values[2] != None else 1,
                                second.values[3] if second.values[3] != None else 0,
                                second.values[4] if second.values[4] != None else 0,
                                second.values[5] if second.values[5] != None else 0)
        
        return (own_datetime - second_datetime).total_seconds()
    
    # this comparison is not well done yet. A bug happened when it was May 31st and it was compared to :06: period, meaning a june period,
    # which only has 30 days. So the day (coming from the datetime_to_check was not in the range of the period June.
    # A quick hack was added but the way of doing the whole function does not seem right
    def compare(self, datetime_to_check):
        
        year = self.values[0] if self.values[0] != None else datetime_to_check.year
        month = self.values[1] if self.values[1] != None else datetime_to_check.month
        day = self.values[2] if self.values[2] != None else datetime_to_check.day
        hour = self.values[3] if self.values[3] != None else datetime_to_check.hour
        minute = self.values[4] if self.values[4] != None else datetime_to_check.minute
        second = self.values[5] if self.values[5] != None else datetime_to_check.second
        
        if day > calendar.monthrange(year, month)[1]:
            day = calendar.monthrange(year, month)[1]
        
        
        #we add the microseconds to avoid wrong results in the comparisons
        own_datetime = datetime.datetime(year, month, day, hour, minute, second, datetime_to_check.microsecond)
        if own_datetime == datetime_to_check :
            return 0
        elif own_datetime > datetime_to_check:
            return 1
        else:
            return -1
        
    
    # Just for testing    
    def __str__(self):
        return ("Year = " + str(self.values[0]) + 
                    ", Month = " + str(self.values[1]) +
                    ", Day = " + str(self.values[2]) +
                    ", Hour = " + str(self.values[3]) +
                    ", Minute = " + str(self.values[4]) +
                    ", second = " + str(self.values[5])) 
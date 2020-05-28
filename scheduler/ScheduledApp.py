from scheduler.OwnDatetime import OwnDatetime

class ScheduledApp:
    
    def __init__(self, app_name, executable, periods, period_freq, time, group = None):
        self.application = app_name
        self.executable = executable
        self.periods = []
        self.periods_in_seconds = []
        
        periods = periods.split(",")
        for period in periods:
            start_and_end = period.strip().split(' ')
            start_of_period = self.string_to_datetime(start_and_end[0])
            end_of_period = self.string_to_datetime(start_and_end[1])
            
            if not start_of_period.check_similar(end_of_period):
                print("Error [ScheduledApp]: The start period " + start_and_end[0] 
                      + "and the end " + start_and_end[1] + 
                      "don't match in their format. This application won't be added to the execution")
                self.application = ""
                return
            
            self.periods.append((start_of_period, end_of_period))
            # we store the period in seconds in order not to calculate them all the time
            # This is almost constant, except if the month is not selected (which defaults to January)
            # and also if February is selected, and so the period is bigger on leap years. But the differences
            # are small enough not to take in account, for now
            self.periods_in_seconds.append(end_of_period.substract_time_s(start_of_period))
            
        self.period_frequency = int(period_freq) 
        self.time = int(time)
        self.group = group
        
    def string_to_datetime(self, string):
        
        # storage for year, month and day
        date_list = [None, None, None] 
        
        # storage for hour, minute, second
        time_list = [None, None, None]
        
        date_and_time = string.split('-')
        
        if 2 == len(date_and_time): # time was provided
            time = date_and_time[1].split(":")
            for i in range(3):
                if time[i] != "":
                    time_list[i] = int(time[i])
        
        date = date_and_time[0].split(":")
        for i in range(3):
            if date[i] != "":
                date_list[i] = int(date[i])
                
        return OwnDatetime(date_list[0], date_list[1], date_list[2], time_list[0], time_list[1], time_list[2])
    
    # Just for testing
    def __str__(self):
        periods = "["
        for period in self.periods:
            periods += period[0].__str__() + " " +  period[1].__str__() + ", "
            
            
        periods += "]"
        return ("Name = " + self.application + 
                ", Executable = " + str(self.executable) +
                ", periods = " + periods +
                ", periods_in_seconds = " + str(self.periods_in_seconds) +  
                ", period_frequency = " + str(self.period_frequency) +
                ", time = " + str(self.time) +
                ", group = " + str(self.group)                )  
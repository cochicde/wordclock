
import datetime 

#we don't use the official datetime because we need to be able to set fields to None
class OwnDatetime:
    
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second 
        
        
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
        
class SchedulerParameters:
    
    def __init__(self, app_name, executable, periods, period_freq, time, group = None):
        self.application = app_name
        self.executable = executable
        self.periods = []
        
        periods = periods.split(",")
        for period in periods:
            start_and_end = period.strip().split(' ')
            self.periods.append((self.string_to_datetime(start_and_end[0]),self.string_to_datetime(start_and_end[1])))
            
        
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
        

class Scheduler:
    
    def __init__(self, executables, parameters):
        # Here I should save all executables and calculate all the times
        self.registered_apps = []
        apps_params_list = {}
        for param in parameters:
            app_name_and_param = param[0].split(".")
            
            if apps_params_list.get(app_name_and_param[0]) == None:
                 apps_params_list[app_name_and_param[0]] = {}
            
            apps_params_list[app_name_and_param[0]][app_name_and_param[1]] = param[1]
            
        
        for app_name in apps_params_list:
            self.registered_apps.append(SchedulerParameters(param, executables[app_name], 
                                                            apps_params_list[app_name]["period"],
                                                            apps_params_list[app_name].get("period_frequency", "10"),
                                                            apps_params_list[app_name].get("time", "2"),
                                                            apps_params_list[app_name].get("group", None)))
            
            
    
    def execute(self):
        #This shoudl be called from wordclock wich will take care of everythin
        #Here, the lowest time should be checked, and sleep untill next trigger.
        #There should be sempahore or something to wake him up
        #When it wakes up, it will check all executables if the period matches:
        #Start with year, month, day, ...
        #If year is not defined, it is repeated yearly
        #If month is not specified, it is repeated monthly
        # ... and so on.
        # The scheduler the will find the animation that fits the time
        # and execute it in a new thread and wait (semaphore) for the time that should run.
        # The scheduler should be able to stop the animation, because the time is up, or
        # an external event happened that force to stop it (from the web page for example)
        # If the stop wasn't because of external, it should show the clock. 
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
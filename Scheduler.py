
import datetime 
import calendar

#we don't use the official datetime because we need to be able to set fields to None
class OwnDatetime:
    
    def __init__(self, year, month, day, hour, minute, second):
        self.values = [year, month, day, hour, minute, second]
        self.needs_check = [year != None, month != None, day != None, hour != None, minute != None, second != None]
        
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
        for i in range(len(self.needs_check)):
            if (self.needs_check[i]) != (second.needs_check[i]):
                return False
        
        return True
    
    def substract_time_s(self, second):
        
        year = self.values[0] if self.needs_check[0] else 2020
        month = self.values[1] if self.needs_check[1] else 12
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
    
    def compare(self, datetime_to_check):
        
        own_datetime = datetime.datetime()
        
        year = self.values[0] if self.needs_check[0] != None else 2020
        month = self.values[1] if self.needs_check[1] != None else 12
    
    # Just for testing    
    def __str__(self):
        return ("Year = " + str(self.values[0]) + 
                    ", Month = " + str(self.values[1]) +
                    ", Day = " + str(self.values[2]) +
                    ", Hour = " + str(self.values[3]) +
                    ", Minute = " + str(self.values[4]) +
                    ", second = " + str(self.values[5])) 
                
        
class SubscribedApp:
    
    def __init__(self, app_name, executable, periods, period_freq, time, group = None):
        self.application = app_name
        self.executable = executable
        self.periods = []
        
        periods = periods.split(",")
        for period in periods:
            start_and_end = period.strip().split(' ')
            start_of_period = self.string_to_datetime(start_and_end[0])
            end_of_period = self.string_to_datetime(start_and_end[1])
            
            if not start_of_period.check_similar(end_of_period):
                print("Error [SubscribedApp]: The start period " + start_and_end[0] 
                      + "and the end " + start_and_end[1] + 
                      "don't match in their format. This application won't be added to the execution")
                self.application = ""
                return
            
            self.periods.append((start_of_period, end_of_period))
            print("Time difference between " + str(start_of_period) + " and " 
                  + str(end_of_period) + " is === " + str(end_of_period.substract_time_s(start_of_period)) )
            
        
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
    
    # return two values. The first one is True or False to indicate if the datetime to_check is in any of 
    # the periods the app has. 
    # The second returned value is the amount of seconds period lasta. If the app has more than one period that matches
    # the period to_check, the smaller period time is returned
    def is_datetime_in_period(self, to_check):
        found = False
        minimum_period = None
       # for perido in self.periods:
            
        
    
    
        
    # Just for testing
    def __str__(self):
        periods = "["
        for period in self.periods:
            periods += period[0].__str__() + " " +  period[1].__str__() + ", "
            
            
        periods += "]"
        return ("Name = " + self.application + 
                ", Executable = " + str(self.executable) +
                ", periods = " + periods +
                ", period_frequency = " + str(self.period_frequency) +
                ", time = " + str(self.time) +
                ", group = " + str(self.group)                )    
    
    
    
class Scheduler:
    
    def __init__(self, executables, parameters):
        self.registered_apps = []
        apps_params_list = {}
        for param in parameters:
            app_name_and_param = param[0].split(".")
            
            if apps_params_list.get(app_name_and_param[0]) == None:
                 apps_params_list[app_name_and_param[0]] = {}
            
            apps_params_list[app_name_and_param[0]][app_name_and_param[1]] = param[1]
            
        for app_name in apps_params_list:
            new_subscribed_app = SubscribedApp(app_name, executables[app_name], 
                                                            apps_params_list[app_name]["period"],
                                                            apps_params_list[app_name].get("period_frequency", "10"),
                                                            apps_params_list[app_name].get("time", "2"),
                                                            apps_params_list[app_name].get("group", None))
            
            # The application name is empty if the parameters have something wrong
            if new_subscribed_app.application != "":
                self.registered_apps.append(new_subscribed_app)
            
        
        for app in self.registered_apps:
            print(str(app))    
            print("")
    
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
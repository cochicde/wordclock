
import datetime
import time
from scheduler.ScheduledApp import ScheduledApp
from animations.AnimationBase import AnimationBase 

class Scheduler:
    
    def __init__(self, matrix, parameters):
        self.registered_apps = []
        
        name_and_classes = {cls.__name__ : cls for cls in AnimationBase.__subclasses__()}
        scheduler_params = parameters["scheduler"]
        
        for scheduled_app_name in scheduler_params.keys():
            
            # Different instances of the same class can be defined if they have a slash.
            # This is the case if the same app is instantiated with different parameters
            class_name = scheduled_app_name.split("/")[0]
            
            new_subscribed_app = ScheduledApp(scheduled_app_name, name_and_classes[class_name](matrix, parameters.get(scheduled_app_name, {})), 
                                                            scheduler_params[scheduled_app_name]["period"],
                                                            scheduler_params[scheduled_app_name].get("period_frequency", "10"),
                                                            scheduler_params[scheduled_app_name].get("time", "2"),
                                                            scheduler_params[scheduled_app_name].get("group", None))
            
            # The application name is empty if the parameters have something wrong
            if new_subscribed_app.application != "":
                self.registered_apps.append(new_subscribed_app)
        self.group_index = 0
        
    def execute(self):
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
        current_datetime = datetime.datetime.now()
        valid_apps = []
        apps_periods = []
        for app in self.registered_apps:
            minimum_period = -1
            # Check if the currenttime is between the app's periods ranges and take the minimum
            for i in range(len(app.periods)):
                if (app.periods[i][0].compare(current_datetime) <= 0 and app.periods[i][1].compare(current_datetime) >= 0) and (minimum_period == -1 or minimum_period > app.periods_in_seconds[i]):
                    minimum_period = app.periods_in_seconds[i]
                    
            if minimum_period != -1:
                valid_apps.append(app)
                apps_periods.append(minimum_period)
        
        if len(valid_apps) != 0:
            app_to_execute = valid_apps[apps_periods.index(min(apps_periods))]
            
            # If the app to execute has a group, iterate over all apps of the same group sequencially
            current_group = app_to_execute.group
            if current_group != None:
                apps_in_group = [app for app in valid_apps if app.group == current_group]
                if self.group_index >= len(apps_in_group):
                    self.group_index = 0
                
                app_to_execute = apps_in_group[self.group_index]
                self.group_index += 1
             
            app_to_execute.executable.execute()
            if app_to_execute.time > 0:
                time.sleep(app_to_execute.time)
            
            return app_to_execute.period_frequency
        else:
            return -1
        
        
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
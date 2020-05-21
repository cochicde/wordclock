
class Scheduler:
    
    def __init__(self, parameters):
        # Here I should save all executables and calculate all the times
        pass
    
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
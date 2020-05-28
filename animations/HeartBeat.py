import time
from animations.AnimationBase import AnimationBase
from animations.HeartBig import HeartBig
from animations.HeartSmall import HeartSmall

class HeartBeat(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
        
        parameters["color"] = parameters.get("color_small", "255 0 0")
        self.heart_small = HeartSmall(matrix_access, parameters)
        
        parameters["color"] = parameters.get("color_big", "255 0 0")
        self.heart_big = HeartBig(matrix_access, parameters)
        
        self.times = int(parameters.get("times", "2"))
        self.small_ms = int(parameters.get("small_ms", "300"))
        self.off_between_both_ms = int(parameters.get("off_between_both_ms", "100"))
        self.big_ms = int(parameters.get("big_ms", "300"))
        self.off_between_times_ms = int(parameters.get("off_between_times_ms", "300"))
        self.matrix_access = matrix_access
    
    def execute(self):
        self.matrix_access.turn_all_off()    
        for i in range(self.times):
            self.heart_small.execute()
            time.sleep(self.small_ms/1000)
                    
            self.matrix_access.turn_all_off()    
            self.matrix_access.refresh()
                    
            time.sleep(self.off_between_both_ms/1000)
    
            self.heart_big.execute()
            time.sleep(self.big_ms/1000)
            
            self.matrix_access.turn_all_off()    
            self.matrix_access.refresh()
            
            if i < self.times - 1:
                time.sleep(self.off_between_times_ms/1000)
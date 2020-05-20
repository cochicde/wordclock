import heart_big


def execute(parameters):
    for i in range(2):
        ledAccess.turn_all_off()    
        ledAccess.refresh()
        if i == 1:
            time.sleep(300/1000)
        set_heart_small(ledAccess)
        time.sleep(300/1000)
                
        ledAccess.turn_all_off()    
        ledAccess.refresh()
                
        time.sleep(100/1000)

        set_heart_big(ledAccess)
        time.sleep(300/1000)
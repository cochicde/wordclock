
class ConfigParser:
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def parse(self):
        ret_dict = {}
        line_counter = 1
        try:
            file = open(self.file_path, "r")
            for line in file:
                line_counter = line_counter + 1
                line.strip()
                if line[0] == '#' or line == "\n" : #Comments and empty lines are skipped 
                    continue 
                
                key_value = line.split('=')
                if len(key_value) != 2:
                    print("ERROR: Line " + str(line_counter) + "\n" + line + "\nis not well formed. It should be STRING = STRING")
                    return None
                
                for i in range(len(key_value)):
                    key_value[i] = key_value[i].strip()
                    
                keys = key_value[0].split('.')  
                
                target = keys[0]
                current_dict = ret_dict

                for i in range(0, len(keys)):
                    if i == len(keys) - 1: # last field
                        current_dict[keys[i]] = key_value[1]
                    else:
                        if keys[i] not in current_dict.keys():
                            current_dict[keys[i]] = {}
                            
                        current_dict = current_dict[keys[i]]
                        target = keys[i]
                        
        finally:
            file.close()
        
        return ret_dict
    



class ConfigParser:
    
    def __init__(self, file_path):
        self.file_path = file_path
        
    # It returns a dictionary whose keys are the target to which the parameter
    # is intended to
    # The value of the key is an array tupple like (rest of the name of the key as an array, string value defined in the file)
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
                    
                keys = key_value[0].split('.', 1)
                target = keys[0]
                extended_value = (keys[1], key_value[1])
                
                if target not in ret_dict.keys():
                    ret_dict[target] = []
                
                ret_dict[target].append(extended_value)
        
        finally:
            file.close()
        
        return ret_dict
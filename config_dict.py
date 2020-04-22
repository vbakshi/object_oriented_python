import os

class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as f:
                for line in f.readlines():
                    key,value = line.rstrip().split("=", 1)
                    dict.__setitem__(self, key, value)            
    
    def __setitem__(self, key, value):

        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as f:
            for k,v in self.items():
                line = '{0}={1}\n'.format(k, v)
                f.write(line)
    

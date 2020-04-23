import os

class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        if not os.path.isfile(self._filename):
            try:
                open(self._filename, 'w').close()
            except IOError:
                badpath = '\\'.join(self._filename.split("\\")[:-1])
                raise IOError("pathname: {} is invalid".format(badpath))
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
    
    def __getitem__(self, key):
        if key not in self.keys():
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)


class ConfigKeyError(KeyError):

    def __init__(self, inputDict, key):
        self.key = key
        self.keys = inputDict.keys()
    
    def __str__(self):
        return "key {0} not found. Available keys: ({1})".format(self.key, ', '.join(self.keys))
        
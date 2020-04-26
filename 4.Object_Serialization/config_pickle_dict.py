import os
import pickle
import pdb

class ConfigPickleDict(dict):

    config_directory = './configs/'

    def __init__(self, filename):
        self._filename = os.path.join(ConfigPickleDict.config_directory, filename + '.pickle')
        if (not os.path.isfile(self._filename)):
            with open(self._filename, 'wb') as fh:
                pickle.dump({}, fh)
        with open(self._filename, 'rb') as fh:
            # pdb.set_trace()
            pkl = pickle.load(fh)
            self.update(pkl)
    
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'wb') as fh:
            pickle.dump(self, fh)
    
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

# if __name__ == "__main__":
#     a = ConfigPickleDict('conf_test')
#     a['username'] = 'vinayak'
#     a['kerberos'] = 'bakshv'
#     print(a)
    #   pickle.dump(a, open('./configs/conf_test.pickle', 'wb'))
#     b = ConfigPickleDict('conf_test')
#     print(b)
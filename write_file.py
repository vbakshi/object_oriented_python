from datetime import datetime 
import abc

class WriteFile(object):

    __metaclass__ = abc.ABCMeta
    
    def __init__(self, filename):
        self.filename = filename
    
    def write_line(self, text):
        f = open(self.filename, 'a')
        f.write(text +'\n')
        f.close()

    @abc.abstractmethod
    def write(self, msg):
        pass
    
class LogFile(WriteFile):

    def write(self, msg):
        dt = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.write_line("{}   {}".format(dt, msg))

class DelimFile(WriteFile):

    def __init__(self, filename, delimiter):
        super(DelimFile, self).__init__(filename)
        self.delimiter = delimiter
    
    def write(self, msg_list):
        new_msg_list = []
        for ele in msg_list:
            if self.delimiter in ele:
                new_msg_list.append('"{0}"'.format(ele))
            else:
                new_msg_list.append(ele)
        self.write_line(','.join(new_msg_list))
    


    

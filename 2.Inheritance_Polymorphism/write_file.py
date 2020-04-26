from datetime import datetime 
import abc
import os

class WriteFile(object):

    __metaclass__ = abc.ABCMeta
    
    def __init__(self, filename):
        self.filename = filename

        if not os.path.isfile(self.filename):
            try:
                open(self.filename, 'w').close()
            except IOError:
                raise IOError("invalid file path: {}".format(self.filename))
    
    def write_line(self, text):
        with open(self.filename, 'a') as f:
            f.write(text +'\n')

    @abc.abstractmethod
    def write(self, msg):
        pass
    
class LogFile(WriteFile):

    def write(self, msg):
        dt = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.write_line("{}\t{}".format(dt, msg))

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
    
if __name__ == "__main__":
    wr = LogFile('./test_logfile_template.log')
    wr.write("running log file writer ...")
    wr.write("using write method to write lines with timestamp")

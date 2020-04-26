from datetime import datetime

class WriteFileUsingFormatter(object):

    def __init__(self, filename, formatter):
        self.formatter = formatter()
        self.fh = open(filename, 'w')
    
    def write(self, text):
        self.fh.write(self.formatter.format(text))
        self.fh.write('\n')

    def close(self):
        self.fh.close()


class CSVFormatter(object):

    def __init__(self):
        self.delim=','
    
    def format(self, input_list):
        new_list = []
        for ele in input_list:
            if self.delim in ele:
                new_list.append('"{0}"'.format(ele))
            else:
                new_list.append(ele)

        return self.delim.join(new_list)    

class LogFormatter(object):
    
    def format(self, text_body):
        strdate = datetime.now().strftime('%Y-%m-%d %H:%M')
        return "{0}  {1}".format(strdate, text_body)


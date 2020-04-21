from write_file import *

log = LogFile('./output/log.txt')
log.write("This is a log message")
log.write("This is another log message")

c = DelimFile("./output/text.csv",",")
c.write(['a','b','c'])
c.write(['1','2,','3'])

from write_file import *
from write_file_using_formatter import * 

log = LogFile('./output/log.txt')
log.write("This is a log message")
log.write("This is another log message")

c = DelimFile("./output/text.csv",",")
c.write(['a','b','c'])
c.write(['1','2,','3'])

writecsv = WriteFileUsingFormatter('./output/text2.csv', CSVFormatter)
writelog = WriteFileUsingFormatter('./output/log2.txt', LogFormatter)

writecsv.write(['hello,','people'])
writecsv.close()

writelog.write("Yolo")
writelog.write("Yolo Again")


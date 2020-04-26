from write_file import WriteFile, LogFile, DelimFile
import os 
import shutil
from datetime import datetime as dt
import pytest


class TestWriteFile(object):

    directory_path = os.getcwd()
    current_time = dt.now()
    
    def teardown(self):
        files_in_directory = [file for file in os.listdir(TestWriteFile.directory_path) if file.endswith('.txt') or file.endswith('.log') or file.endswith('.csv')]
        for file in files_in_directory:
            os.remove(file)

    def test_invalid_path(self):
        with pytest.raises(IOError):
            WriteFile(TestWriteFile.directory_path +"/resources/"+"testfile.txt")

    def test_write_line(self):
        gen_writer = WriteFile('./test_genfile.txt')
        gen_writer.write_line("Hello")
        gen_writer.write_line("How are you doing")
        with open('./test_genfile.txt') as fh:
            lines_actual = fh.readlines()
            assert lines_actual[0].strip('\n') == "Hello"
            assert lines_actual[1].strip('\n') == "How are you doing"
    
    def test_logfile_write(self):
        log_writer = LogFile('./test_logfile.log')
        log_writer.write("started logging")
        log_writer.write("testing log file writer")

        with open('./test_logfile.log') as lf:
            lines_actual = lf.readlines()
            timestamp1, line1 = lines_actual[0].split('\t')
            timestamp2, line2 = lines_actual[1].split('\t')

            date_obj = dt.strptime(timestamp1, '%Y-%m-%d %H:%M')

            assert line1.strip('\n') == "started logging"
            assert line2.strip('\n') == "testing log file writer"
            assert date_obj.year == TestWriteFile.current_time.year
            assert date_obj.month == TestWriteFile.current_time.month
            assert date_obj.day == TestWriteFile.current_time.day

    def test_delimfile_write(self):
        csv_write = DelimFile('./test_delimfile.csv', ",")
        csv_write.write(["a","b","c"])
        csv_write.write(["Hi,","How","are","you?"])

        with open('./test_delimfile.csv') as csv:
            lines = csv.readlines()

            assert lines[0].strip('\n').split(',') == ['a', 'b', 'c']
            assert lines[1].strip('\n')[:5] == '"Hi,"' 




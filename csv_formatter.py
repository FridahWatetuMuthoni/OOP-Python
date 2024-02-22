from datetime import datetime

class WriteFile:
    def __init__(self, filename, writter):
        self.fh = open(filename, 'w')
        self.formatter = writter
    
    def write(self, text):
        self.fh.write(self.formatter.format(text))
        self.fh.write('\n')
    
    def close(self):
        self.fh.close()
        
class CSVFormatter:
    
    def __str__(self):
        self.delim = ','
    
    def format(self, this_list):
        new_list = []
        
        for element in this_list:
            if self.delim in element:
                new_list.append(f"'{element}'")
            else:
                new_list.append(element)
        return self.delim.join(new_list)

class LogFormatter:
    
    def format(self, this_line):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        return f"{date_str} {this_line}"
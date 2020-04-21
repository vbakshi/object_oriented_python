class MaxSizeList(object):

    def __init__(self, max_size):
        self.res = []
        self.max_size = MaxSizeList.check_max_size(max_size)
    
    def push(self, ele):
        self.res.append(ele)
        if len(self.res) > self.max_size:
            self.res.pop(0)
    
    def get_list(self):
        return self.res
    
    @staticmethod
    def check_max_size(size):
        if ~isinstance(size, int) or size <= 0:
            raise ValueError("Invalid max size: {} Please enter a positive integer for max size".format(size))
        else:
            return size
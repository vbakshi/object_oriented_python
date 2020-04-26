import pytest
from max_size_list import MaxSizeList

class TestMaxSizeList(object):


    def test_push(self):
        max_sz_list = MaxSizeList(2)
        max_sz_list.push(1)
        max_sz_list.push(4)
        max_sz_list.push(7)
        max_sz_list.push(13)

        assert len(max_sz_list.get_list()) == 2
        assert max_sz_list.get_list()[-1] == 13
        assert max_sz_list.get_list()[0] == 7

    def test_input_exception(self):
        with pytest.raises(ValueError):
            max_sz_list = MaxSizeList("12")

    





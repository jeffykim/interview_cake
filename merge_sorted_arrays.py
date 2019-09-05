import unittest


def merge_lists(my_list, alices_list):
    new_list=[]

    while(len(my_list)!=0 or len(alices_list) !=0):

        my_list_item = my_list.pop(0)
        alices_list_item=alices_list.pop(0)
        
    #     my_list_item = my_list[0]
    #     alices_list_item = alices_list[0]
    #     if my_list_item>alices_list_item:
    #         new_list.append(alices_list_item)
    #         new_list.append(my_list_item)
    #     else:
    #         new_list.append(my_list_item)
    #         new_list.append(alices_list_item)
    #     my_list.pop(0)
    #     alices_list.pop(0)
    # if(len(my_list)!=0):
    #     new_list.append(my_list)
    # if(len(alices_list)!=0):
    #     new_list.append(alices_list)

    return new_list


















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
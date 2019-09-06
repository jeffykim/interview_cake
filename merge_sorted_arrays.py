import unittest


def merge_lists(my_list, alices_list):
    #determine the size of the new list
    new_list_size= len(my_list)+len(alices_list)
    print(new_list_size)
    #instatiate the list
    new_list=[None]*new_list_size
    #count will be the index of the new_list index
    count = 0
    my_count=0
    alice_count=0
    while(count<new_list_size):

        #need to handle 3 edge cases, where alice's list gets exhausted, my list gets exhausted, when a list is exhausted before the merge is complete
        #this is a index out of bounds error. Meaning how do you handle that?
        # handling edge case 1. when alice's list gets exhausted
        if alice_count>=len(alices_list):
            new_list[count] = my_list[my_count]
            my_count= my_count+1

        #handling the edge case 2 when my list gets exhausted

        elif my_count>=len(my_list):
            new_list[count]= alices_list[alice_count]
            alice_count=alice_count+1

        elif my_list[my_count]>alices_list[alice_count]:
            new_list[count]= alices_list[alice_count]
            alice_count=alice_count+1
        else:
            new_list[count]=my_list[my_count]
            my_count= my_count+1


        count=count+1



    # while(len(my_list)!=0 or len(alices_list) !=0):

    #     my_list_item = my_list.pop(0)
    #     alices_list_item=alices_list.pop(0)

    #more pythonic way would be
    # this would be in O(nlgn) time
    # new_list= sorted(my_list+alices_list)


        
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
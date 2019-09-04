import unittest


def merge_ranges(meetings):
    
    #an easy way to sort a list is by using the python list method sort()
    # or another way is sorted() a built in python function
    meetings.sort()
    print(meetings)# this confirms that the meetings are sorted
    
    #after this you now know the first beginning meeting time won't conflict
    #with the next meeting start time.
    
    
    #And then you can compare the end of the
    # previous meeting with the start time of the next meeting.
    #if the end of the first meeting is larger than or equal to the start of the second
    # you merge
    # if the end of the first meeting is less than the second meeting
    # you add it to the list
    merged_meetings =[meetings[0]]
    for meeting in meetings[1:]:
        test_start, test_end = meeting
        start, end = merged_meetings[-1]
        if end >= test_start:
            if end >=test_end:
                continue
            merged_meetings[-1] = (start, test_end)

        else:
            merged_meetings.append((test_start,test_end))




            
        
        
    return merged_meetings









# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
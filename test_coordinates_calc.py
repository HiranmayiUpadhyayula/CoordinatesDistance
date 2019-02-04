import unittest
from coordinates_calc import coordinates_distance


#test cases
class TestCoordinatesDistance(unittest.TestCase):
    def test_coordinates_distance(self):
        origin = [6, 33]
        expected = [{u'id': u'd', u'value': u'20,16'},
{u'id': u'z', u'value': u'32,33'},
{u'id': u'o', u'value': u'10,61'},
{u'id': u't', u'value': u'28,51'},
{u'id': u'a', u'value': u'31,49'},
{u'id': u'p', u'value': u'37,27'},
{u'id': u'n', u'value': u'18,64'},
{u'id': u'i', u'value': u'21,63'},
{u'id': u'w', u'value': u'18,66'},
{u'id': u'v', u'value': u'47,21'},
{u'id': u'l', u'value': u'6,76'},
{u'id': u'm', u'value': u'43,64'},
{u'id': u'k', u'value': u'0,81'},
{u'id': u'b', u'value': u'44,67'},
{u'id': u'j', u'value': u'19,84'},
{u'id': u'e', u'value': u'68,53'},
{u'id': u'q', u'value': u'44,88'},
{u'id': u'f', u'value': u'71,8'},
{u'id': u'h', u'value': u'34,97'},
{u'id': u'r', u'value': u'75,63'},
{u'id': u'g', u'value': u'61,90'},
{u'id': u'y', u'value': u'75,92'},
{u'id': u'c', u'value': u'93,6'},
{u'id': u's', u'value': u'99,46'},
{u'id': u'u', u'value': u'88,79'},
{u'id': u'x', u'value': u'84,100'}]

        out = coordinates_distance(origin)
        self.assertEqual(out, expected)
	
#comparing the actual output with the expected output. OK means the test cases were passed. 

if __name__ == '__main__':
    unittest.main()
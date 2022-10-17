import unittest
 
# Our code to be tested
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
 
# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def test_normal_case(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
 
    def test_negative_case(self): 
        """expect -1 as output to denote error when looking at negative area"""
        rectangle = Rectangle(-1, 2)
        self.assertEqual(rectangle.get_area(), -1, "incorrect negative output")

    def test_perimiter(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_perimeter(), 10, "incorrect perimeter")
 
# run the test
unittest.main()
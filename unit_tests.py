"""A template for a python script deliverable for INST326.
Names: Daniel Jeong, Irfan Mushfique, Nooran Elmostafa, Yaw Apraku
File: unit_tests.py
Assignment: Final Project
Due Date: -------
Description: This python file contains the unit tests for our final project
"""
from final_project import House
import unittest

class Function_Tester:
    def __init__(self, object):
        self.object = object
        self.base = final_project.size_base_value(self.object.size)

    def test_size_base_value(self):
        expected = 250000
        actual = final_project.size_base_value(self.object.size)
        self.assertEqual(expected, actual, "Failed to load correct output")

    def test_age_value(self):
        actual = final_project.age_value(self.object.age, base)
        expected = base * 1.05
        self.assertEqual(expected, actual, "Failed to load correct output")

    def test_bedrooms_bathrooms_value(self):
        actual = final_project.bedrooms_bathrooms_value(self.object.bedrooms, self.object.bathrooms, base)
        expected = base * 7.5
        self.assertEqual(expected, actual, "Failed to load correct output")

    def test_doors_windows_value(self):
        actual = final_project.doors_windows_value(self.object.doors, self.object.windows, base)
        expected = base * 8.5
        self.assertEqual(expected, actual, "Failed to load correct output")

    def test_location_safety_value(self):
        actual = final_project.location_safety_value(self.object.location, self.object.crime_rate, base)
        modifier = base * .08
        expected = base - modifier
        self.assertEqual(expected, actual, "Failed to load correct output")

    def test_value_checker(self):
        actual = final_project.location_safety_value(self.base)
        expected = "After assessing the different aspects of this property, we have " \
              "concluded that this property is a great buy and you shouldn't have any second thoughts about " \
              "purchasing the property!"
        self.assertEqual(expected, actual, "Failed to load correct output")


def main():
    house = House(1500, 15, 3, 4, 8, "Frisco,Texas", 21, 10.56)
    tester = Function_Tester(house)
    print(tester)

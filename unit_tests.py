from final_project import House
import unittest

class Function_Tester:
    def __int__(self, object):
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
        expected = "This property is not a good buy"
        self.assertEqual(expected, actual, "Failed to load correct output")


def main():
    house = House(1500, 12, 4, 3, 7, "Oakland,California", 20, 70.03)
    tester = Function_Tester(house)
    print(tester)

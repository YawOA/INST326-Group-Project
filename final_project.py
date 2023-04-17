"""A template for a python script deliverable for INST326.
Names: Daniel Jeong, Irfan Mushfique, Nooran Elmostafa, Yaw Apraku
File: final_project.py
Assignment: Final Project
Due Date: -------
Description: This is a property value estimator for homes in the USA. This program calculates the value
of a property based on the physical aspects of the home and does a final check based on said attributes
to determine whether the home is a good buy
"""

import sys
import argparse

class House:
    def __int__(self, size, age, bedrooms, bathrooms, windows, location, doors, crime_rate):
        """
        Arguments:
            size: The size of the home, in square feet
            age: The age of the home, in years
            bedrooms: Number of bedrooms in the home
            bathrooms: Number of bathrooms in the home
            windows: Number of windows installed throughout the house
            location: Where the home is located in
            doors: Number of doors throughout the house
            crime_rate: The crime rate within the area per capita
            Two optional parameters for this is garage for old homes (50 and up)
            whether it was renovated(these will be in boolean)
        Returns:
            New house object containing the above parameters
        """
        pass


def size_base_value(size):
    """
    Arguments:
        size: The size of the home, in square feet. This will set the base value of the home based on the
        following information:
        1. 120 - 500 feet: $500
        2. 501 - 800 feet: $100,000
        3. 801 - 1,000 feet: $175,000
        4. 1,001 - 1,500 feet: $250,000
        5. 1,501 - 2,500: $350,000
        6. 2,501 - 4,000: $500,000
        7. 4,001 - 5,000 feet: $750,000
        8. 5,001+ feet: $1,000,000
    Returns:
        Base value of the home based on size
    """
    pass

def age_value(age, current_value):
    """
    Arguments:
        current_value: Default value of home based on differing factors
        age: Age of home in years. This impacts the home value based on the following criteria:
        1. Newly built (0 - 4 years): 15% jump in home value
        2. Fairly new (5 - 10 years): 10% jump in home value
        3. Good shape (11 - 20 years): 5% jump in home value
        4. Decent Shape (21 - 40 years): 2.5% jump in home value
        5. Starting to push it (41 - 50 years): 0% change
        6. Aging (51 - 60 years): 3.5% drop in home value
        7. Really starting to age (61 - 70 years): 5% drop in home value
        8. Aging big time (71+ years): 7.5% drop in home value
    Returns:
         Modified home value based on age
    """
    pass

def bedrooms_bathrooms_value(bedrooms, bathrooms, current_value):
    """
    Arguments:
        current_value: Default value of home based on differing factors
        bedrooms: Number of bedrooms in the home
        Increase based on bedrooms comes down to the following:
            1. 0-1: 0% increase
            2. 2-5: 5% increase
            3. 6-9: 7.5% increase
            4. 10+: 12.5% increase
        bathrooms: Number of bathrooms in the home
        Increase based on bathrooms comes down to the following:
            1. 0-1: 0% increase
            2. 2-4: 2.5% increase
            3. 5-7: 5% increase
            4. 8+: 7.5% increase
    Returns:
        Modified home value based on number of bedrooms and bathrooms

    """
    pass

def doors_windows_value(doors, windows, current_value):
    """
    Arguments:
        current_value: Default value of home based on differing factors
        doors: Number of doors in home
        Increase based on number of doors comes down to the following:
            1. 0-7: 1.5% increase
            2. 8-14: 3.5% increase
            3. 15-21: 5% increase
            4. 22-34: 7.5% increase
            5. 35+: 10% increase
        windows: Number of windows in home
        Increase based on number of windows comes down to the following:
            1. 0-2: 1.5% increase
            2. 3-5: 3.5% increase
            3. 6-9: 5% increase
            4. 10-15: 7.5% increase
            5. 16+: 20% increase
    Returns:
        Updated home value based on number of doors and windows in home.

    """
    pass

def location_safety_value(location, crime_rate, current_value):
    """
    Arguments:
        current_value: Default value of home based on differing factors
        location: The location of the home (string) stated by full city name and full city state
        (ex. Philadelphia,Pennsylvania is valid)
        crime_rate: The crime rate of the location per capita (per 100,000 people)
        Value based on location and crime rate comes down to following factors:
            1. Locations with crime rate of 0-200 per 100,000: 7.5% increase
            2. Locations with crime rate of 201-400 per 100,000: 2.5% increase
            3. Locations with crime rate of 401-600 per 100,000: 1% decrease
            4. Locations with crime rate of 601-800 per 100,000: 5% decrease
            5. Locations with crime rate of 801+ per 100,000: 8% decrease
    Returns:
        Modified property value based on location and its crime rate

    """
    pass

def value_checker(final_value):
    """
    Arguments:
        final_value: This is the final value of the home based on all the physical attributes of the latter
    Returns:
        A final value assessment to determine whether the property in question is of good value
    """
    pass

def main(size, age, bedrooms, bathrooms, windows, location, doors, crime_rate):
    """
    Arguments:
        size: The size of the home, in square feet
        age: The age of the home, in years
        bedrooms: Number of bedrooms in the home
        bathrooms: Number of bathrooms in the home
        windows: Number of windows installed throughout the house
        location: Where the home is located in
        doors: Number of doors throughout the house
        crime_rate: The crime rate within the area per capita
    Returns:
        Creates object, computes home value using calculating functions, and determines whether the property is
        a good buy
    """


def parse_args(args_list):
    """
    Takes a list of strings from the command prompt and passes them through as arguments.
    Arguments:
        args_list (list) : the list of strings from the command prompt
        The arguments that will be taken in:
            size
            age
            bedrooms
            bathrooms
            windows
            location
            doors
            crime_rate
    Returns:
        args (ArgumentParser)
    """
    pass

if __name__ == "__main__":
    """
    Only function is to call the main
    """







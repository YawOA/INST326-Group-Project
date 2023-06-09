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
from argparse import ArgumentParser
import requests

class House:
    def __init__(self, size, age, bedrooms, bathrooms, windows, location, doors, crime_rate):
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
        self.size = size
        self.age = age
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.windows = windows
        self.location = location
        self.doors = doors
        self.crime_rate = crime_rate



def size_base_value(size):
    """
    Arguments:
        size: The size of the home, in square feet. This will set the base value of the home based on the
        following information:
        1. 120 - 500 feet: $50,000
        2. 501 - 800 feet: $100,000
        3. 801 - 1,000 feet: $175,000
        4. 1,001 - 1,500 feet: $250,000
        5. 1,501 - 2,500: $350,000
        6. 2,501 - 4,000: $500,000
        7. 4,001 - 5,000 feet: $750,000
        8. 5,001+ feet: $1,000,000
    Returns:
        Base value of the home based on size

    Source: https://www.homelight.com/blog/buyer-how-much-does-it-cost-to-build-a-house/
    """
    if size < 120:
        return None
    elif size <= 500:
        return 50000
    elif size <= 800:
        return 100000
    elif size <= 1000:
        return 175000
    elif size <= 1500:
        return 250000
    elif size <= 2500:
        return 350000
    elif size <= 4000:
        return 500000
    elif size <= 5000:
        return 750000
    else:
        return 1000000

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

    Source: https://www.opendoor.com/articles/factors-that-influence-home-value (Age section)
    """
    if (age >= 0) and (age <= 4):
        return current_value * 1.15
    elif (age >= 5) and (age <= 10):
        return current_value * 1.1
    elif (age >= 11) and (age <= 20):
        return current_value * 1.05
    elif (age >= 21) and (age <= 40):
        return current_value * 1.025
    elif (age >= 41) and (age <= 50):
        return current_value
    elif (age >= 51) and (age <= 60):
        decreaser = current_value * .035
        return current_value - decreaser
    elif (age >= 61) and (age <= 70):
        decreaser = current_value * .05
        return current_value - decreaser
    else:
        decreaser = current_value * .075
        return current_value - decreaser


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


    Source: https://newsilver.com/the-lender/how-much-value-does-an-extra-
    bedroom-add/#:~:text=A%20half%2Dbath%20has%20been,time%20to%20sell%20comes%20around.

    """
    bedrooms_increase = 0
    if bedrooms > 1 and bedrooms <= 5:
        bedrooms_increase = 0.05
    elif bedrooms > 5 and bedrooms <= 9:
        bedrooms_increase = 0.075
    elif bedrooms >= 10:
        bedrooms_increase = 0.125

    bathrooms_increase = 0
    if bathrooms > 1 and bathrooms <= 4:
        bathrooms_increase = 0.025
    elif bathrooms > 4 and bathrooms <= 7:
        bathrooms_increase = 0.05
    elif bathrooms >= 8:
        bathrooms_increase = 0.075

    return current_value * (1 + bedrooms_increase + bathrooms_increase)

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

    Source: https://thewindowdoorstore.com/how-much-value-do-new-windows-and-doors-add-to-a-home/#:~:text=
    Added%20Resale%20Value%20of%20New%20Windows%20and%20Doors&text=According%20to%20
    a%202020%20survey,estimated%20ROI%20of%2081%20percent.
    """
    if doors >= 0 and doors <= 7:
        door_inc = .015
    elif doors >= 8 and doors <= 14:
        door_inc = .035
    elif doors >= 15 and doors <= 21:
        door_inc = .05
    elif doors >= 22 and doors <= 34:
        door_inc = .075
    else:
        door_inc = 0.1

    if windows >= 0 and windows <= 2:
        window_inc = .015
    elif windows >= 3 and windows <= 5:
        window_inc = .035
    elif windows >= 6 and windows <= 9:
        window_inc = .05
    elif windows >= 10 and windows <= 15:
        window_inc = .075
    else:
        window_inc = 0.2

    updated_Value = current_value * (1 + door_inc + window_inc)

    return updated_Value

def location_safety_value(city, current_value, crime_rate):
    """
    Arguments:
        current_value: Default value of home based on differing factors
        city: The location of the home (string) stated by full city name and full city state
        (ex. Philadelphia,Pennsylvania is valid)
        crime_rate: The crime rate of the location per capita (per 1000 people) (float)
        Value based on location and crime rate comes down to following factors:
            1. Locations with crime rate of 0-20 per 1,000: 8.5% increase
            2. Locations with crime rate of 20-30 per 1,000: 3.5% increase
            3. Locations with crime rate of 30-42 per 1,000: 1% decrease
            4. Locations with crime rate of 42-50 per 1,000: 5% decrease
            5. Locations with crime rate of 50+ per 1,000: 8% decrease
    Returns:
        Modified property value based on location and its crime rate

    https://www.reallistingagent.com/blog/2021/5/5/how-crime-rate-affects-property-value#:~:
    text=Plenty%20of%20factors%2C%20both%20in,your%20property%20will%20be%20worth.

    """
    url_city = city.replace(" ", "-").lower()
    url_link = f"https://www.neighborhoodscout.com/{url_city}-crime"
    #url_link is reference for user to know where to go to get accurate crime data
    response = requests.get(url_link)

    if crime_rate > 0.0 and crime_rate <=20.0:
        return current_value * 1.085
    elif crime_rate > 20.0 and crime_rate <= 30.0:
        return current_value * 1.035
    elif crime_rate > 30.0 and crime_rate <= 42.0:
        decreaser = current_value * .01
        return current_value - decreaser
    elif crime_rate > 42.0 and crime_rate<= 50.0:
        decreaser = current_value * .05
        return current_value - decreaser
    else:
        decreaser = current_value * .08
        return current_value - decreaser



def value_checker(home, final_value, crime_rate):
    """

    Arguments:
        home: House object created via parameters by user
        final_value: This is the final value of the home based on all the physical attributes of the latter
    Returns:
        A final value assessment to determine whether the property in question is of good value
    """
    great_value_1 = (home.bedrooms >= 3) and (home.bathrooms >= 2) and (crime_rate <= 20) and \
                   (final_value <= 550000)

    great_value_2 = (home.windows >= 7) and (home.doors >= 20) and(home.bedrooms >= 4) and (home.bathrooms >= 3) \
                   and (crime_rate <= 20) and \
                   (final_value <= 450000)

    decent_value_1 = (home.bedrooms >= 2 and home.bedrooms <= 4) and \
                     (home.bathrooms >= 1 and home.bathrooms <= 3) and \
                     ((crime_rate >= 20 and crime_rate < 35) or (crime_rate >= 15 and crime_rate <= 25)) and \
                   (final_value >= 500000 and final_value <= 650000)

    decent_value_2 = (home.windows >= 5 and home.windows <= 8) and (home.doors >= 15 and home.doors <= 21) and \
        (home.bedrooms >= 2 and home.bedrooms <= 5) and \
        (home.bathrooms >= 1 and home.bathrooms <= 3) and \
        ((crime_rate >= 10 and crime_rate <= 20) or (crime_rate >= 20 and crime_rate <= 34)) and \
        (final_value >= 550000 and final_value <= 700000)

    questionable_value_1 = (home.bedrooms >= 1 and home.bedrooms <= 5) and \
                     (home.bathrooms >= 1 and home.bathrooms <= 3) and \
                     ((crime_rate >= 30 and crime_rate <= 45)) and \
                   (final_value >= 300000 and final_value <= 700000)

    questionable_value_2 = (home.windows >= 3 and home.windows <= 8) and (home.doors >= 12 and home.doors <= 23)\
                           and (home.bedrooms >= 1 and home.bedrooms <= 5) and \
                     (home.bathrooms >= 1 and home.bathrooms <= 3) and \
                     ((crime_rate >= 37 and crime_rate <= 50)) and \
                   (final_value >= 300000 and final_value <= 700000)

    bad_value_1 = (home.bedrooms >= 1 and home.bedrooms <= 3) and \
                     (home.bathrooms >= 0 and home.bathrooms <= 1) and \
                     ((crime_rate > 50)) and \
                   (final_value >= 200000 and final_value <= 800000)

    bad_value_2 = (home.windows >= 2 and home.windows <= 7) and (home.doors >= 7 and home.doors <= 23)\
                    and (home.bedrooms >= 1 and home.bedrooms <= 3) and \
                     (home.bathrooms >= 0 and home.bathrooms <= 1) and \
                     ((crime_rate >= 50)) and \
                   (final_value >= 200000 and final_value <= 800000)

    if great_value_1 == True or great_value_2 == True:
        print("After assessing the different aspects of this property, we have "
              "concluded that this property is a great buy and you shouldn't have any second thoughts about "
              "purchasing the property!")
    if decent_value_1 == True or decent_value_2 == True:
        print("After assessing the different aspects of this property, we have "
              "concluded that this property is a decent buy, through there are better options out there")
    if questionable_value_1 == True or questionable_value_2 == True:
        print("After assessing the different aspects of this property, we have "
              "concluded that this property has questionable value, and any thoughts of purchasing should be"
              "given a second thought")
    if bad_value_1 == True or bad_value_2 == True:
        print("After assessing the different aspects of this property, we have "
              "concluded that this property is not a good buy, and any thoughts of purchasing should be"
              "heavily reconsidered")


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
    print("326 PROPERTY VALUE ESTIMATOR:\n")
    home = House(size, age, bedrooms, bathrooms, windows, location, doors, crime_rate)
    base_value = size_base_value(home.size)
    print("The base value for the property is: $", base_value)

    age_adjusted_value = age_value(home.age, base_value)
    age_adjusted_value = round(age_adjusted_value, 2)
    print("The age of the home is", home.age, "years. Therefore, this changes the property value"
                                              " to $", age_adjusted_value)

    bedrooms_bathrooms_adjusted_value = bedrooms_bathrooms_value(home.bedrooms, home.bathrooms, age_adjusted_value)
    bedrooms_bathrooms_adjusted_value = round(bedrooms_bathrooms_adjusted_value, 2)
    print("There are", home.bedrooms, "bedrooms and", home.bathrooms, "bathrooms. Therefore, this changes the "
                                                                      "property value to $",
          bedrooms_bathrooms_adjusted_value)

    doors_windows_adjusted_value = doors_windows_value(home.doors, home.windows, bedrooms_bathrooms_adjusted_value)
    doors_windows_adjusted_value = round(doors_windows_adjusted_value, 2)
    print("There are", home.doors, "doors and", home.windows, "windows. Therefore, this changes the property"
                                                              " value to $",
          doors_windows_adjusted_value)

    location_safety_adjusted_value = location_safety_value(home.location, doors_windows_adjusted_value, home.crime_rate)
    location_safety_adjusted_value = round(location_safety_adjusted_value, 2)
    print("After assessing the location of the property, the final value "
          "comes out to $", location_safety_adjusted_value)

    value_checker(home, doors_windows_adjusted_value, home.crime_rate)

    print("\nThanks for using the 326 Property Value Estimator! We hope to have you back soon!")



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
    Returns:
        args (ArgumentParser)
    """
    parser = ArgumentParser()
    parser.add_argument('size', type=int, help='Size of the the property in square feet')
    parser.add_argument('age', type=int, help='Age of the property in years')
    parser.add_argument('bedrooms', type=int, help='Number of bedrooms in the property')
    parser.add_argument('bathrooms', type=int, help='Number of bathrooms in the property')
    parser.add_argument('windows', type=int, help='Number of windows on the property')
    parser.add_argument('location', type=str, help='Location of the property in the U.S')
    parser.add_argument('doors', type=int, help='Number of doors in property')
    parser.add_argument('crime_rate', type=float, help='Crime rate in location of property, per 1000')

    args = parser.parse_args(args_list)
    states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
    "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
    "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
    "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
    "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
    "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
    "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
    "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
    if not 102 <= args.size:
        raise ValueError("Property size must be larger than 102 square ft")
    if args.age < 0:
        raise ValueError("Property age cannot be negative")
    if args.bedrooms < 0:
        raise ValueError("Number of bedrooms cannot be negative")
    if args.bathrooms < 0:
        raise ValueError("Number of bathrooms cannot be negative")
    if args.windows < 0:
        raise ValueError("Number of windows cannot be negative")
    location_checker = args.location.split(",")
    if location_checker[-1] not in states:
        raise IndexError("State entered is not a real U.S state")
    if args.doors < 0:
        raise ValueError("Number of doors cannot be negative")
    if args.crime_rate < 0 and args.crime_rate > 1000:
        raise ValueError("Invalid crime rate enter. Ensure the crime rate you are entering is"
                         " per capita (per 1,000 people")
    return args



if __name__ == "__main__":
    """
    Only function is to intake arguments and call main
    """
    arguments = parse_args(sys.argv[1:])
    main(arguments.size, arguments.age, arguments.bedrooms, arguments.bathrooms,
            arguments.windows, arguments.location, arguments.doors, arguments.crime_rate)






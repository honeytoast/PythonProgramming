#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CPSC 223P
#### Assignment 1


class Category:
    """A class to be used for holding the label, lower, and upper bound of bmi
    categories."""

    def __init__(self, label, lower, upper):
        self.label = label
        self.lower = lower
        self.upper = upper


class Person:    
    """A class that holds all the personal information of the user, 
    including their BMR, BMI category, and needed change to go up and down 
    the next level."""

    def __init__(self, name, gender, age, weight, height):
        self.name = name
        self.gender = gender
        self.age = float(age)
        self.weight = weight
        self.height = height

        # Converts weight in kg to Newtons and divides by gravity to find mass. 
        # Conversions used: 1kg = 9.80665N, gravity on Earth: 9.807m/s^2 
        # Our mass on Earth is almost exactly the same as our weight in kg.
        self.mass = weight * 9.80665 / 9.807

        self.bmi = self.mass / (self.height / 100)**2
        
        if self.gender == 'F' or self.gender == 'f':
            self.bmr = bmrFemale(self.weight, self.height, self.age)
        elif self.gender == 'M' or self.gender == 'm':
            self.bmr = bmrMale(self.weight, self.height, self.age)

        # The BMI category the user is in
        self.category = self.lookUpBmiCategory()

        # The weight the user needs to be in the previous/next BMI level
        self.target_weightlow = self.category.lower * (self.height / 100)**2 
        self.target_weighthigh = self.category.upper * (self.height / 100)**2

        # The weight loss/gain needed for the user to move down/up BMI level
        self.target_loss = self.weight - self.target_weightlow
        self.target_gain = self.target_weighthigh - self.weight

        # Default weight and height units are in the metric system
        self.weight_unit = 'kg'
        self.height_unit = 'cm'
        
        # The amount of weekly weight loss/gain according to user's BMR
        self.weekly_change = self.bmr / 500 * .45
    
    # Creates the category class for each BMI category and returns the category
    # object that the user is in according to their BMI
    def lookUpBmiCategory(self):
        severeThinness = Category('Severe Thinness', 0, 15.99)
        moderateThinness = Category('Moderate Thinness', 16.0, 16.99)
        mildThinness = Category('Mild Thinness', 17.00, 18.49)
        normal = Category('Normal Range', 18.50, 24.99)
        overweight = Category('Overweight', 25.00, 29.99)
        obeseI = Category('Obese Class I (Moderate)', 30.00, 34.99)
        obeseII = Category('Obese Class II (Severe)', 35.00, 39.99)
        obeseIII = Category('Obese Class III (Very Severe)', 40, 0)
        
        return { self.bmi < 16.0: severeThinness,
             self.bmi >= 16.0 and self.bmi <= 16.99: moderateThinness,
             self.bmi >= 17.00 and self.bmi <= 18.49: mildThinness,
             self.bmi >= 18.50 and self.bmi <= 24.99: normal,
             self.bmi >= 25.00 and self.bmi <= 29.99: overweight,
             self.bmi >= 30.00 and self.bmi <= 34.99: obeseI,
             self.bmi >= 35.00 and self.bmi <= 39.99: obeseII,
             self.bmi > 39.99: obeseIII }[1]
    
    # Converts weight and height from kg and centimeters to pounds and inches
    # Called when the user wants to output their results in U.S. units
    def convertUS(self):
        self.weight_unit = 'lb'
        self.height_unit = 'in'
        self.weight = toPounds(self.weight)
        self.height = toInches(self.height)
        self.target_weightlow = toPounds(self.target_weightlow)
        self.target_weighthigh = toPounds(self.target_weighthigh)
        self.target_loss = toPounds(self.target_loss)
        self.target_gain = toPounds(self.target_gain)
        self.weekly_change = toPounds(self.weekly_change)

    # Prints formatted BMI and BMR report of the user
    def printResults(self):
        print("""
        BMI and BMR Report:
        ---------------------------------------------------------
        Name: {}      
        Age: {}
        Height: {}{}   \t\t\tWeight: {}{}
        BMI: {}       \t\t\tBMR: {}
        BMI Category: {}
        
        To lose/gain weight:
        
        - You must cut an extra {} kcal/day = {}{}/week.

        + You must eat an extra {} kcal/day = {}{}/week.
        """.format(self.name, int(self.age), form(self.height), 
                   self.height_unit, form(self.weight), self.weight_unit, 
                   form(self.bmi),form(self.bmr), self.category.label, 
                   form(self.bmr), form(self.weekly_change), self.weight_unit,
                   form(self.bmr), form(self.weekly_change), self.weight_unit))

        if self.category.label == 'Severe Thinness':
            print("""\r\tYou are already at the lowest BMI category.
            \r\tGain {}{} to go up to the next BMI category.
            \n\r\tPlease seek medical attention!
            """.format(form(self.target_gain), self.weight_unit))
        elif self.category.label == 'Obese Class III (Very Severe)':
            print("""\r\tLose {}{} to go down to the previous BMI category.
            \r\tYou are already at the highest BMI category.
            \n\r\tPlease seek medical attention!
            """.format(form(self.target_loss), self.weight_unit))
        else:
            print("""\r\tLose {}{} to go down to the previous BMI category.
            \r\tGain {}{} to go up to the next BMI category.
            \n\r\tGood luck!!!
            """.format(form(self.target_loss), self.weight_unit, 
                       form(self.target_gain), self.weight_unit))

    
# Formats output for floating point numbers
def form(x):
    return ("{0:.2f}".format(x))

# Calculates BMR for a female
def bmrFemale(weight, height, age):
    return 447.593 + (9.247 * weight) + (3.908 * height) - (4.330 * age)

# Calculates BMR for a male
def bmrMale(weight, height, age):
    return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

# Converts weight x in kilograms to pounds.
def toPounds(x):
    return x / .453592

# Converts height x in centimeters to inches.
def toInches(x):
    return x / 2.54

# Converts weight x in pounds to kilograms. 
def toKg(x):         
    return x * .453592

# Converts height x in inches to centimeters. 
def toCm(x):          
    return x * 2.54


# Asks the user to input their information and constructs a Person class 
# that stores and calls for calculation of other needed information before 
# printing their BMI and BMR report.
def main():
    print('\nHi! Welcome to the BMI/BMR calculator.')
    name = input('\nWhat is your name?: ')
    gender = input('\nAnd your gender is (F/M): ')
    age = input('\n{}, how old are you?: '.format(name))

    print('\nHow would you prefer to enter your weight and height?')
   
    input_format = input("""
    In metric units with centimeters and kilograms 
    or U.S. customary units with inches and pounds (metric/us): """)

    if input_format == 'us':
        weight = input('\nNow, please enter your weight in pounds: ')
        height = input('Lastly, please tell me your height in inches: ')
    else:
        weight = input('\nNow, please enter your weight in kilograms: ')
        height = input('Lastly, please tell me your height in centimeters: ')
    
    weight = float(weight)
    height = float(height)

    if input_format == 'us':
        weight = toKg(weight)
        height = toCm(height)

    user = Person(name, gender, age, weight, height)
    print("""\nHow would you like your results to be printed? 

    A report in metric units will output results in centimeters and kilograms. 
    A report in U.S customary units will output results in inches and pounds.
    """)

    output_format = input('Metric units or U.S. customary units? (metric/us): ')

    if output_format == 'us':
        user.convertUS()

    user.printResults()  

# Program entry point
if __name__ == '__main__':
    main()

Name: Grace Hadiyanto
E-mail: ifoundparis@gmail.com
CPSC 223P
Assignment 1

Product: BMI and BMR calculator

Description: The program prompts the user for their personal information
             such as:
             - Name
             - Age
             - Gender
             It then prompts them for the unit system (metric/us) that they want 
             to enter their weight and height in.
             After entering:
             - Weight
             - Height
             The program calculates the user's BMI, BMR, their BMI category
             and how much weight they need to gain or lose to go to the next
             or previous BMI category. All calculations are done in metric
	     units cm and kg. The formulas for the calculations have been
	     adjusted to use those units.
             
             The user is then asked if they want to view their report in the
             metric or U.S. customary units.
             
             The following is a template of the report that will be printed.
             
             BMI and BMR Report:
             ---------------------------------------------------------
             Name: {User name}      
             Age: {User age}
             Height: {User height}              Weight: {User weight}
             BMI: {User BMI}    		            BMR: {User BMR}
             BMI Category: {User BMI category}
        
             To lose/gain weight:
        
             - You must cut an extra {User BMR} kcal/day = {Weight change}/week.

             + You must eat an extra {User BMR} kcal/day = {Weight change}/week.
       
             Lose {User target loss} to go down to the previous BMI category.
             Gain {User target gain} to go up to the next BMI category.
            
             {Remark about the users needed loss/gain}

             After printing the report, the program exits.

Caution: When inputting their information, the user must read carefully.
         If the program prompts the user, unless obvious, there will be expected
         inputs in parentheses such as (expected_input1/expected_input2).
         The user is expected to input in case-sensitive format, one of
         the exact inputs inside the parentheses.

How to run: Open your terminal and make sure you are in the directory folder
            that contains "mybmi.py".
            Type "python3.3 mybmi.py" and press enter to start the program.

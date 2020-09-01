# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator months ==   to check elif a string is in a particular list/tuple like this:
# elif input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another elif...elif...else statement to "adjust" elif
# the day number falls within a certain range.

months = input("enter month")
date = int(input("enter date"))

if months == str("dec") and date >= int(21):
    print(months + " " + str(date) + " " + "is in winter" )
elif months == str("jan") or months ==  "feb":
    print(months + " " + str(date) + " " + "is in winter" )
elif months == str("mar") and date <= int(20):
    print(months + " " + str(date) + " " + "is in winter" )
elif months == str("mar") and date >= int(21):
    print(months + " " + str(date) + " " + "is in spring" )
elif months == str("may") or months ==  "april":
    print(months + " " + str(date) + " " + "is in spring" )
elif months == str("jun") and date <= int(21):
    print(months + " " + str(date) + " " + "is in spring" )
elif months == str("jun") and date >= int(22):
    print(months + " " + str(date) + " " + "is in summer" )
elif months == str("jul") or months ==  "aug":
    print(months + " " + str(date) + " " + "is in summer" )
elif months == str("sep") and date <= int(21):
    print(months + " " + str(date) + " " + "is in summer" )
elif months == str("sep") and date >= int(22):
    print(months + " " + str(date) + " " + "is in fall" )
elif months == str("oct") or months ==  "nov":
    print(months + " " + str(date) + " " + "is in fall" )
elif months == str("dec") and date <= int(20):
    print(months + " " + str(date) + " " + "is in fall" )










    






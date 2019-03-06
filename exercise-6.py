# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
print("Please enter the month as three characters: ") 
a = input("Enter the month of the season (Jan - Dec): ").lower()
b = int(input("Enter the day of the month: "))
c = ('dec', 'jan', 'feb', 'mar')
d = ('mar', 'apr', 'may', 'jun') #      Mar 20 - Jun 20: Spring
e = ('jun', 'jul', 'aug', 'sep') #      Jun 21 - Sep 21: Summer
f = ('sep', 'oct', 'nov', 'dec')
if ((a in d) and ((a == 'apr') or (a == 'may') or ((a == 'jun') and b in range(21)) or ((a == 'mar') and b in range(20, 31)))):
   k = "Spring" 
elif ((a in e) and ((a == 'jul') or (a == 'aug') or((a == 'sep') and b in range(21, 31)) or ((a == 'jun') and b in range(22)))):
   k = "Summer"
elif ((a in c) and ((a == 'jan') or (a == 'feb') or((a == 'mar') and b in range(20)) or ((a == 'dec') and b in range(21, 31)))):
   k = "Winter" 
else:
   k = "Fall"
print(f"{a} {b}  is in {k}") 
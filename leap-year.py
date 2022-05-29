import calendar

def leap_year(year):
    ''' Function to Know if a year is leap or no using method isleap from the module calendar'''
    if calendar.isleap(year):
        return 'The year ' + str(year) + ' is Leap'
    else:
        return 'The year ' + str(year) + ' is not Leap'

try:
    year = int(input('Please enter the year for you want to jnow if is leap or no: '))
    print(leap_year(year))
except ValueError:
    print('Please enter a number')

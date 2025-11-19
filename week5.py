# import mymodule

# mymodule.calculator()
# mymodule.module_name
import datetime
from datetime import datetime
from datetime import date 

def date_calculation():
    date_of_birth_str = input("Enter your date of birth (YYYY-MM-DD: ")
    date_of_birth = datetime.strptime(date_of_birth_str,"%Y-%m-%d").date()
    current_date = date.today()
    years_old = current_date.year - date_of_birth.year
    print("You are: ", years_old, "years old")

date_calculation()


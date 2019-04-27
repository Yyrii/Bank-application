from random_data.example_container import*
from random_data.numbers import*

def random_name():
    return user_names[random_number(0,len(user_names))]+'_'+str(random_number(1900,2010))


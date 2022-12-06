import math
from datetime import date
from conversion import pounds_to_kilograms

def compute_age():
    dob = date(1986, 10,22)
    today = date.today()
    delta = today - dob
    return math.floor(delta.days/365)

def addend_log(weight, bps, bpd, bpm):
    age = compute_age()
    kg = '{:.2f}'.format(pounds_to_kilograms(weight))
    year = date.today().year
    month = date.today().month
    day = date.today().day
    string = f'\n[{month}/{day}/{year}],{age},{kg},{bps}/{bpd},{bpm},183'
    with open('vitals.txt', 'a') as f:
        f.write(string)
        f.close()

def load_last_log_entry():
    with open('vitals.txt', 'r') as f:
        last_line = f.readlines()[-1]
        f.close()
    last_line_list = last_line.split(',')
    return last_line_list

def print_log_as_table():
    pass

def print_vitals_menu():
    print('Vitals log 1.0.0')
    print('Type "help" for more information')
    input_args = input('-> ')
    return input_args

def help_menu(input_args):
    # if input_args == '-h' or input_args == '--help':
    pass
from datetime import date, datetime, timedelta
import pickle

# this is due 12/9
# D - 5 Days
# remeber to use the main function
# primary calculator function
# import date/time

#        start_hour, start_minutes, duration minutes,
# write input validation that restricts user input to dates to in the future
# create a 2022 and 2023 data structure
# implement a function that automatically deletes an element off of the tree at the end of a month
# create escape sequence exits


calendar_2022 = {
    12: None
}

calendar_2023 = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
    10: None,
    11: None ,
    12: None
}

def save_practice_calendar(calendar):
    with open('practice_scalendar.pickle', 'wb') as f:
        pickle.dump(calendar, f)
        f.close()    



def print_day_planner_menu():
    print('Day Planner 1.0.0')
    print('Type "help" for more information')

def help():
    '''
        NAME

        day_planner - schedule and view tasks on a persistent calendar

    SYNOPSIS

        > python ./day_planner.py
        --- (Start Menu)
        Day Planner 1.0.0
        Type "help" for more information
        -> [OPTION...]

        -V, --view-tasks-by-date 
            enter a date and view tasks already created
        
        -s, --schedule-task-by-date 
            schedule a named task by date
            outputs the scheduled tasks by scheduled date
        
        -v, --version 
            output the version number to terminal

        -q, --quit 
            exit the application

    EXAMPLE TERMINAL OUTPUT
        > -V 
        12/01/2022
        TASK:1 [14:20:00 - 15:00:00] - User Defined Task

        > -s
        Enter The date of the task [mm/dd/yyyy] > 12/1/2022


    EXAMPLE LOG OUTPUT
        
    '''
    

def carriage_return():
        input_args = input('> ')
        # return menu_loop(input_args)

def transition_menu():
    # return carriage_return()
    return print_days_tasks(loaded_calendar)

def load_calendar():
    with open('practice_calendar.pickle', 'rb') as f:
        calendar = pickle.load(f)
        f.close()
    return calendar

def check_date_input_validation(date):
    pass


def print_days_tasks(calendar):
    task_date =  input('Enter date [mm/dd/yyyy] > ') # input validation
    try:
        date = task_date.split('/') # still need to be made to type int
    except ValueError:
        print('ERROR: use "/" character to specify date')
    if len(task_date) < 10:
        task_date = ''
        print('Enter the date in [mm/dd/yyyy] format')
        transition_menu()
    input_date = datetime(int(date[2]), int(date[0]), int(date[1]))
    m = input_date.month
    d = input_date.day
    try:
        for key in calendar[m][d]:
                start_time = timedelta(hours=calendar[m][d][key][0],minutes=calendar[m][d][key][1])
                duration = timedelta(minutes=calendar[m][d][key][2])
                end_time = start_time + duration
                description = calendar[m][d][key][3]
                print(input_date)
                print(f'TASK:{key} [{start_time} - {end_time}] - {description}')
    except KeyError:
        print('Day Unscheduled')

def task_list_element_creator(calendar):
    task_date =  input('Enter The date of the task [mm/dd/yyyy] > ') # input validation
    date = task_date.split('/') # still need to be made to type int
    m = int(date[0])
    d = int(date[1])
    try:
        for key in calendar[m][d]:
                start_time = timedelta(hours=calendar[m][d][key][0],minutes=calendar[m][d][key][1])
                duration = timedelta(minutes=calendar[m][d][key][2])
                end_time = start_time + duration
                description = calendar[m][d][key][3]
                print(f'TASK:{key} [{start_time} - {end_time}] - {description}')
    except KeyError:
        print('Day Unscheduled')
    start_time_string = input('Enter task start time (24h time) [hh:mm] > ')
    start_time_list = start_time_string.split(':') # still need to be made to type int
    task_duration = int(input('Enter the duration of the task [m] > '))
    task_name = input('Enter task name > ')
    new_datetime = datetime(int(date[2]), int(date[0]), int(date[1]), int(start_time_list[0]), int(start_time_list[1]))
    m = new_datetime.month
    d = new_datetime.day
    task = [new_datetime,task_duration,task_name]
    return task
        
def add_task_to_calendar(calendar, task):
    m = task[0].month
    d = task[0].day
    sh = task[0].hour
    sm = task[0].minute
    dm = task[1]
    tn = task[2]
    if calendar[m] == None:
        calendar[m] = {d:{1:task[2:]}}
    else:
        scheduled_days = []
        num_tasks = []
        for key in calendar[m]:
            scheduled_days.append(key)
        if d in scheduled_days:
            conflict = False
            for key in calendar[m][d]:
                start_time = timedelta(hours=calendar[m][d][key][0],minutes=calendar[m][d][key][1])
                duration = timedelta(minutes=calendar[m][d][key][2])
                end_time = start_time + duration
                description = calendar[m][d][key][3]
                print(f'TASK:{key} [{start_time} - {end_time}] - {description}')
                proposed_task_start_time = timedelta(hours=sh, minutes=sm)
                duration_delta = timedelta(minutes=dm)
                proposed_task_end_time = proposed_task_start_time + duration_delta
                if proposed_task_start_time < start_time and proposed_task_end_time < start_time:
                    conflict = False
                elif proposed_task_start_time > end_time and proposed_task_end_time > end_time:
                    conflict = False
                else:
                    conflict = True
                    print('^^^^')
                    print(f'[CONFLICT] Try a different date or time. {proposed_task_start_time}')
                    print()
                num_tasks.append(key)
                transition_menu()
            if not conflict:
                new_task_numbers = []
                task_number = 0
                for elem in num_tasks:
                    if sh < calendar[m][d][elem][0]:
                        new_task_numbers.append(elem + 1)
                task_number = new_task_numbers[0] - 1
                for elem in reversed(new_task_numbers):
                    calendar[m][d][elem] = calendar[m][d][elem - 1]
                calendar[m][d][task_number] = [sh,sm,dm,tn]
                for key in calendar[m][d]:
                    start_time = timedelta(hours=calendar[m][d][key][0],minutes=calendar[m][d][key][1])
                    duration = timedelta(minutes=calendar[m][d][key][2])
                    end_time = start_time + duration
                    print(f'TASK:{key} [{start_time} - {end_time}] - {description}')

        else:
            calendar[m][d] = {1:task[2:]}
            start_time = timedelta(hours=sh,minutes=sm)
            duration = timedelta(minutes=dm)
            end_time = start_time + duration
            print('Task Added')
            print(f'TASK:1 [{start_time} - {end_time}] - {tn}')       
    return calendar


if choice == '-V' or choice == '--view-tasks-by-date':
    print_days_tasks(***)
    transition_menu()
elif choice == '-s' or choice == '--view-tasks-by-date':
    updated_calendar = add_task_to_calendar(calendar, task_list_element_creator(***))
elif choice == 'help':
    help()__docs__



# add a print day to file option
# print days tasks after entering the day in the menu

"""
    calorie_log = []
    calorie macro intake
    keto fat percentage
    chart of eating times and quantities
    percentage adhered to
    days since started diet
"""
# > just started

'''
    Routine definintions


WR_definition =
3:45 - 4:00 Wake Up Routine
   15 min wake up routine with boxing
        -rnd 1-
    2 min shadow boxing (warmup)
    1 min rest
        30 sec down 32 ounces water
        30 sec crunches
        -rnd 2-

    2 min sh1adow boxing
    1 min rest
        30 sec get dressed
        30 sec pushups
        -rnd 3-
    2 min shadow boxing (shoe shine rnd)
    1 min rest
        30 sec prep steak
        30 sec crunches
        -rnd 4-
    2 min shadow boxing (1/2 hand speed round)
    1 min rest
        30 sec prep audio clip for run
         30 sec crunches
        -rnd 5-
    2 min shadow boxing (constant defense)
    1 min rest
        prep for run
            '''
MR_definition  = '''
2h
    7.5 VR1
    15 minute programming challenge (listen to the Bible)
    5 memorization: Psalm 119 4vv.
    7.5 Rosary
    7.5 Prayer
    15 morning hygiene
        1m hot towel
        8m shave
        2m shower
        4m moisturize, teeth, other hygine
            30 min strictly reading eloquent javascript
            22.5 VR2 
1h
    45 minute programming challenge while watching bloomberg to prep for the trading day
    15 minute prep for the day
       news articles in the new york times, wall street journal, pack for the day, lecture prep
'''
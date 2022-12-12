from datetime import datetime, timedelta

# serialization
def print_startup_menu():
    print('Day Planner 1.0.0')
    print('Type "help" for more information')
    input_args = input('-> ')
    return input_args

# ! > task output syntax
def create_new_task():
    task_date = (input('Enter task date -> ')).split('/')
    start_time = (input('Enter start time -> ')).split(':')
    duration = (input('Enter duration -> ')).split(':')
    stl = task_date + start_time
    start_time_datetime = datetime(eval(stl[2]),eval(stl[1]),eval(stl[0]),eval(stl[3]),eval(stl[4]))
    duration_delta = timedelta(hours=eval(duration[0]),minutes=eval(duration[1]))
    end_time_datetime = start_time_datetime + duration_delta
    return start_time_datetime, end_time_datetime, duration



# create a way to track what times of what days are planned and unplanned

if print_startup_menu() == 'a':
    start, end, duration = create_new_task()
    print(f'{start.date()} {start.time()} {end.time()}')



'''
    what do I need?:
        I need to know the total amount of free time remaining on a particular day after planning a task
        I need to be able to print a layout of the time table with spaces indicating planned time slots and freetime at any point in the planning program
        I need to know what days aren't planned by week and month
        I need to be able to expand a task and see what the outline of the task is
        I need to be plan lectures or repeating tasks once
        I need a man page
        I need persistence
        I need to be able to update diet and vitals logs
        I need to be able to print out logs in a table format
        I need to create an activity log and be able to perform operations on the data
        I need to be able to print a what time a task is by name for a day and a week


day_dict = {
# start_time: duration
    '3:45': [0, 15]
    ...
}
'''
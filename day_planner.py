# this is due 12/9
# D - 7 Days
import datetime

'''
    water intake calculator
'''

water_requirements = [
    None,
    224,
    224,
    224,
    224,
    224,
    192,
    128
]
# water_remaining = 0
water_consumed = 0
water_log = []

'''
    Calorie intake calculator
'''


# primary calculator function

class Log:
    pass
#

def macros(cals, macro_type):
    multplier = 0
    if macro_type == fat:
        multplier = 9
    else:
        multplier = 4
    return cals * multplier

'''
    exercise specific functions
'''

days = [
    None,
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

weeks = {
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
    11: None,
    12: None,
    13: None,
    14: None,
    15: None,
    16: None,
    17: None,
    18: None,
    19: None,
    20: None,
    21: None,
    22: None,
    23: None,
    24: None,
    25: None,
    26: None,
    27: None,
    28: None,
    29: None,
    30: None,
    31: None,
    32: None,
    33: None,
    34: None,
    35: None,
    36: None,
    37: None,
    38: None,
    39: None,
    40: None,
    41: None,
    42: None,
    43: None,
    44: None,
    45: None,
    46: None,
    47: None,
    48: None,
    49: None,
    50: None,
    51: None,
    52: None
}

months = [
    None,
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

'''
workouts = {
    wk
    1: {}
}
'''

# import date/time
def body_fat_log_addend(date, time,tbw, perc, log):
    bf_pounds = '{:.2f}'.format(perc * tbw) + ' #'
    bf_perc = '{:.2f}'.format(perc) + '%'
    output_string = f'{date} -  {time}: {bf_perc} body fat percentage -> {bf_pounds} body fat'
    return log.append(output_string)


def weekly_training_session_checker(year, month, day, workout_weeks_list):
    week_ind = datetime.date(year, month, day).isocalendar().week
    if week[week_ind] == None:
        return True
    else:
        return False

# > add yoga
def weekly_training_session_adder(year, month, day, weeks_list, workouts_dict, start_hour, start_min, duration_min):
    week_ind = datetime.date(year, month, day).isocalendar().week
    day_num = datetime.date(year, month, day).isocalendar().weekday
    # > while loop here
    # Sunday == 7
    if weekly_training_session_checker(year, month, day, weeks_list) == False:
        print('-r -> add run') # completed
        print('-s -> add strength training session') # began
        print('-b -> add boxing training session') # began
        print('-a -> add abs training session') # completed
        print('-y -> add yoga training session') # completed
        workout_type = input("Enter the type of workout:")
        # > add input validation
        # > not finished
        if day_num == 7 and workout_type == '-r':
            print("ERROR: Today is a run off day")
            print("ERROR: Choose -s, -b, -a or -y")
        elif day_num == 6 and (workout_type != '-r' or workout_type != '-a'):
            print("ERROR: Today is strictly a run day")
            print("ERROR: Choose the correct day and workout")

        elif and workout_type ==  '-s':
            plan_complete = False
            strength_dict = {}
            '''
            strength_dict = {
                1: [exercise_name, sets, reps, notes]
                2: [exercise_name, sets, reps, notes]
                ...
            }
            # print in table format
            '''
            while not plan_complete:
                exercise_num = 1
                exercise_name = input('Enter the excercise name: ')
                sets = input('Enter the number of sets: ')
                repetitions = input('Enter the number of repetitions: ')
                notes = input('Enter any notes for this exercise: ' or None)
                strength_dict[excercise_num] = [exercise_name, sets, repetitions, notes] 
                completed = input("Adding any other exercises? [y/n] ")
                if completed = 'y':
                    plan_complete  = True
                else:
                    excercise
                     

        # > not finished
        elif workout_type ==  '-b':
            plan_complete = False
            '''
            boxing_dict = {
                1: [exercise_name, duration_min, rest_min, notes]
                2: [exercise_name, duration_min, rest_min, notes]
                ...
            }
            # print in table format
            '''
            while not plan_complete:
                exercise_name = input('Enter the excercise name: ')
                duration = input('Enter the round duration in minutes: ')
                rest = input('Enter the rest interval in minutes: ')
                notes = input('Enter any notes for this exercise: ' or None)
                completed = input("Adding any other exercises? [y/n] ")
                if completed = 'y':
                    plan_complete  = True

        elif workout_type == '-a':
            '''
            abs_dict = {
                1: [exercise_name, sets, reps, notes]
            }
            '''
            abs_dict = {
                1: ['Hanging Leg Lifts', 3, 15, '1 min. rest -> (15 sec. rest, 30 sec. crunches, 15 sec. rest)'],
                2: ['Barbell Windshield Wipers', 4, 10, 'Super set with 12 weighted sit-ups, 1 min rest -> (15 sec. rest, 30 sec. crunches, 15 sec. rest)'],
                3: ['Cable Crunches', 15, 4, 'Super set with exercises 4 and 5, 30 second rest after entire circuit'],
                4: ['Downard Cable Choppers', 15, 4, '2nd exercise in Superset, 15 each side'],
                5: ['Upward  Choppers', 15, 4, '3nd exercise in Superset, 15 each side, 30 seconds rest after'],
                duration: duration_min,
                start_time: [start_hour, start_min]
            }
            return workouts_dict[week_ind][day_num] = abs_dict

        elif workout_type == '-y':
                '''
            yoga_dict = {
                    1: ['Saturno Movement Yoga', '3:55 - 23:55', 'https://www.youtube.com/watch?v=ITzF85_88x4']
                    duration: 20
                    start_time: [11,20]
            }
                '''
            yoga_dict = {
                1: ['Saturno Movement Yoga', '3:55 - 23:55', 'https://www.youtube.com/watch?v=ITzF85_88x4']
                duration: 20
                start_time: [11,20]
            }
            return workouts_dict[week_ind][day_num] = yoga_dict

        elif workout_type == '-r':
            '''
            run_dict = {
                1: [run_milaeage, audio_url, audio_duration, t/o, weather(32_deg_f/clear),notes]
                2: [exercise_name, duration_min, rest_min, notes]
                ...
            }
            '''
            # int input validation
            run_mileage = int(input("Enter the mileage of the run: "))
            audio_url = input("Enter the URL for the audio file you will listen to during the run: ")
            audio_duration_min =  int(input("Enter the duration in minutes of the audio file "))
            setting = input("-o -> Outside, -t -> treadmill: ")
            weather = []
            # input validation
            weather[0] = int(input("Enter temperature outside during the run in fahrenheit: "))
            weather[1] = input("Enter weather conditions outside during -c -> clear, -p -> rain/snow, -w -> wind: ")
            notes = input("Enter any additional notes: ")

            run_dict = {
                1: [run_milaeage, audio_url, audio_duration_min, setting, weather, notes]
            }
            return workouts_dict[week_ind][day_num] = run_dict



        '''
        if day_num == 7:
            workouts_dict[week_ind] = day_num:{['boxing', 'strength', 'abs']}
        elif day_num < 6:
            workouts_dict[week_ind] = day_num:{[['run']['boxing', 'strength', 'abs']]}
        else:
            workouts_dict[week_ind] = day_num:{['run']}
        '''

def percentage_workout_completion():
    pass

4 = {
    1:['boxing','stength','Abs']
    2:
    3:
    4:
    5:
    6:
    7:['run']
}


'''
    Routine Constants
'''
todo_tasks = ['WR', 'MR','ER','Run','Boxing','Lecture','Abs','TOP', 'Boxing Practice', 'htb']
sleep_hours = [8,4]
available_hours = 24


'''
    Study specific...
'''
lectures = {
    # class: [lecture title, text material covered]
}







'''
    Fitness specifics
'''
run_log = {
    # date/time: [mileage, pace, {BPM:[],pulse:[]}, (i/o)]
} 
   # percentage completion compared to plans/ expectation
   # is there a way to figure out what the oxygen composition of the air is at what altitutes

avg_run_pace = 9.2
    # create a function that outputs the average pace, visualization of the progression  

races = []
    # figure out how to incorporate .ics files into when races are and develope a coutndown clock
v02max = 0


crossfit_log = {} 
   # percentage completion compared to plans/ expectation

strength_training_log = {} 
   # percentage completion compared to plans/ expectation

one_RM_log {
    # date:[excercise,lift]
}


def water_tracker(ounces, water_consumed, water_log, year, month, day, requirements):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    day = datetime.date(year, month, day).isocalendar().weekday
    if water_log[len(water_log)-1][1] > date:
        water_consumed = 0
        requirements = water_reguirements[day]
    water_consumed += ounces
    remaining = requirements - water_consumed
    log_entry = water_log.push([month,date,hour,minute,second,day,water_consumed,remaining])
    print(f'ADDED: [{hour}:{minute} -> {ounces} oz. -> {remaining} oz. remaining]')
    return water_log, water_consumed, remaining
    

"""
    calorie_log = []
    calorie macro intake
    keto fat percentage
    chart of eating times and quantities
    percentage adhered to
    days since started diet
"""
# > just started
def calorie_tracker(calories, macro, year, month, day, requirements):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    day = datetime.date(year, month, day).isocalendar().weekday
    if calorie_log[][] > date:
         = 0
        requirements = water_reguirements[day]
    water_consumed += ounces
    remaining = requirements - water_consumed
    log_entry = water_log.push([month,date,hour,minute,second,day,water_consumed,remaining])
    print(f'ADDED: [{hour}:{minute} -> {ounces} oz. -> {remaining} oz. remaining]')
    return water_log, water_consumed, remaining

'''
    Routine definintions

'''
WR_definition = '''
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
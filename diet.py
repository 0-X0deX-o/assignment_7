from time_elements import month,date,hour,minute,second,get_day_num
from conversion import pounds_to_kilograms, kilograms_to_pounds, calories_to_grams
from vitals_log import load_last_log_entry, compute_age

# This takes calorie input and outputs the lines to a csv file

meal = {
    'fat':[0,0],
    'carbs':[0,0],
    'protein':[0,0]
}

cal_requirements_per_day = [None, 4149, 4149, 4149, 2242, 4213, 3511, 1827]

# BMR * activity factors = caloric need
met_factors = {
    'walking': 4.0,
    # 'running': [[speed mph ,MET value][speed mph, MET value]]
    'running': [[6.0, 10.0],[6.7, 11.0],[7.5, 12.5],[8.6, 14.0],[10,16.5]],
    'strength_training': 6.0,
    # 'boxing': [[activity, MET value][activity, MET value]]
    'boxing': [['bags/pads', 9.0],['sparring', 7.0]],
    'jump_rope': 10.5,
    'yoga': 4.0,
    'desk_work': 1.3,
    'sleeping': 0.9,
    'standing': 2.0 
}

# how to determine MET value
# eqn = wt-kg * MET 

def compute_percentage_carb_intake(carb_calories, total_calories):
    percentage_int = carb_calories / total_calories
    return percentage_int

def load_weight():
    list_entry = load_last_log_entry()
    kg = list_entry[3]
    return kg

def compute_basal_metabolic_rate(weight_kg, age_years):
    # revised Harris-Benedict Formula   
    # 66.5 + (13.75 * kg) + (5.003 * htcm) - (6.755 * age)
    bmr = 66.5 + (13.75 * weight_kg) + (5.003 * 183) - (6.755 * age_years)
    return bmr

def compute_bmi(weight_kg):
    return weight_kg/(1.83**2)

def addend_body_compostion_log(entry_num,year,month,date,weight_kg,bmi,bfp):
    entry_num += 1
    pnds = '{:.1f}'.format(kilograms_to_pounds(weight_kg))
    bf_pnds = '{:.2f}'.format(eval(pnds) * bfp)
    lbm = 1-bfp
    lbm_pnds = '{:.2f}'.format(lbm * eval(pnds))
    entry = f'\n{entry_num},[{month}/{date}/{year}],{pnds},{bmi},{bfp},{bf_pnds},{lbm},{lbm_pnds}'
    with open('body_composition.txt', 'a') as f:
        f.write(entry)
        f.close()

# rewrite
def meal_updater(calories, macro, meal):
    meal[macro][0] += calories
    grams = calories_to_grams(calories, macro)
    meal[macro][1] += grams

meal = {
    'fat':[0,0],
    'carbs':[0,0],
    'protein':[0,0]
}



'''
log entry structure
date,time,total calories,[fat cal, protein cal, carbs cal] carbs % ,remaining total calories,[remaining fat cal, remaining protein cal, remaining carbs cal] 
'''


    '''
    
    This needs to be moved to the water tracker
    
    if calorie_log[0][0] > date:
        requirements = water_reguirements[day]
    water_consumed += ounces
    remaining = requirements - water_consumed
    log_entry = water_log.push([month,date,hour,minute,second,day,water_consumed,remaining])
    print(f'ADDED: [{hour}:{minute} -> {ounces} oz. -> {remaining} oz. remaining]')
    return water_log, water_consumed, remaining
    '''
    pass

def load_entry_number(last_line_list):
    return last_line_list[0]
# Mass
def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def kilograms_to_pounds(kilos):
    return kilos * 2.20462

# Distance
def inches_to_centimeters(inches):
    return inches * 2.54

# Energy
def grams_to_calories(grams, macro_type):
    if macro_type == 'fat':
        multplier = 9
    else:
        multplier = 4
    return grams * multplier

def calories_to_grams(calories, macro_type):
    if macro_type == 'fat':
        divisor = 9
    else:
        divisor = 4
    return calories / macro_type
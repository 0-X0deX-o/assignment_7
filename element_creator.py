import pickle

calendar = {
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
    12: None
}

with open('calendar.pickle', 'wb') as f:
    pickle.dump(calendar, f)
    f.close()
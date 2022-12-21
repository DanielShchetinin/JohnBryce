import datetime
import random

def testing(dateNumberToName):

    date_string = "2022-12-21, Mon, 20:10"
    ret_val = dateNumberToName(date_string)

    assert ret_val == "Thursday"
    

def dateNumberToName(date_string):
    t1 = datetime.datetime.strptime(date_string, "%Y-%m-%d, %a, %H:%M")
    t1 += datetime.timedelta(days=3)
    return t1.strftime("%A")

# date_string = f"2022-12-19, Mon, 20:10"
# week_name = dateNumberToName(date_string)
# print(week_name)

# import datetime

# # timestamp = datetime.datetime.now()
# # print(timestamp)
# # print(timestamp.timestamp())


# # dt2 = datetime.datetime.strptime("19-12-2022", "%d-%m-%Y")
# # print(dt2)


# # dt1 = datetime.datetime.now()
# # print(dt1.strftime("Today is: %d.%m.%Y"))

# # now = datetime.datetime.now()

# # now_plus_1_day = now + datetime.timedelta(days=1)
# # now_plus_1_day_correct = now_plus_1_day.strftime("\nDate: %d.%m.%Y\nTime: %H:%M:%S")
# # print("Inserted:", now_plus_1_day)
# # print("\nCorrected:", now_plus_1_day_correct)

# def my_test(n: int):
#     prod = 1
#     for i in range(n):
#         prod = prod * n
        
# if __name__ == "__main__":
#     start = datetime.datetime.now()
#     my_test(1000000)
#     end = datetime.datetime.now()
#     run_time = (end - start).total_seconds()
#     print(run_time)



class Car:
    
    def __init__(self, typecar, color):
        
        self.typecar = typecar
        
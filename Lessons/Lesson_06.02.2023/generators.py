import datetime
def batches(n: int, l: list):
    i = 0
    while i < len(l):

        yield l[i: i+n]
        i += n

if __name__ == '__main__':
    start = datetime.datetime.now()
    choose = input("\nДля начала напишите Start: ")
    if choose == "Start":
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        for b in batches(3, 'sadfasdfsadfsadf'):
            print(b)
    start = datetime.datetime.now()
    end = datetime.datetime.now()
    date = end.strftime("%d.%m.%Y")
    time = end.strftime("%H:%M")
    run_time = (end - start).total_seconds()
    print("\nProgram Run Time:", run_time, "Seconds\n")
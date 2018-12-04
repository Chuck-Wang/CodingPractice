from collections import defaultdict


def func1():
    with open("input_4") as file:
        input_list = file.read().split("\n")
    log_list = []
    dict = defaultdict(int)
    time_dict = defaultdict(int)
    count = 0
    for x in input_list:
        list = x.split()
        year = int(list[0].split("-")[0][1:])
        month = int(list[0].split("-")[1])
        date = int(list[0].split("-")[2])
        time = int(list[1].split(":")[1].split("]")[0])
        if not int(list[1].split(":")[0]) == 0:
            date += 1
            time = 0
        rest = list[2:]
        log_list.append([year, month, date, time, rest])
    log_list = sorted(log_list, key = lambda x : (x[1], x[2], x[3]))
    print log_list
    current_guard = -1
    sleep = 0
    for x in log_list:
        if len(x[4]) == 4:
            current_guard = int(x[4][1].split("#")[1])
        if len(x[4]) == 2:
            if x[4][0] == "falls":
                sleep = x[3]
            if x[4][0] == "wakes":
                dict[current_guard] += x[3] - sleep
    print dict
    max = 0
    max_guard = 0
    for keys in dict:
        if dict[keys] > max:
            max = dict[keys]
            max_guard = keys
    print max
    print max_guard
    current_guard = -1
    sleep = -100
    for x in log_list:
        if len(x[4]) == 4:
            current_guard = int(x[4][1].split("#")[1])
        if len(x[4]) == 2:
            if current_guard == max_guard:
                if x[4][0] == "falls":
                    sleep = x[3]
                if x[4][0] == "wakes":
                    for i in range(sleep, x[3]):
                        time_dict[i] += 1
                    sleep = -100
    print time_dict
    max = 0
    max_time = 0
    for keys in time_dict:
        if time_dict[keys] > max:
            max = time_dict[keys]
            max_time = keys
    print max
    print max_time

func1()

def func2():
    with open("input_4") as file:
        input_list = file.read().split("\n")
    dict = {}
    count = 0
    for i in range(1, 1001):
        dict[i] = defaultdict(int)
    for x in input_list:
        list = x.split()

# func2()

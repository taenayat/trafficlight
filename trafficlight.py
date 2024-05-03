import numpy as np
import matplotlib.pyplot as plt

def get_traffic_light_status(t, n, time_lag, red, green):
    is_green = np.zeros(n, dtype=bool)
    time_lag = np.mod(time_lag, red+green)
    t_one_cycle = np.mod(t,red+green)
    for i in range(n):
        lag = np.mod(time_lag * i, red+green)
        if lag > red:
            if t_one_cycle < lag - red or t_one_cycle >= lag:
                is_green[i] = True
            else:
                is_green[i] = False
        else:
            if t_one_cycle < lag or t_one_cycle >= green + lag:
                is_green[i] = False
            else:
                is_green[i] = True
    return is_green

def forward_car_wait_time_calculate(n, time_lag ,red, green, drive_time, nudge=0):
    wait_time, i = 0, 0
    t = nudge # starting time of the car may be 0 or maybe the car arrives later
    while True:
        status = get_traffic_light_status(t, n, time_lag, red, green)
        if status[i] == True:
            i += 1
            t += drive_time
        else:
            t += 1
            wait_time += 1
        # print('t=',t, status, 'wait:', wait_time)
        if i >= n:
            break
    return wait_time


def backward_car_wait_time_calculate(n, time_lag ,red, green, drive_time, nudge=0):
    wait_time, i= 0, n-1
    t = nudge # starting time of the car may be 0 or maybe the car arrives later
    while True:
        status = get_traffic_light_status(t, n, time_lag, red, green)
        if status[i] == True:
            i -= 1
            t += drive_time
        else:
            t += 1
            wait_time += 1
        # print('t=',t, status, 'wait:', wait_time)
        if i < 0:
            break
    return wait_time

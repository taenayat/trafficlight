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


# red = 10 # red time
# green = 12 # green time
# time_lag = 0 # lag between traffic lights
# n = 2 # number of traffic lights

# is_green = np.ones(n, dtype=bool) # by default every traffic light is green
# x = 0 # total time behind redlight
# # forward car:
# for t in range(red+green):
#     for i in range(n):
#         if not is_green[i]:
#             x += t - red


# for i in range(n):
#     if time_lag * i > red:
#         is_green[i] = True

        # if t_one_cycle == -green + time_lag * i:
        #     is_green[i] = False
        # if t_one_cycle == time_lag * i:
        #     is_green[i] = True
        # if t_one_cycle == green + time_lag * i:
        #     is_green[i] = False



# for t in range(2*(red+green)):

    # if status[i] == False:
    #     wait_time += 1
    # else:
    #     i += 1



# forward_wait, backward_wait = np.zeros((10,20)), np.zeros((10,20))
# for red in np.arange(1,11):
#     for time_lag in np.arange(red+green):
#         forward_wait[red-1,time_lag] = forward_car_wait_time_calculate(n, time_lag, red, green, drive_time)
#         backward_wait[red-1,time_lag] = backward_car_wait_time_calculate(n, time_lag, red, green, drive_time)

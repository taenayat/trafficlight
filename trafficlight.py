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



######################################################################

red = 5 # red time
green = 10 # green time
n = 10
drive_time = 3

forward_wait, backward_wait = np.zeros(red+green), np.zeros(red+green)
for time_lag in range(red+green):
    for nudge in range(red+green):
        forward_wait[time_lag] += forward_car_wait_time_calculate(n, time_lag, red, green, drive_time, nudge)
        backward_wait[time_lag] += backward_car_wait_time_calculate(n, time_lag, red, green, drive_time, nudge)
    forward_wait[time_lag] /= (red+green)
    backward_wait[time_lag] /= (red+green)

# plt.plot(forward_wait)
# plt.plot(backward_wait)
plt.plot(forward_wait + backward_wait)
plt.xlabel('lag time')
plt.ylabel('forward + backward time')
plt.show()

######################################################################

n = 6
drive_time = 3
min_wait = np.zeros((10,10))

for red in np.arange(1,11):
    print(red)
    for green in np.arange(1,11):

        forward_wait, backward_wait = np.zeros(red+green), np.zeros(red+green)
        for time_lag in range(red+green):
            for nudge in range(red+green):
                forward_wait[time_lag] += forward_car_wait_time_calculate(n, time_lag, red, green, drive_time, nudge)
                backward_wait[time_lag] += backward_car_wait_time_calculate(n, time_lag, red, green, drive_time, nudge)
            forward_wait[time_lag] /= (red+green)
            backward_wait[time_lag] /= (red+green)
        min_wait[red-1,green-1] = np.min(forward_wait + backward_wait)

plt.imshow(min_wait)
plt.colorbar(label='waiting time')
plt.xlabel('red time')
plt.ylabel('green time')
plt.show()


######################################################################

n = 11
green = 10
min_wait = np.zeros((10,10))

for red in np.arange(1,11):
    print(red)
    for drive_time in range(green):

        forward_wait, backward_wait = np.zeros(red+green), np.zeros(red+green)
        for time_lag in range(red+green):
            for nudge in range(red+green):
                forward_wait[time_lag] += forward_car_wait_time_calculate(n, time_lag, red, green, drive_time, nudge)
                backward_wait[time_lag] += backward_car_wait_time_calculate(n, time_lag, red, green, drive_time, nudge)
            forward_wait[time_lag] /= (red+green)
            backward_wait[time_lag] /= (red+green)

        min_wait[red-1,drive_time] = np.min(forward_wait + backward_wait)
        
plt.imshow(min_wait)
plt.colorbar(label='waiting time')
plt.xlabel('red time')
plt.ylabel('drive time between two traffic lights')
plt.show()

######################################################################

n = 6
drive_time = 3
green = 10
min_wait = np.zeros(10)

for i, red in enumerate(np.arange(1,21,2)):
    print(i)
    forward_wait, backward_wait = np.zeros(red+green), np.zeros(red+green)
    for time_lag in range(red+green):
        for nudge in range(red+green):
            forward_wait[time_lag] += forward_car_wait_time_calculate(n, time_lag, red, green, drive_time, nudge)
            backward_wait[time_lag] += backward_car_wait_time_calculate(n, time_lag, red, green, drive_time, nudge)
        forward_wait[time_lag] /= (red+green)
        backward_wait[time_lag] /= (red+green)
    # min_wait[i] = np.min(forward_wait + backward_wait)
    min_wait[i] = np.min(forward_wait + backward_wait) / red

plt.plot(np.arange(1,21,2), min_wait)
plt.xlabel('red time')
plt.ylabel('waiting time')
plt.show()



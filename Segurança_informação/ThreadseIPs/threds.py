from threading import Thread
import time


def car(velocity, pilot):
    track = 0
    while track <= 100:
        track += velocity
        time.sleep(0.2)
        print(f"Pilot: {pilot} Km: {track}")


t_car1 = Thread(target=car, args=[1,'FU'])
t_car2 = Thread(target=car, args=[1.5, 'LÃ'])

t_car1.start()
t_car2.start()

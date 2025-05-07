import time


class timer():
    def __init__(duration):
        pass
    def timer(duration):
        print("running")
        time.sleep(1)
        duration -= 1
        if duration <=0:
            print("end")
            return "end"
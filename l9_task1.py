import time

class TrafficLight:
    def __init__(self, color):
        self._color = color

    def running(self):
        colors = {7.0: ['\033[31m', 'RED'], 2.0: ['\033[33m', 'YELLOW'], 5.0: ['\033[32m', 'GREEN']}
        for key, val in colors.items():
            self._color = colors[key][1]
            print(colors[key][0] + self._color)
            time.sleep(key)

a = TrafficLight('WHITE')
a.running()

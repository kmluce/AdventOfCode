import fileinput

class BusSchedule():
    def __init__(self):
        self.leaveTime = 0
        self.frequencies = []
        self.closestTime = 0
        self.closestBus = 0

    def print_schedule(self):
        print("time is:", self.leaveTime)
        for element in self.frequencies:
            print(element)

    def process_schedule(self):
        for line in fileinput.input():
            if fileinput.isfirstline():
                line = line.rstrip()
                self.leaveTime = int(line)
            else:
                line = line.rstrip()
                self.frequencies = line.split(',')
        self.print_schedule()

        for bus in self.frequencies:
            if bus == 'x':
                pass
            else:
                busNo = int(bus)
                busTime = (int(self.leaveTime / busNo) + 1) * busNo
                print("Bus ", busNo, " comes at ", busTime)
                if self.closestTime == 0 or self.closestTime > busTime:
                    self.closestTime = busTime
                    self.closestBus = busNo
        print("Result is bus ", self.closestBus, " at ", self.closestTime, " for result of ",
              (self.closestTime - self.leaveTime) * self.closestBus)





if __name__ == '__main__':
    schedule = BusSchedule()
    schedule.process_schedule()

class HuantedBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pickup(self, passenger):
        self.passengers.append(passenger)

    def dropoff(self, passenger):
        self.passengers.remove(passenger)


team = ['Alice', 'Bob', 'Charlie', 'David']
bus1 = HuantedBus(team)
print(bus1.passengers)
bus1.pickup('Flora')
print(bus1.passengers)
bus1.dropoff('Bob')
print(bus1.passengers)
print(team)
print(">>>>>>>>>>>>>")
bus2 = HuantedBus()
bus3 = HuantedBus()
bus2.pickup('Alice')
bus3.pickup('Bob')
print(bus2.passengers)
print(bus3.passengers)
bus3.dropoff('Bob')
print(bus2.passengers)
print(bus3.passengers)
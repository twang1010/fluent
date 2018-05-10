class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pickup(self, passenger):
        self.passengers.append(passenger)

    def dropoff(self, passenger):
        self.passengers.remove(passenger)

bus1 = Bus(['Alice', 'Bob', 'Charlie', 'David'])
print(bus1.passengers)
bus1.pickup('Flora')
print(bus1.passengers)
bus1.dropoff('Bob')
print(bus1.passengers)
print(">>>>>>>>>>>>>")
bus2 = Bus()
bus3 = Bus()
bus2.pickup('Alice')
bus2.pickup('Bob')
print(bus2.passengers)
print(bus3.passengers)
bus2.dropoff('Bob')
print(bus2.passengers)
print(bus3.passengers)
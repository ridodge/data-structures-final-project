class PriorityList:
    """Create priority list from objects, priority 1, 2, 3"""
    def __init__(self):
        self.low = 1
        self.medium = 2
        self.high = 3
        self.priorities = {self.low: [], self.medium: [], self.high: []}


    def insert(self, item, priority):
        valid = [self.low, self.medium, self.high]
        if priority in valid:
            if priority == self.high:
                self.priorities[self.high].append(item)
            elif priority == self.medium:
                self.priorities[self.medium].append(item)
            else:
                self.priorities[self.low].append(item)



    def return_high(self):
        return self.priorities[self.high]


    def return_medium(self):
        return self.priorities[self.medium]

    def return_low(self):
        return self.priorities[self.low]

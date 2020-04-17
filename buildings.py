import datetime

class Building:

    def __init__(self, address, stories):
        self.address = address
        self.stories = stories
        self.designer = "Cooper Nichols"
        self.owner = ""
        self.date_constructed = ""
    
    def construct(self):
        self.date_constructed = datetime.datetime.now()
    
    def purchase(self, owner):
        self.owner = owner

    def report(self): 
        print(f'{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.')

eight_hundred_eighth = Building("800 8th Street", 12)
eight_hundred_eighth.purchase("Sofio Coopdiani")
eight_hundred_eighth.construct()
eight_hundred_eighth.report()
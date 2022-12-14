
class Map:
    map = ["********",
           "********",
           "********",
           "********",
           "********",
           "********",
           "********",
           "********"]

    def __init__(self):
        pass
    
    def render(self):
        for row in self.map:
            print(row)
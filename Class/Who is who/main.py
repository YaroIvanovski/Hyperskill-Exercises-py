
class Angel:
    def __init__(self):
        self.color = "white"
        self.feature = "wings"
        self.home = "Heaven"


class Demon:
    def __init__(self):
        self.color = "red"
        self.feature = "horns"
        self.home = "Hell"


for instance in [Angel(), Demon()]:
    print(instance.color, instance.feature, instance.home, sep='\n')
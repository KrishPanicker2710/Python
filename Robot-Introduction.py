class Robot:
    def __init__(self, name, age):
        self.name = name
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am robot.")
ai = Robot()
ai.introduce()
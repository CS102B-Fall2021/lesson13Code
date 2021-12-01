class Tamagotchi:

    def __init__(self, name, hygiene = 0, sleep = 0, intelligence = 0):
        self.name = name
        self.hygiene = hygiene
        self.sleep = sleep
        self.intelligence = intelligence
        self.__age = 1000

    def currentStatus(self):
        print("Current Status")
        happiness = self.hygiene + self.sleep + self.intelligence

        if happiness <= 0:
            print("^_^")
        elif happiness > 0 and happiness < 5:
            print("-_-")
        else:
            print("T_T")

    def bathtime(self):
        print("scrub dub dub")
        if self.hygiene > 0:
            self.hygiene -= 1
    
    def naptime(self):
        print("z z z")
        if self.sleep > 0:
            self.sleep -= 1

    def exercise(self):
        print("Go to blink")
        self.hygiene += 2
        self.sleep += 1

    def readbook(self):
        print("Go to cooper")
        self.intelligence += 1

    def gotoNYU(self):
        print("Go to NYU")
        self.intelligence -= 3

name = input("Enter your pet's name: ")
tama = Tamagotchi(name)

print(tama.name)

while True:
    print("""
    0 - print status
    1 - bath time
    2 - nap time
    3 - gym time
    4 - cooper time
    5 - nyu time
    6 - quit
    """)

    choice = input()

    print(tama.name)
    print(tama.__age)
    if choice == '0':
        tama.currentStatus()
    elif choice == '1':
        tama.bathtime()
    elif choice == '2':
        tama.naptime()
    elif choice == '3':
        tama.exercise()
    elif choice == '4':
        tama.readbook()
    elif choice == '5':
        tama.gotoNYU()
    elif choice == '6':
        break
    else:
        print("INVALID choice")

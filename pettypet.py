import random

#color
RESET, RED, GREEN, YELLOW = "\033[0m", "\033[31m", "\033[32m", "\033[33m"

class Pet:

    def __init__(self,name):
        self.name = name
        self.fullness = 60
        self.energy = 40
        self.affection = 1

    def clamp(self,attr,delta,low=0,high=100):
        setattr(self,attr,max(low,min(high, getattr(self,attr) + delta)))

    def rename(self):
        """strip to remove spaces n self.name to choose old name if user does no change."""
        self.name = input("Enter new name: ").strip() or self.name     
        print(f"{GREEN}{self.name} loves its new name!{RESET}")

    def feed(self):
        if self.fullness < 100:
            gain = random.randint(1,20)
            self.clamp("fullness", 25)  # FIXED: +25 instead of -25
            self.clamp("energy", 20)
            self.clamp("affection", gain)
            print(f"\n{self.name} is eating!\n{GREEN}Fullness: {self.fullness} | Energy: {self.energy} | Affection: +{gain}{RESET}")
        else:
            print(f"\n{RED}{self.name} is already full!{RESET}")
    
    def play(self):
        if self.energy >= 40 and self.fullness >= 60:
            gain = random.randint(10,30)
            self.clamp("energy", -20)
            self.clamp("fullness", -20)
            self.clamp("affection", gain)

            print(f"\n{self.name} played hard!\n{GREEN}Energy: {self.energy} | Fullness: {self.fullness} | Affection: +{gain}{RESET}")
        else:
            print(f"\n{RED}{self.name} is too tired or hungry to play!{RESET}")

    def sleep(self):
        if self.fullness >= 15:  # FIXED: Removed high energy requirement
            self.clamp("energy", 40)
            self.clamp("fullness", -25) # digesting food
            print(f"\n{GREEN}{self.name} is sleeping peacefully.{RESET}")
        else:
            print(f"{RED}{self.name} is too hungry to sleep!{RESET}")

    def random_event(self):
        if self.affection >= 50:
            randomeventchance = random.randint(1,100)

            if randomeventchance <= 20:
                print(f"{YELLOW}Surprise! {self.name} found a hidden treat under the couch! (+10 Affection, +10 Fullness){RESET}")
                self.clamp("affection", 10)
                self.clamp("fullness", 10)

            elif randomeventchance <= 35:
                print(f"{YELLOW}{self.name} got a burst of energy and ZOOMS around the house. (-10 Fullness){RESET}")
                self.clamp("fullness", -10)  # FIXED: -10 instead of 10

            elif randomeventchance <= 50:
                print(f"{YELLOW}{self.name} jumped onto your lap and started purring <3 (+15 Affection){RESET}")
                self.clamp("affection", 15)

#-------------User interface-------------------

print("Welcome to the pet store.")

cat_name = None

while True:
    user_pet_choice = input("Would like to get a pet (Y/N)? ").upper().strip()
    if user_pet_choice == 'Y':
        cat_name = Pet("Kitty")
        print(f"{GREEN}You took a cat home.{RESET}")
        break
    elif user_pet_choice == "N":
        print("OK. Thank you for visiting.")
        exit()  # FIXED: Exit program if user doesn't want a pet
    else:
        print(f"{RED}Please enter a valid option.{RESET}")

while True:
    cat_name.random_event()
    print("\n" + "="*30 + "\n")
    print(f"What do u do with {cat_name.name}?")
    print(f"\n{'='*30}\n{cat_name.name} | Energy: {cat_name.energy} | Fullness: {cat_name.fullness} | Affection: {cat_name.affection}")
    print("1) Rename  2) Feed  3) Play  4) Sleep  5) Leave")

    try:
        user_choice = int(input(f"{YELLOW}Your choice: {RESET}"))
    except ValueError:
        print("Enter a valid option.")
        continue

    if user_choice == 1:
        cat_name.rename()  # FIXED: Removed duplicate print statement
    elif user_choice == 2:
        cat_name.feed()
    elif user_choice == 3:
        cat_name.play()
    elif user_choice == 4:
        cat_name.sleep()
    elif user_choice == 5:
        print(f"You left {cat_name.name} alone.\n") 
        break
    else:
        print("Enter a valid option.")
        
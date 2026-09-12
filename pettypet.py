import random

#color
reset, red, green, yellow = "\033[0m", "\033[31m", "\033[32m", "\033[33m"

class Pet:
    def __init__(self,name):
        self.name = name
        self.hunger = 40
        self.energy = 40
        self.affection = 1

    def feed(self):
        print(f"{self.name} is eating!")

        self.hunger = min(100, self.hunger + 25)
        self.energy = min(100, self.energy + 20)

        print(f"{green}{self.name}'s hunger is {self.hunger}/100.")
        print(f"{self.name}'s energy is now {self.energy}/100.{reset}")

        gain = random.randint(1,20)
        self.affection = min(100, self.affection + self.affection_amount)

        print(f"{green}{self.name} grows more friendly toward you. {reset}")

    def play(self):
        if self.energy >=20 and self.hunger >=30:
            self.energy = max(100, self.energy - 20)
            self.hunger = max(100, self.hunger - 20)

            print(f"\n{self.name} played hard!\n{green}Energy:{self.energy}\tHunger:{self.hunger}{reset}")

            gain = random.randint(10,30)
            self.affection = min(100,self.affection + gain)
            print(f"{self.name} enjoys your presence.")
        else:
            print(f"\n{red}{self.name} is too tried to play!{reset}")

    def sleep(self):
        if self.energy >=30:
            print(f"\n{green}{self.name} is sleeping peacefully.{reset}")
            self.hunger = min(100, self.hunger - 30)
            self.energy = min(100, self.energy + 10)
        else:
            print(f"{red}{self.name} is too hungry to sleep!{reset}")

    def random_event(self):
        if self.affection >= 50:
            randomeventchance = random.randint(1,100)

            if randomeventchance <= 20:
                print(f"{yellow}Surprise! {self.name} found a hidden treat under the couch! (+10 Affection, -10 Hunger){reset}")
                self.affection = min(100, self.affection + 10)
                self.hunger = max(0, self.hunger - 10)

            elif randomeventchance <= 35:
                print(f"{yellow}{self.name} gota  burst of energy and ZOOMS around the house. (-10 hunger){reset}")

            elif randomeventchance <=50:
                print(f"{yellow}{self.name} jumped onto your lap and started purring<3 (+15 Affection){reset}")
                self.affection = min(100, self.affection + 15)
            else:
                return

#-------------User interface-------------------

print("Welcome to the pet store.")

while True:
    user_pet_choice = input("Would like to get a pet(Y/N)? ").upper()
    if user_pet_choice =='Y' :
        print(f"{green}You were given a cat.{reset}")
        print(f"{green}You took a cat home.{reset}")
        break
    elif user_pet_choice == "N":
        print("OK.Thank you for visiting.")
        break
    else:
        print("Please enter a valid option.")

cat_name = Pet("kitty")

while True:
    cat_name.random_event()
    print("\n" + "="*30 + "\n")
    print(f"What do u do with the {cat_name.name}?")
    print(f"\n{'='*30}\n{cat_name.name} | Energy: {cat_name.energy} | Hunger: {cat_name.hunger} | Affection: {cat_name.affection}")
    print("1) Rename  2) Feed  3) Play  4) Sleep  5) Leave")
    print(f"{yellow}Your choice: {reset}")

    try:
        user_choice = int(input(""))
    except ValueError:
        print("Enter a valid option.")
        continue

    if user_choice == 1:
        pet_name = input("Please enter the name of your cat: ")
        cat_name.name = pet_name
        print(f"{green}{cat_name.name} seems happy with its new name.{reset}")
    elif user_choice == 2:
        cat_name.feed()
    elif user_choice == 3:
        cat_name.play()
    elif user_choice == 4:
        cat_name.sleep()
    elif user_choice == 5:
        print(f"you left {cat_name.name} alone.\n") 
        break
    else:
        print("Enter a valid option.")    

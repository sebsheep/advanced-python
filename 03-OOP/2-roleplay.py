from random import randrange, choice, random
from typing import Self


class Character:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, character2: Self) -> None:
        character2.health -= self.damage

    def heal(self) -> None:
        self.health += 10

    def is_dead(self) -> bool:
        return self.health <= 0


player = Character("Évariste", 100, 7)
monster_names = [
    "Sébastien",
    "MacBook",
    "Non-Euclidean Horror",
    "Windows95",
    "Javascript",
]

score = 0


def user_choice(question, choices):
    response = input(question)
    while response not in choices:
        print("Your choice must be one of the following:")
        print(", ".join(choices) + ".")
        response = input(question)
    return response


while not player.is_dead():
    monster = Character(choice(monster_names), randrange(8, 17), randrange(15, 40))
    initial_health = monster.health

    print("*" * 42)
    print("*" + "The monster".center(40) + "*")
    print("*" + monster.name.center(40) + "*")
    print("*" + "enters the ring".center(40) + "*")
    print("*" * 42)

    while not monster.is_dead() and not player.is_dead():
        print(
            f"{monster.name} has {monster.health} health points and {monster.damage} attack points."
        )
        print(f"You have {player.health} health points.")
        print("What do you want to do?")
        response = user_choice("1) Attack \t 2) Heal :", ("1", "2"))
        if response == "1":
            player.attack(monster)
            print(f"You deal {player.damage} damage to {monster.name}.")
        else:
            player.heal()
            print("You regain 10 health points.")

        if not monster.is_dead():
            if random() < 0.9:
                print(f"{monster.name} attacks you and deals {monster.damage} damage!")
                monster.attack(player)
            else:
                print(
                    f"You get a bit of respite, {monster.name} heals and gains 10 health points."
                )
        print()

    if not player.is_dead():
        print(f"Congratulations! You defeated {monster.name}!")
        score += initial_health
        print(f"You gain {initial_health} points, you now have {score} points!")
        print("Press Enter...")
        input()

print(f"You are dead, defeated by {monster.name}.")

print("*" * 42)
print("*" + "FINAL SCORE".center(40) + "*")
print("*" + str(score).center(40) + "*")
print("*" * 42)

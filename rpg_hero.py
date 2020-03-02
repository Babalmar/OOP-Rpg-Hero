import random


class Dice:

    @staticmethod
    def k6():
        k6 = random.randint(1, 6)
        return k6

    @staticmethod
    def k8():
        k8 = random.randint(1, 8)
        return k8

    @staticmethod
    def k10():
        k10 = random.randint(1, 10)
        return k10

    @staticmethod
    def k12():
        k12 = random.randint(1, 12)
        return k12

    @staticmethod
    def k20():
        k20 = random.randint(1, 20)
        return k20


class Hero:
    def __init__(self, name, hp, attack, defence, experience, inventory):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.experience = experience
        self.inventory = inventory

    def __repr__(self):
        return 'Name: {}Hit Points: {}\nAttack: {}\nDefence: {}\nExperience points: {}\nInventory: {}'\
            .format(self.name, self.hp, self.attack, self.defence, self.experience, self.inventory)

    @staticmethod
    def name():
        names_list = []
        with open('names.txt') as f:
            for row in f:
                names_list.append(row)
        name = random.choice(names_list)
        return name


class Warrior(Hero):
    def __init__(self, name, hp, attack, defence, experience, inventory):
        super().__init__(name, hp, attack, defence, experience, inventory)

    @staticmethod
    def warcry():
        print("Raaaa!")

    # @classmethod
    # def recruit(cls):
    #    return cls()


class Wizard(Hero):
    def __init__(self, name, hp, attack, defence, experience, inventory):
        super().__init__(name, hp, attack, defence, experience, inventory)

    @staticmethod
    def chant():
        print("Ka namaa fthan Cthulhu!")


class Rogue(Hero):
    def __init__(self, name, hp, attack, defence, experience, inventory):
        super().__init__(name, hp, attack, defence, experience, inventory)

    @staticmethod
    def sneak():
        print("...")


hero1 = Warrior(Hero.name(), Dice.k20(), Dice.k12(), Dice.k10(), 10000, {'sword', 'leather sandals'})
hero2 = Wizard(Hero.name(), Dice.k10(), Dice.k6(), Dice.k8(), 11000, {'staff +1', 'robe'})
hero3 = Rogue(Hero.name(), Dice.k12(), Dice.k8(), Dice.k10(), 12000, {'blackjack', 'bow'})

hero1.warcry()
hero2.chant()
hero3.sneak()

print(hero1)
print(hero2)
print(hero3)
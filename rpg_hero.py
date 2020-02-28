class Hero:
    def __init__(self, name, hp, attack, defence, experience, inventory):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.experience = experience
        self.inventory = inventory


class Warrior(Hero):
    def __init__(self, name, basic_class, hp, attack, defence, experience, inventory):
        super().__init__(name, hp, attack, defence, experience, inventory)
        self.basic_class = basic_class

    def __repr__(self):
        return 'Name: {}\nClass: {}\nHit Points: {}\nAttack: {}\nDefence: {}\nExperience points: {}\nInventory: {}'\
            .format(self.name, self.basic_class, self.hp, self.attack, self.defence, self.experience, self.inventory)

    @staticmethod
    def warcry():
        print("Raaaa!")


class Wizard(Hero):
    def __init__(self, name, basic_class, hp, attack, defence, experience, inventory):
        super().__init__(name, hp, attack, defence, experience, inventory)
        self.basic_class = basic_class

    def __repr__(self):
        return 'Name: {}\nClass: {}\nHit Points: {}\nAttack: {}\nDefence: {}\nExperience points: {}\nInventory: {}' \
            .format(self.name, self.basic_class, self.hp, self.attack, self.defence, self.experience, self.inventory)

    @staticmethod
    def chant():
        print("Ka namaa fthan Cthulhu!")


class Rogue(Hero):
    def __init__(self, name, basic_class, hp, attack, defence, experience, inventory):
        super().__init__(name, hp, attack, defence, experience, inventory)
        self.basic_class = basic_class

    def __repr__(self):
        return 'Name: {}\nClass: {}\nHit Points: {}\nAttack: {}\nDefence: {}\nExperience points: {}\nInventory: {}' \
            .format(self.name, self.basic_class, self.hp, self.attack, self.defence, self.experience, self.inventory)


hero1 = Warrior('Conan', 'Warrior', 30, 20, 15, 10000, {'sword', 'leather sandals'})
hero2 = Wizard('Amarok', 'Wizard', 20, 14, 10, 11000, {'staff +1', 'robe'})

hero1.warcry()
hero2.chant()


print(hero1)
print(hero2)
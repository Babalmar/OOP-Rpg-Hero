class Hero:
    def __init__(self, name, hp, attack, defence, experience, inventory):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.experience = experience
        self.inventory = inventory


class Warrior(Hero):
    def __init__(self, name, hp, attack, defence, experience, inventory):
        super().__init__(name, hp, attack, defence, experience, inventory)


class Mage(Hero):
    pass


class Thief(Hero):
    pass


hero1 = Warrior('Conan', 30, 20, 15, 10000, {'sword', 'leather sandals'})
print('Name: {}'.format(hero1.name))
print('Attack: {}'.format(hero1.attack))
print('Defence: {}'.format(hero1.defence))
print('Inventory: {}'.format(hero1.inventory))
print('Experience points: {}'.format(hero1.experience))
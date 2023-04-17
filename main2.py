import random
from typing import Any


# класс мечник для получения аттрибутов
class Swordman:
    name: str
    strength: int
    agility: int

    def __init__(self):
        self.name = "swordman"
        self.strength = 10
        self.agility = 5


# класс лучник для получения аттрибутов
class Archer:
    name: str
    strength: int
    agility: int

    def __init__(self):
        self.name = "archer"
        self.strength = 5
        self.agility = 10


# добавление объектов классов в лист
def registration():
    swordman = Swordman()
    archer = Archer()
    classes = list()
    classes.append(swordman)
    classes.append(archer)
    return classes


# класс игрока с его характеристиками и взаимодействия с игроком (взаимодействия с игроком в плане методы взаимодействия? или кто взаимодействует?)
class Player:
    player_id: int
    role: str
    base_strength: int = 0
    base_agility: int = 0
    strength: int = 1
    agility: int = 1
    damage: int = 1
    hp: int
    critical_chance: float
    critical_damage: float
    armor: int
    chance_of_evasion: float
    attack_speed: float
    inventory: list
    lvl: int = 1
    experience: int = 350
    remaining_experience: int
    gold: int

    # метод для назначения класса  и начальных аттрибутов пользователю
    def get_role_and_atributes(self, player):
        status = True
        choose = gameplay.choose_class(player)
        classes = registration()
        # try:
        for game_class in classes:
            if choose == game_class.name:
                player.role = game_class.name
                player.base_strength = game_class.strength
                player.base_agility = game_class.agility
                status = True
                break
            else:
                status = False
        if not status:
            print("Ввод не верный, попробуй еще раз")
            self.get_role_and_atributes(player)

    # метод для повышения уровня
    def lvl_up(self, player):
        a = gameplay.lvl_check()
        self.lvl += 1
        self.experience = self.experience - a
        self.get_stats()


    # метод для получения и повышения характеристик
    def get_stats(self):
        self.strength = self.base_strength + self.lvl * 5
        self.agility = self.base_agility + self.lvl * 5
        self.strength = self.base_strength + self.lvl * 3
        self.agility = self.base_agility + self.lvl * 2
        self.hp = self.strength * 15
        self.damage = self.strength * 2
        self.critical_chance = self.strength * 0.005
        if self.critical_chance > 0.2:
            self.critical_chance = 0.2
        self.critical_damage = self.strength * self.agility * 0.002
        self.armor = int(self.agility * 0.15)
        self.chance_of_evasion = self.agility * 0.005
        if self.chance_of_evasion > 0.3:
            self.chance_of_evasion = 0.3
        self.attack_speed = 1 + self.agility * 0.005


# Класс для всех предметов
class Item:
    id: int
    cost: int
    rarety: int


# Класс для всех защитных предметов
class Armor(Item):
    armor: int
    hp: int
    chance_of_evasion: float


# класс для создания предмета helmet
class Helmet(Armor):
    def __init__(self):
        self.id = 1
        self.hp = 100
        self.armor = 2


class Location:
    id: int
    needed_lvl: int
    mob_list: list
    drop_list: list

    def generate_enemy(self):
        pass


class Forest(Location):
    def __init__(self):
        self.name = "Лес"
        self.id = 1
        self.needed_lvl = 1

    def get_mob_list(self):
        self.mob_list = list()
        self.mob_list.append(zombie_enemy)
        return self.mob_list


class Cave(Location):
    def __init__(self):
        self.name = "пещера"
        self.id = 2
        self.needed_lvl = 2


def get_location_list():
    locations = list()
    locations.append(forest)
    locations.append(cave)
    return locations


class mob:
    mob_name: str
    base_strength: int = 1
    base_agility: int = 2
    strength: int
    agility: int
    damage: int
    hp: int
    critical_chance: float
    critical_damage: float
    armor: int
    chance_of_evasion: float
    attack_speed: float
    lvl: int
    gold: int


class Zombie(mob):

    def __init__(self):
        self.mob_name = "zombie"

    def get_lvl(self):
        self.lvl = random.randint(gamer.lvl-2, gamer.lvl+2)
        if self.lvl <= 0:
            self.lvl = 1

    def get_stats(self):
        self.strength = self.base_strength + self.lvl * 3
        self.agility = self.base_agility + self.lvl * 2
        self.hp = self.strength * 15
        self.damage = self.strength * 5
        self.critical_chance = self.strength * 0.005
        if self.critical_chance > 0.2:
            self.critical_chance = 0.2
        self.critical_damage = self.damage * (self.strength * self.agility * 0.002)
        self.armor = int(self.agility * 0.15)
        self.chance_of_evasion = self.agility * 0.005
        if self.chance_of_evasion > 0.3:
            self.chance_of_evasion = 0.3
        self.attack_speed = 1 + self.agility * 0.005


# класс для всех игровых методов
class Gameplay:

    # выбор пользователем класса
    def choose_class(self, player):
        choose = input("Выберите класс: swordman или archer\n")
        return choose

    # Проверка достижения уровня

    def lvl_check(self):
        needed_experience = 100 * gamer.lvl + 100 * ((gamer.lvl - 1) ** 2)
        gamer.remaining_experience = needed_experience - gamer.experience
        if gamer.experience >= needed_experience:
            gamer.lvl_up(gamer)
            return needed_experience


    def show_stats(self):
        self.lvl_check()
        print(" Уровень - ", gamer.lvl, "\n",
              "Опыт - ", gamer.experience,"\n" ,"Опыт для повышения уровня -  ", gamer.remaining_experience,  "\n",
              "Сила - ", gamer.strength, "\n",
              "Ловкость - ", gamer.agility, "\n",
              "Урон - ", gamer.damage, "\n",
              "Хп - ", gamer.hp, "\n",
              "Шанс крит урона - ", round(gamer.critical_chance * 100, 2), "%\n",
              "Крит урона - ", gamer.critical_damage * 1000, "%\n",
              "Броня - ", gamer.armor, "\n",
              "Шанс уклонения - ", round(gamer.chance_of_evasion * 100, 2), "%\n",
              "Скорость атаки - ", gamer.attack_speed, "\n",
              )

    def menu(self, locations):
        a = int(input("1-показать стату 2-инвентарь 3-доступные локации \n"))
        if a == 1:
            gameplay.show_stats()
        elif a == 3:
            locations = get_location_list()
            for location in locations:
                if gamer.lvl >= location.needed_lvl:
                    print(location.name)


gamer = Player()
gameplay = Gameplay()
helmet = Helmet()
forest = Forest()
cave = Cave()
zombie_enemy = Zombie()

# d
# print(gamer.strength, gamer.agility, gamer.damage, gamer.hp, gamer.critical_damage, gamer.armor)
get_location_list()
# zombie_enemy.get_lvl()
# zombie_enemy.get_stats()
# print(zombie_enemy.lvl, zombie_enemy.strength, zombie_enemy.agility)
# forest.get_mob_list()
gamer.get_role_and_atributes(gamer)
gamer.get_stats()
gameplay.menu(gamer)



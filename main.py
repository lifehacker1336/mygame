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


# добавление объектов класса в лист
def registration():
    swordman = Swordman()
    archer = Archer()
    classes = list()
    classes.append(swordman)
    classes.append(archer)
    return classes


# класс игрока с его характеристиками и взаимодействия с игроком
class Player:
    player_id: int
    role: str
    base_strength: int = 0
    base_agility: int = 0
    strength: int
    agility: int
    damage: int
    hp: int
    critical_chance: float
    critical_damage: float
    armor: int
    chance_of_evasion: float
    attack_speed: float
    inventory: list
    lvl: int = 1
    experience: int = 0
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
        gamer.lvl += gamer.lvl
        gamer.experience = 0
        self.get_stats()

    # метод для получения и повышения характеристик
    def get_stats(self):
        gamer.strength = gamer.base_strength+gamer.lvl*5
        gamer.agility = gamer.base_agility+gamer.lvl*5


# Класс для всех предметов
class Item:
    id: int
    cost: int
    rarety: int

    def a(self):
        pass

# Класс для всех защитных предметов
class Armor(Item):
    armor: int
    strength: 1
    hp: int
    chance_of_evasion: float

    # Добавление всех предметов в лист
    def get_armor_list(self):
        armor_list = list()
        armor_list.append(helmet.id)
        print(armor_list)



# класс для создания предмета helmet
class Helmet(Armor):

    def __init__(self):
        helmet.id = 1
        helmet.hp = 100


# класс для всех игровых методов
class Gameplay:

    # выбор пользователем класса
    def choose_class(self, player):
        choose = input("Выберите класс: swordman или archer\n")
        return choose

    # Проверка достижения уровня
    def lvl_check(self):
        needed_experience = 100*gamer.lvl + 100*(gamer.lvl-1)**2
        if gamer.experience >= needed_experience:
            gamer.lvl_up(gamer)
        else:
            pass


gamer = Player()
gameplay = Gameplay()
helmet = Helmet()
# gamer.get_role_and_atributes(gamer)
# gameplay.lvl_check()
# print(gamer.role, gamer.base_strength, gamer.base_agility)

helmet.get_armor_list()


class Swordman:
    name: str
    strength: int
    agility: int

    def __init__(self):
        self.name = "swordman"
        self.strength = 10
        self.agility = 5


class Archer:
    name: str
    strength: int
    agility: int

    def __init__(self):
        self.name = "archer"
        self.strength = 5
        self.agility = 10


def registration():
    swordman = Swordman()
    archer = Archer()
    classes = list()
    classes.append(swordman)
    classes.append(archer)
    return classes


class Gameplay:

    def choose_class(self, player):
        choose = input("Выберите класс: swordman или archer\n")
        return choose

    # def choose_class(self):    #     self.choose = input("Выберите класс: swordman или archer\n")    #     player.get_role()    #     return gameplay.choose


class Player:
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

    def lvl_up(self, player):  # переделать эту хуйню
         pass



gamer = Player()
gameplay = Gameplay()
gamer.get_role_and_atributes(gamer)
print(gamer.role, gamer.base_strength, gamer.base_agility)


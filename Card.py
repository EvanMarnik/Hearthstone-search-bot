from asyncio.windows_events import NULL
import enum
class Card:
    name: str = None
    manaCost: int = None
    text: str = None
    image: str = None
    collectible: bool = None

    def __init__(self, json: dict):
        self.name = json["name"]
        self.manaCost = json["manaCost"]
        self.text = json["text"]
        self.image = json["image"]
        self.collectible = json["collectible"] == 1

class MinionCard(Card):
    health: int = None
    type: str = None
    def __init__(self, json: dict):
        Card.__init__(self, json=json)
        self.health = json["health"]
        self.attack = json["attack"]
        if "minionType" in json:
            type = json["minionType"]


class SpellCard(Card):
    school: str = None
    def __init__(self, json: dict):
        Card.__init__(self, json=json)
        if "spellSchoolId" in json:
            school = json["spellSchoolId"]


class WeaponCard(Card):
    durability: int = None
    attack: int = None
    def __init__(self, json: dict):
        Card.__init__(self, json=json)
        self.attack = json["attack"]
        self.durability = json["durability"]



class HeroCard(Card):
    armor: int = None
    def __init__(self, json: dict):
        Card.__init__(self, json=json)
        self.armor = json["armor"]

class spellSchool(enum.Enum):
    ARCANE = 1
    FIRE = 2
    FROST = 3
    NATURE = 4
    HOLY = 5
    SHADOW = 6
    FEL = 7

class minionType(enum.Enum):
    BEAST = 20
    DRAGON = 24
    MURLOC = 14
    PIRATE = 23
    ELEMENTAL = 18
    NAGA = 92
    QUILBOAR = 43
    DEMON = 15
    MECH = 17
    TOTEM = 21
    ALL = 26

class rarity(enum.Enum):
    BASIC = 1
    COMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5
    NONE = NULL
    
class cardClass(enum.Enum):
    DEMON_HUNTER = 14
    DRUID = 2
    HUNTER = 3
    MAGE = 4
    PALADIN = 5
    PRIEST = 6
    ROGUE = 7
    SHAMAN = 8
    WARLOCK = 9
    WARRIOR = 10
    NEUTRAL = 12
    DEATH_KNIGHT = 1
    DREAM = 11

def json_to_cards(json: dict) -> list[Card]:
    cards: list[Card] = []
    for card_json in json["cards"]:
        if card_json["cardTypeId"] == 4:
            cards.append(MinionCard(json = card_json))
        elif card_json["cardTypeId"] == 7: 
            cards.append(WeaponCard(json = card_json))
        elif card_json["cardTypeId"] == 3:
            cards.append(HeroCard(json = card_json))
        elif card_json["cardTypeId"] == 5:
            cards.append(SpellCard(json = card_json))
        else:
            cards.append(Card(json = card_json))

    return cards
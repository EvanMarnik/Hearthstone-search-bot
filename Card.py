import enum
class spellSchool(enum.Enum):
    Arcane = 1
    Fire = 2
    Frost = 3
    Nature = 4
    Holy = 5
    Shadow = 6
    Fel = 7
    def __str__(self):
        return self.name

class minionType(enum.Enum):
    Beast = 20
    Dragon= 24
    Murloc = 14
    Pirate = 23
    Elemental = 18
    Naga = 92
    Quilboar = 43
    Demon = 15
    Mech = 17
    Totem = 21
    All = 26
    def __str__(self):
        return self.name

class rarity(enum.Enum):
    Basic = 2
    Common = 1
    Rare = 3
    Epic = 4
    Legendary = 5
    NONE = None
    def __str__(self):
        return self.name
    
class cardClass(enum.Enum):
    Demon_Hunter = 14
    Druid = 2
    Hunter = 3
    Mage = 4
    Paladin = 5
    Priest= 6
    Rogue = 7
    Shaman = 8
    Warlock = 9
    Warrior = 10
    Neutral = 12
    Death_Knight = 1
    Dream = 11
    def __str__(self):
        return self.name

class Card:
    name: str = None
    manaCost: int = None
    text: str = None
    image: str = None
    collectible: bool = None
    card_class: cardClass = None
    card_rarity: rarity = None
    def __init__(self, json: dict):
        self.name = json["name"]
        self.manaCost = json["manaCost"]
        self.text = json["text"]
        self.image = json["image"]
        self.collectible = json["collectible"] == 1
        self.card_class = cardClass(json["classId"])
        self.card_rarity = rarity(json["rarityId"])

class MinionCard(Card):
    health: int = None
    type: str = None
    def __init__(self, json: dict):
        Card.__init__(self, json=json)
        self.health = json["health"]
        self.attack = json["attack"]
        if "minionType" in json:
            s = json["minionType"]
            self.type = minionType(s)


class SpellCard(Card):
    school: spellSchool = None
    def __init__(self, json: dict):
        Card.__init__(self, json=json)
        if "spellSchoolId" in json:
            s = json["spellSchoolId"]
            self.school = spellSchool(s)

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
        if "armor" in json:
            self.armor = json["armor"] #have to do this since the literal heroes are
                                        #treated as hero 'cards' but dont have armor

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
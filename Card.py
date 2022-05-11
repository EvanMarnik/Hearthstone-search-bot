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


def json_to_cards(json: dict) -> list[Card]:
    cards: list[Card] = []
    for card_json in json["cards"]:
        if card_json["cardTypeId"] == 4:
            cards.append(MinionCard(json = card_json))
        else:
            cards.append(Card(json = card_json))

    return cards
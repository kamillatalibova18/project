'''
•	id(int)
•	название(text)
•	тип(text)
•	имя клиента(text)
•	дата рождения(int)
•	пол(text)
•	стоимость(int)

'''

class Club_card:
    """

    """
    def __init__(self, club_card_id: int, name: str, card_type: str, client_name: str, data: str, gender: str, price: int):
        """ """
        self.club_card_id = club_card_id
        self.name = name
        self.card_type = card_type
        self.client_name = client_name
        self.data = data
        self.gender = gender
        self.price = price
    def __str__(self):
        return f"{self.club_card_id}. {self.name} {self.card_type} {self.client_name} {self.data} {self.gender} {self.price}"
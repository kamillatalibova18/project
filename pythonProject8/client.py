'''
•	Id(int)
•	Имя(text)
•	дата рождения(int)
•	пол(text)
•	логин(text)
•	пароль(int)
•	номер телефона(int)

'''

class Client:
    """

    """
    def __init__(self, client_id: int, name: str, data: int, gender: str, login: str, password: int, number_phone: int):
        """ """
        self.client_id = client_id
        self.name = name
        self.data = data
        self.gender = gender
        self.login = login
        self.password = password
        self.number_phone = number_phone
    def __str__(self):
        return f"{self.client_id}. {self.name} {self.data} {self.gender} {self.login} {self.password} {self.number_phone}"
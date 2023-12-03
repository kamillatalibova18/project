from client import Client
from club_card import Club_card
from payments import Payments


class Fitness:


    def __init__(self, fitness_id: int):
        """ """
        self.fitness_id = fitness_id
        self.clients = []
        self.club_card = []
        self.payments = []

    def add_client(self, client: Client):
        """добавляем клиента в список """
        self.clients.append(client)

    def add_club_card(self, club_card: Club_card):
        """добавляем клубную карту в список """
        self.club_card.append(club_card)

    def add_payments(self, payments: Payments):
        """ добавляем платежи в спсиок"""
        self.payments.append(payments)

    def __str__(self):
        fitness_info = f"Fitness ID: {self.fitness_id}\n\n"

        fitness_info += "Club_card:\n"
        for club_card in self.club_cards:
            fitness_info += f"{club_card}\n"

        fitness_info += "Clients:\n"
        for client in self.clients:
            fitness_info += f"{client}\n"

        fitness_info += "Payments:\n"
        for payment in self.payments:
            fitness_info += f"{payment}\n"

        return f"{self.clients} {self.payments} {self.club_cards}"



    def read_club_cards(self, club_cards_fname):
        with open(club_cards_fname, "r", encoding="utf-8") as club_cards_f:
            for line in club_cards_f:
                values = line.split(";")
                print(line)
            if len(values) == 7:
                club_card_id, name, card_type, client_name, gender, data, price = line.split(";")
                club_card_id = int(club_card_id)
                name = str(name)
                card_type = str(card_type)
                client_name = str(client_name)
                gender = str(gender)
                data = str(data)
                price = int(price)

                club_card = Club_card(club_card_id, name, card_type, client_name, gender, data, price)
                self.club_card.append(club_card)

    def read_clients(self, clients_fname):
        with open(clients_fname, 'r', encoding="utf-8") as clients_f:
            for line in clients_f:
                values = line.split(";")
                print(line)
            if len(values) == 7:
                client_id, name, data, gender, login, password, number_phone = line.split(";")
                client_id = int(client_id)
                name = str(name)
                data = str(data)
                gender = str(gender)
                login = str(login)
                password = int(password)
                number_phone = int(number_phone)
                client = Client(client_id, name, data, gender, login, password, number_phone)
                self.clients.append(client)






if __name__ == '__main__':
    fitness = Fitness(1)
    fitness.read_clients("client.txt")
    fitness.read_club_cards("club_card.txt")

    for client in fitness.clients:
        for club_card in fitness.club_card:
            if club_card.client_name == client.name:
                print(f"{client.name} - {club_card.card_type}")






"""
•	id(int)
•	номер телефона клиента(int)
•	ФИО клиента(text)
•	Email(text)
•	Пол(text)
•	Дата рождения(int)
•	есть ли опыт в занятии фитнес-клуба(text)
•	оплата(частями, рассрочку, полностью)(text)
•	номер карты(int)


"""
class Payments:
    """

    """
    def __init__(self, payments_id: int, number_phone_client: int, full_name_client: str, email: str, gender: str, data: int, experience_lesson: str, payment: str, card_number: int):
        """ """
        self.payments_id = payments_id
        self.number_phone_client = number_phone_client
        self.full_name_client = full_name_client
        self.email = email
        self.gender = gender
        self.data = data
        self.experience_lesson = experience_lesson
        self.payment = payment
        self.card_number = card_number
    def __str__(self):
        return f"{self.payments_id}. {self.number_phone_client} {self.full_name_client} {self.email} {self.gender} {self.data} {self.experience_lesson} {self.payment} {self.card_number}"
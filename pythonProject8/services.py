"""
•	id(int)
•	тип услуги(text)
•	дата начала(int)
•	дата окончания(int)
•	цена(money)

"""
class Services:
    """

    """
    def __init__(self, services_id: int, type: str, data_start: str, data_over: int, price: int):
        """ """
        self.services_id = services_id
        self.type = type
        self.data_start = data_start
        self.data_over = data_over
        self.price = price
    def __str__(self):
        return f"{self.services_id}. {self.type} {self.data_start} {self.data_over} {self.price}"
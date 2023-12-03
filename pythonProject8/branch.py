"""
•	id(int)
•	название(text)
•	адрес(text)

"""

class Branc:
    """

    """
    def __init__(self, branch_id: int, name: str, address: str):
        """ """
        self.branch_id = branch_id
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.branch_id}. {self.name} {self.address}"
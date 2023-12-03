"""
•	id(int)
•	название(text)
•	вид(text)
•	длительность(int)
•	уровень сложности(int)
•	наименование абонемента(text)

"""
class Training:
    """

    """
    def __init__(self, training_id: int, name: str, view: str, duration: int, difficultly_level: int, name_sub: str):
        """ """
        self.training_id = training_id
        self.name = name
        self.view = view
        self.duration = duration
        self.difficultly_level = difficultly_level
        self.name_sub = name_sub

    def __str__(self):
        return f"{self.training_id}. {self.name} {self.view} {self.duration} {self.difficultly_level} {self.name_sub}"


class LogicalToken:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.bool = None

    def __str__(self):
        return f'{self.type}:{self.value},{self.bool}'
    
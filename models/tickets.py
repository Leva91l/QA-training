import random


class Tickets:
    EXAM_TICKETS = {
        'math': 'tickets/math',
        'biology': 'tickets/biology',
        'russian': 'tickets/russian',
    }

    def __init__(self, subject):
        self.number = 1
        self.subject = subject

    def __iter__(self):
        return self

    def __next__(self):
        try:
            with open(f'{self.EXAM_TICKETS[str(self.subject)]}', 'r') as f:
                lines = f.readlines()
                index = random.randint(0, len(lines) - 1)
                yield lines[index][:-1]
        except FileNotFoundError:
            raise ValueError(f'{self.subject} not found.')

    def __repr__(self):
        return self.number

    def __str__(self):
        return self.number

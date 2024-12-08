class Subject:

    def __init__(self, title, payment_per_hour, total_hours):
        self.title = title
        self.payment_per_hour = payment_per_hour
        self.total_hours = total_hours

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

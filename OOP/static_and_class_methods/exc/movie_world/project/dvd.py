import calendar
class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.age_restriction = age_restriction
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.id = id
        self.name = name
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        return cls(name, id, int(date.split(".")[2]), calendar.month_name[(int(date.split(".")[1]))], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
        
        
        
        
        
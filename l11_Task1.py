class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"

    @staticmethod
    def validate_date(obj):
        try:
            if (obj.day > 31 or obj.day < 1 or obj.day > 29 and obj.month == 2
                    or obj.day > 30 and obj.month in (4, 6, 9, 11) or obj.day > 28 and obj.year % 4 > 0):
                raise MyErr(f'Day {obj.day} is incorrect in date {obj.day}-{obj.month}-{obj.year}')
            if obj.month > 12 or obj.day < 1:
                raise MyErr(f"Month {obj.month} is incorrect in date {obj.day}-{obj.month}-{obj.year}")
            if obj.year > 3000 or obj.year < 1:
                raise MyErr(f"Year {obj.year} is incorrect")
        except MyErr as err:
            print(err)
            return False
        else:
            return True

    @classmethod
    def set_date(cls, date_str):
        try:
            a = list(map(int, date_str.split('-')))
        except ValueError as err:
            return err
        d, m, y = a
        if Date.validate_date(cls(d, m, y)):
            return cls(d, m, y)


date_1 = Date.set_date('29-2-2021')
print(date_1)

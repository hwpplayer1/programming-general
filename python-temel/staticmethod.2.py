class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def disp(self):
        print('{}/{}/{}'.format(self.day, self.month, self.year))

    @staticmethod
    def isLeapYear(year):
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

date = Date(10, 12, 2007)

date.disp()                            # örnek metodun çağrılması için asıl biçim
Date.disp(date)                        # örnek metodun çağrılması için alternatif biçim
result = Date.isLeapYear(2000)         # static metodun çağrılması için asıl biçim
print('Artık' if result else 'Artık değil')

result = date.isLeapYear(2000)         # static metodun çağrılması için alternatif biçim
print('Artık' if result else 'Artık değil')

from pyluach import dates
import datetime


class LuachSfirah:

    count = 0

    def __init__(self, count):
        self.count = count
        self.view_sfirah()

    today = dates.HebrewDate.today()

    now = datetime.datetime.today()
    print(now.hour, now.minute)

    SINGLE_NUMBERS = ['', 'אחד', 'שנים', 'שלשה', 'ארבעה', 'חמשה', 'ששה', 'שבעה', 'שמונה', 'תשעה']

    DOZENS_NUMBERS = ['', ' עשר', ' ועשרים', ' ושלשים', ' וארבעים', ' וחמישים']

    TODAY = 'היום '

    TO_OMER = 'לעומר'

    THAT_IS = 'שהם '

    def day_or_days(self, days=0):
        if days == 0:
            days = self.count
        return ' ימים ' if days <= 10 else ' יום '

    def week_or_weeks(self):
        return ' שבועות ' if self.count >= 14 else ' שבוע '

    def get_days(self):
        single_number = self.SINGLE_NUMBERS[self.count % 10]
        dozens_number = self.DOZENS_NUMBERS[self.count // 10]
        return single_number + dozens_number

    def get_days_of_week(self):
        return self.SINGLE_NUMBERS[self.count % 7]

    @staticmethod
    def fix_spelling_errors(string):
        return string.replace('אחד ימים', 'יום אחד')\
            .replace('אחד שבוע', 'שבוע אחד')\
            .replace('שנים ימים', 'שני ימים')\
            .replace('שנים שבועות', 'שני שבועות')\
            .replace('  עשר', ' עשרה')\
            .replace('  ו', ' ')

    def get_weeks_and_days_in_week(self):
        p1 = self.THAT_IS + self.get_weeks() + self.week_or_weeks()
        p2 = ('ו' + self.get_days_of_week() + self.day_or_days(5)).replace('ואחד ימים', 'ויום אחד')
        if self.count < 7:
            return ''
        if self.count % 7 == 0:
            return p1
        return p1 + p2

    def get_weeks(self):
        return self.SINGLE_NUMBERS[self.count // 7]

    @staticmethod
    def find_sfirah_today():
        today = LuachSfirah.today
        now = LuachSfirah.now
        if (now.hour >= 19 and now.minute > 28) or now.hour >= 20:
            today = today + 1
        if today.month == 1:
            return today.day - 15
        if today.month == 2:
            return today.day + 15
        if today.month == 3:
            return today.day + 44
        return 0

    def view_sfirah(self):
        if self.count > 49 or self.count < 1:
            print('היום אין אומרים ספירת העומר כלל וכלל!')
            return
        p1 = self.TODAY + self.get_days() + self.day_or_days()
        p2 = self.get_weeks_and_days_in_week() + self.TO_OMER
        print(self.fix_spelling_errors(p1 + p2))


if __name__ == '__main__':
    print('\033[1m', '               לוח ספירת העומר', '\033[0m')
    while True:
        print('\033[95m')
        count_day = input('הכנס את מספר הספירה של יום מסויים ותקבל את נוסח הספירה של אותו יום\n או לחילופין לחץ Enter ותקבל את הספירה של היום.\n____')
        print('\033[0m')
        if count_day == '':
                day = LuachSfirah(LuachSfirah.find_sfirah_today())
                continue
        if count_day.isnumeric():
            day = LuachSfirah(int(count_day))
        print('\n')

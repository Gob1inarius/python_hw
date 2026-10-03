class Solution(object):
    def dayOfYear(self, date):
        year, month, day = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days[1] = 29
        return sum(days[:month - 1]) + day
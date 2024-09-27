import random


# класс который выдаёт рандомное значение на серии промежутков
class RAND:
    @staticmethod
    def random_in_range_x(ranges):
        range_choice = random.choice(ranges)
        return random.randint(range_choice[0], range_choice[1])

    @staticmethod
    def random_in_range_y(ranges):
        range_choice = random.choice(ranges)
        return random.randint(range_choice[0], range_choice[1])

    @staticmethod
    def is_in_ranges(num, ranges):
        for start, end in ranges:
            if start <= num <= end:
                return True
            else:
                return False

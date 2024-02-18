class Person:
    def __init__(self, last_name, first_name, zodiac_sign, birth_date):
        self.last_name = last_name
        self.first_name = first_name
        self.zodiac_sign = zodiac_sign
        self.birth_date = birth_date

def sort_people_by_birth_date(people_list):
    return sorted(people_list, key=lambda x: x.birth_date)

def display_people_with_zodiac_sign(people_list, zodiac_sign):
    found = False
    print(f"Люди с таким знаком зодиака '{zodiac_sign}':")
    for person in people_list:
        if person.zodiac_sign == zodiac_sign:
            print(f"{person.last_name} {person.first_name} - Дата рождения: {person.birth_date[0]}.{person.birth_date[1]}.{person.birth_date[2]}")
            found = True
    if not found:
        print(f"Нет людей с таким знаком зодиака '{zodiac_sign}'.")
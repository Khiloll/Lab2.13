#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .zodiac_package.people_module import Person, sort_people_by_birth_date, display_people_with_zodiac_sign

# Создание списка людей
people = [
    Person("Кенесбаев", "Хилол", "Козерог", [2002, 12, 28]),
    Person("Магдаев", "Даламбек", "Стрелец", [2004, 12, 14]),
    Person("Кулешов", "Олег", "Дева", [2003, 8, 26])
]

# Пользовательский ввод
searched_zodiac_sign = input("Введите знак зодиака: ")

# Сортировка людей по дате рождения
sorted_people = sort_people_by_birth_date(people)

# Вывод информации о людях с заданным знаком Зодиака
display_people_with_zodiac_sign(sorted_people, searched_zodiac_sign)
"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих
странах. Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы,
которая считывает название города и выводит на печать страну.

"""


def country_city(city_1):
    list_of_countries = {
        "Belarus": ["Minsk", "Pinsk", "Brest"],
        "Ukraine": ["Kiev", "Lvov", "Chernigov"],
        "Germany": ["Berlin", "Hamburg", "Frankfurt"]
    }
    for key, value in list_of_countries.items():
        if city_1 in value:
            print(key)


def main():

    city_1 = input("Enter a city: ")
    country_city(city_1)


if __name__ == '__main__':
    main()
import csv


def read_print_note():
    with open('uk_film_lib.csv') as f:
        print(f.read())


def add_note():
    with open('uk_film_lib.csv', 'a') as f:
        new_note = input().split(",")
        writer = csv.writer(f)
        writer.writerow(new_note)


def film_highest_rating():
    with open('uk_film_lib.csv') as f:
        dict_film_lib = csv.DictReader(f)

        highest_rating = 0
        film__highest__rating = ""
        for row in dict_film_lib:
            if int(row[' rating']) > highest_rating:
                highest_rating = int(row[' rating'])
                film__highest__rating = row['film_name']
    return film__highest__rating


print(film_highest_rating())


def film_lowest_rating():
    with open('uk_film_lib.csv') as f:
        dict_film_lib = csv.DictReader(f)
        lowest_rating = 6
        film__lowest__rating = ""
        for row in dict_film_lib:
            if int(row[' rating']) < lowest_rating:
                lowest_rating = int(row[' rating'])
                film__lowest__rating = row['film_name']
    return film__lowest__rating


print(film_lowest_rating())


def average_rating():
    with open ('uk_film_lib.csv') as f:
        dict_film_lib = csv.DictReader(f)
        sum_rating = 0
        count_films = 0
        for row in dict_film_lib:
            sum_rating += int(row[' rating'])
            count_films += 1
    return round(sum_rating/count_films, 2)


print(average_rating())





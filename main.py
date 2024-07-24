# This is a sample Python script.
import csv
import json
import struct
from typing import List, Dict, Any

FILE_JSON = "users.json"
FILE_CSV = "books.csv"


def read_from_csv(name_of_file: str):
    with open(name_of_file, newline="\n") as csvfile:
        reader = csv.reader(csvfile)
        list_book = list()
        for row in reader:
            list_book.append(dict({'title': row[0], 'author': row[1], 'pages': row[3], 'genre': row[2]}))
        list_book.pop(0)
        return list_book


def read_from_json(name_of_file: str):
    with open(name_of_file) as jsfile:
        list_user = list()
        file_content = jsfile.read()
        templates = json.loads(file_content)
        for temp in templates:
            list_user.append(dict({'name': temp.get('name'), 'gender': temp.get('gender'),
                                   'address': temp.get('address'), 'age': temp.get('age')}))
        return list_user


def write_to_json(dictionary, name_of_file):
    with open(name_of_file, 'w') as file:
        json.dump(dictionary, file, indent=2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_users = read_from_json(FILE_JSON)
    amount_of_users = len(list_users)
    list_books = read_from_csv(FILE_CSV)
    amount_of_books = len(list_books)
    result_reference = dict()
    full_result: list[dict[Any, Any]] = list()
    index_user = 0
    for user in list_users:
        books_for_user = list()
        index_book = index_user
        while index_book < amount_of_books:
            books_for_user.append(list_books[index_book])
            index_book += amount_of_users
        result_reference["books"] = books_for_user
        index_user += 1
        full_result.append({**user, **result_reference})

    write_to_json(full_result, "reference.json")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

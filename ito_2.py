group_28 = [
    ['Данила', 5, 4, 3, 4, 2],
    ['Илья', 2, 3, 3, 4, 5, 5, 5],
    ['Георгий', 5, 5, 4, 5, 3, 4],
    ['Соня', 4, 4, 3, 5, 5, 3, 5],
    ['Никита', 4, 3, 5, 3, 4, 4],
    ['Влад', 4, 3, 4, 5, 3]
]


def show_student(student_record):
    print(student_record[0], student_record[1:])


for record in group_28:
    show_student(record)


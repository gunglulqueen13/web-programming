groupmates = [
    {
        "name": "Полина",
        "surname": "Вешкина",
        "exams": ["Теория вероятностей", "Английский", "Web-программирование"],
        "marks": [4, 5, 5],
    },
    {
        "name": "Надежда",
        "surname": "Сударикова",
        "exams": ["Теория вероятностей", "Английский", "Web-программирование"],
        "marks": [4, 4, 4],
    },
    {
        "name": "Елена",
        "surname": "Голубева",
        "exams": ["Теория вероятностей", "Английский", "Web-программирование"],
        "marks": [5, 5, 5],
    },
    {
        "name": "Полина",
        "surname": "Калещук",
        "exams": ["Теория вероятностей", "Английский", "Web-программирование"],
        "marks": [5, 5, 5],
    },
    {
        "name": "Алёна",
        "surname": "Яковлева",
        "exams": ["Теория вероятностей", "Английский", "Web-программирование"],
        "marks": [4, 3, 5],
    },
]


def filter_students(groupmates):
    average_mark = float(input("Введите средний балл для фильтрации: "))
    filtered_students = []
    for student in groupmates:
        marks_sum = sum(student["marks"])
        marks_count = len(student["marks"])
        average = marks_sum / marks_count
        if average > average_mark:
            filtered_students.append(student)
    return filtered_students


filtered_students = filter_students(groupmates)
for student in filtered_students:
    print(
        student["name"].ljust(15),
        student["surname"].ljust(10),
        str(student["exams"]).ljust(30),
        str(student["marks"]).ljust(20),
    )

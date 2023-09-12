var groupmates = [
    {
        "name": "Полина",
        "surname": "Вешкина",
        "group": "БФИ2102",
        "marks": [4, 5, 5],
    },
    {
        "name": "Надежда",
        "surname": "Сударикова",
        "group": "БФИ2102",
        "marks": [4, 4, 4],
    },
    {
        "name": "Елена",
        "surname": "Голубева",
        "group": "БФИ2101",
        "marks": [5, 5, 5],
    },
    {
        "name": "Полина",
        "surname": "Калещук",
        "group": "БФИ2102",
        "marks": [5, 5, 5],
    },
    {
        "name": "Алёна",
        "surname": "Яковлева",
        "group": "БФИ2101",
        "marks": [4, 3, 5],
    },
];

var rpad = function (str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

var printStudents = function (students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i <= students.length - 1; i++) {
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
};

var filterStudents = function (students, group, averageMark) {
    var filteredStudents = [];
    for (var i = 0; i < students.length; i++) {
        if (students[i].group === group) {
            var sum = students[i].marks.reduce(function (a, b) {
                return a + b;
            });
            var average = sum / students[i].marks.length;
            if (average > averageMark) {
                filteredStudents.push(students[i]);
            }
        }
    }
    return filteredStudents;
};

// var group = prompt("Введите название группы: ");
// var averageMark = parseFloat(prompt("Введите среднюю оценку: "));

// var filteredGroupmates = filterStudents(groupmates, group, averageMark);

printStudents(groupmates)
// console.log(`Найдем студентов группы: ${group} со средней оценкой выше: ${averageMark}`)
// printStudents(filteredGroupmates);
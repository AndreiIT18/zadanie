groupmates = [
 {
 "name": u"Василий",
 "group": "912-2",
 "age": 12,
 "marks": [4, 3, 5, 5, 4]
 },
 {
 "name": u"Анна",
 "group": "912-1",
 "age": 18,
 "marks": [3, 2, 3, 4, 3]
 },
 {
 "name": u"Георгий",
 "group": "912-2",

 "age": 19,
 "marks": [3, 5, 4, 3, 5]
 },
 {
 "name": u"Валентина",
 "group": "912-1",
 "age": 18,
 "marks": [5, 5, 5, 4, 5]
 }
]
def print_students(students):
 print 
 u"Имя студента".ljust(15), \
 u"Группа".ljust(8), \
 u"Возраст".ljust(8), \
 u"Оценки".ljust(20)

 for student in students:
    print(
 student["name"],
 student["group"],
 str(student["age"]),
 str(student["marks"]))
 print 
filter(lambda x: sum(x.get("marks"))/len(x.get("marks")) > 3, groupmates)
print_students(groupmates)


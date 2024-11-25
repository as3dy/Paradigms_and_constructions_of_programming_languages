# 1) Определение классов данных в соответствии с предметной областью "Студенческая группа" и "Кафедра" (Вариант 28, Шевченко Г.А)

# Класс "Кафедра"
class Department:
  def __init__(self, id, name):
    self.id = id         # ID записи о кафедре
    self.name = name       # Наименование кафедры

# Класс "Студенческая группа"
class StudentGroup:
  def __init__(self, id, name, num_students, department_id):
    self.id = id         # ID записи о студенческой группе
    self.name = name       # Наименование группы
    self.num_students = num_students # Количество студентов (количественный признак)
    self.department_id = department_id # ID записи о кафедре (для связи один-ко-многим)

# Класс для связи многие-ко-многим "Группы кафедры"
class DepartmentGroup:
  def __init__(self, department_id, group_id):
    self.department_id = department_id # ID записи о кафедре
    self.group_id = group_id      # ID записи о студенческой группе

# 2) Создание списков объектов классов с тестовыми данными

# Список кафедр
departments = [
  Department(1, "Кафедра ФН"),
  Department(2, "Кафедра ИУ"),
  Department(3, "Кафедра ИБМ"),
  Department(4, "Кафедра СМ")
]

# Список студенческих групп
student_groups = [
  StudentGroup(1, "ФН1-13Б", 25, 1),
  StudentGroup(2, "ИУ7-24Б", 30, 2),
  StudentGroup(3, "ИБМ3-34Б", 28, 3),
  StudentGroup(4, "ИУ6-14Б", 28, 2),
  StudentGroup(5, "СМ12-43Б", 23, 4),
  StudentGroup(6,"ИБМ6-33Б",29,3),
  StudentGroup(7,"ФН3-41Б",23,1),
  StudentGroup(8,"СМ14-32Б",21,4)
  ]

# Связи многие-ко-многим между кафедрами и студенческими группами
department_groups = [
  DepartmentGroup(1, 1),
  DepartmentGroup(1, 7), 
  DepartmentGroup(2, 2),
  DepartmentGroup(2, 4),
  DepartmentGroup(3, 3),
  DepartmentGroup(3, 6),
  DepartmentGroup(4, 5), 
  DepartmentGroup(4, 8),   
  ]

# Создание словарей для быстрого доступа к данным по ID
department_dict = {dept.id: dept for dept in departments}
group_dict = {group.id: group for group in student_groups}

# 3) Запросы

# Запрос №1: Выведите список всех связанных студенческих групп и кафедр, отсортированный по кафедрам, сортировка по студенческим группам произвольная.

# Создаем список кортежей (кафедра, студенческая группа)
dept_group_list = [(department_dict[group.department_id], group) for group in student_groups]

# Сортируем список по названию кафедры
dept_group_list.sort(key=lambda x: x[0].name)

# Результат
print("Список всех связанных студенческих групп и кафедр, отсортированный по кафедрам:")
for dept, group in dept_group_list:
  print(f"Кафедра: {dept.name}, Студенческая группа: {group.name}")

# Запрос №2: Выведите список кафедр с общим количеством студентов в студенческих группах в каждой кафедре, отсортированный по общему количеству студентов.

# Суммируем количество студентов по кафедрам
dept_student_counts = {}
for group in student_groups:
  dept_id = group.department_id
  dept_student_counts[dept_id] = dept_student_counts.get(dept_id, 0) + group.num_students

# Преобразуем данные в список кортежей (кафедра, общее количество студентов)
dept_totals = [(department_dict[dept_id], total_students) for dept_id, total_students in dept_student_counts.items()]

# Сортируем по общему количеству студентов (по убыванию)
dept_totals.sort(key=lambda x: x[1], reverse=True)

# Выводим результат
print("\nСписок кафедр с общим количеством студентов в студенческих группах, отсортированный по общему количеству студентов:")
for dept, total_students in dept_totals:
  print(f"Кафедра: {dept.name}, Общее количество студентов: {total_students}")

# Запрос №3:
# Выведите список всех кафедр, у которых в названии присутствует слово «кафедра», и список связанных с ними студенческих групп.

# Создаем словарь department_id -> [group_id, ...] для связей многие-ко-многим
dept_to_groups = {}
for dg in department_groups:
  dept_to_groups.setdefault(dg.department_id, []).append(dg.group_id)

# Выводим список кафедр и связанных с ними студенческих групп
print("\nСписок кафедр, у которых в названии присутствует слово «кафедра», и связанных с ними студенческих групп:")
for dept_id, group_ids in dept_to_groups.items():
  dept = department_dict[dept_id]
  if "кафедра" in dept.name.lower():
    # Получаем список студенческих групп
    groups = [group_dict[group_id] for group_id in group_ids]
    print(f"Кафедра: {dept.name}")
    print("Студенческие группы:")
    for group in groups:
      print(f"- {group.name}")
    print()

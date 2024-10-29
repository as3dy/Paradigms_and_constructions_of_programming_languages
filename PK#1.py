from dataclasses import dataclass
from typing import List
# Классы и данные:


# Класс «Кафедра»
@dataclass
class Kafedra:
  id_kafedra: int
  name_kafedra: str

# Класс «Студенческая группа»
@dataclass
class StudGruppa:
  id_gruppa: int
  name_gruppa: str
  kolichestvo_studentov: int
  id_kafedra: int # Для реализации связи один-ко-многим

# Класс «Группы кафедры» для реализации связи многие-ко-многим
@dataclass
class GruppyKafedry:
  id_gruppa: int
  id_kafedra: int

# Создание списка объектов класса «Кафедра» с тестовыми данными
kafedry = [
  Kafedra(id_kafedra=1, name_kafedra='Информатики'),
  Kafedra(id_kafedra=2, name_kafedra='Математики'),
  Kafedra(id_kafedra=3, name_kafedra='Физики'),
]

# Создание списка объектов класса «Студенческая группа» с тестовыми данными
gruppy = [
  StudGruppa(id_gruppa=1, name_gruppa='ИВБО-01-21', kolichestvo_studentov=25, id_kafedra=1),
  StudGruppa(id_gruppa=2, name_gruppa='ИВБО-02-21', kolichestvo_studentov=28, id_kafedra=2),
  StudGruppa(id_gruppa=3, name_gruppa='ИВБО-03-21', kolichestvo_studentov=27, id_kafedra=1),
  StudGruppa(id_gruppa=4, name_gruppa='ИВБО-04-21', kolichestvo_studentov=30, id_kafedra=3),
  StudGruppa(id_gruppa=5, name_gruppa='ИВБО-05-21', kolichestvo_studentov=26, id_kafedra=2),
]

# Создание списка объектов класса «Группы кафедры» с тестовыми данными
gruppy_kafedry = [
  GruppyKafedry(id_gruppa=1, id_kafedra=1),
  GruppyKafedry(id_gruppa=1, id_kafedra=2),
  GruppyKafedry(id_gruppa=2, id_kafedra=2),
  GruppyKafedry(id_gruppa=2, id_kafedra=3),
  GruppyKafedry(id_gruppa=3, id_kafedra=1),
  GruppyKafedry(id_gruppa=3, id_kafedra=3),
  GruppyKafedry(id_gruppa=4, id_kafedra=3),
  GruppyKafedry(id_gruppa=5, id_kafedra=2),
  GruppyKafedry(id_gruppa=5, id_kafedra=1),
]



# Создаем словарь, где ключ - id кафедры, значение - объект кафедры
kafedra_dict = {kafedra.id_kafedra: kafedra for kafedra in kafedry}

# Создаем словарь, где ключ - id кафедры, значение - список студентческих групп
kafedra_to_gruppy = {}

for gruppa in gruppy:
  key = gruppa.id_kafedra
  if key in kafedra_to_gruppy:
    kafedra_to_gruppy[key].append(gruppa)
  else:
    kafedra_to_gruppy[key] = [gruppa]

# Сортируем кафедры по имени
sorted_kafedry = sorted(kafedry, key=lambda k: k.name_kafedra)

# Выводим список кафедр и связанных с ними групп
print("Список кафедр и связанных с ними групп (сортировка по кафедрам):\n")
for kafedra in sorted_kafedry:
  print(f"Кафедра: {kafedra.name_kafedra}")
  gruppy_kafedry = kafedra_to_gruppy.get(kafedra.id_kafedra, [])
  for gruppa in gruppy_kafedry:
    print(f" Группа: {gruppa.name_gruppa}")
  print()


# Подсчет общего числа студентов в каждой кафедре
kafedra_total_students = []

for kafedra in kafedry:
  gruppy_kafedry = kafedra_to_gruppy.get(kafedra.id_kafedra, [])
  total_students = sum(gruppa.kolichestvo_studentov for gruppa in gruppy_kafedry)
  kafedra_total_students.append((kafedra, total_students))

# Сортировка кафедр по общему числу студентов (по убыванию)
kafedra_total_students.sort(key=lambda x: x[1], reverse=True)

# Вывод результата
print("Список кафедр с общим числом студентов (сортировка по числу студентов):\n")
for kafedra, total_students in kafedra_total_students:
  print(f"Кафедра: {kafedra.name_kafedra}, Общее число студентов: {total_students}")




# Определяем слово для поиска в названии кафедры
search_word = "мати"

# Фильтруем кафедры, содержащие искомое слово
filtered_kafedry = [kafedra for kafedra in kafedry if search_word.lower() in kafedra.name_kafedra.lower()]

# Создаем словарь кафедр для быстрого доступа по id
kafedra_dict = {kafedra.id_kafedra: kafedra for kafedra in kafedry}

# Создаем словарь групп для быстрого доступа по id
gruppa_dict = {gruppa.id_gruppa: gruppa for gruppa in gruppy}

# Для каждой выбранной кафедры находим связанные с ней группы через связь многие-ко-многим
print(f"Кафедры, содержащие '{search_word}' в названии, и связанные с ними группы:\n")
for kafedra in filtered_kafedry:
  # Находим все связи в gruppy_kafedry для данной кафедры
  related_gruppy_ids = [relation.id_gruppa for relation in gruppy_kafedry if relation.id_kafedra == kafedra.id_kafedra]
  # Убираем дубликаты
  related_gruppy_ids = list(set(related_gruppy_ids))
  # Получаем объекты групп
  related_gruppy = [gruppa_dict[gruppa_id] for gruppa_id in related_gruppy_ids]
  print(f"Кафедра: {kafedra.name_kafedra}")
  for gruppa in related_gruppy:
    print(f" Группа: {gruppa.name_gruppa}")
  print()

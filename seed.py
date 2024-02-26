from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Score
from random import randint, choice
from datetime import datetime, timedelta

# Підключення до бази даних
db_username = 'postgres'
db_password = 'mysecretpassword'
db_name = 'postgres'
db_host = 'localhost'
db_port = '5432'

db_string = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(db_string)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Ініціалізація Faker
fake = Faker()

# Створення студентів, груп, викладачів, предметів та оцінок
# Студенти
for _ in range(50):
    student = Student(name=fake.name())
    session.add(student)

# Групи
groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    group = Group(name=group_name)
    session.add(group)

# Викладачі
for _ in range(5):
    teacher = Teacher(name=fake.name())
    session.add(teacher)

# Предмети
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
for subject_name in subjects:
    teacher_id = randint(1, 5)
    subject = Subject(name=subject_name, teacher_id=teacher_id)
    session.add(subject)

# Оцінки
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
for student_id in range(1, 51):
    for subject_id in range(1, 6):
        score_date = fake.date_time_between(start_date=start_date, end_date=end_date)
        score = Score(student_id=student_id, subject_id=subject_id, score=randint(1, 100), date=score_date)
        session.add(score)

# Збереження змін до бази даних
session.commit()

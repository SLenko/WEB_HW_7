from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Score

# Підключення до бази даних
db_username = 'postgres'
db_password = 'mysecretpassword'
db_name = 'postgres'
db_host = 'localhost'
db_port = '5432'

db_string = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(db_string)
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    avg_scores = session.query(Student, func.avg(Score.score).label('average_score')).\
        join(Score).group_by(Student.id).order_by(func.avg(Score.score).desc()).limit(5).all()
    return avg_scores

def select_2(subject_name):
    # Знайти студента із найвищим середнім балом з певного предмета
    highest_avg_score_student = session.query(Student, func.avg(Score.score).label('average_score')).\
        join(Score).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).\
        order_by(func.avg(Score.score).desc()).first()
    return highest_avg_score_student

def select_3(subject_name):
    # Знайти середній бал у групах з певного предмета
    avg_scores_group = session.query(Group.name, func.avg(Score.score).label('average_score')).\
        join(Student).join(Score).join(Subject).filter(Subject.name == subject_name).\
        group_by(Group.name).all()
    return avg_scores_group

def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок)
    avg_score_overall = session.query(func.avg(Score.score)).scalar()
    return avg_score_overall

def select_5(teacher_name):
    # Знайти які курси читає певний викладач
    courses_taught = session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()
    return courses_taught

def select_6(group_name):
    # Знайти список студентів у певній групі
    students_in_group = session.query(Student).join(Group).filter(Group.name == group_name).all()
    return students_in_group

def select_7(group_name, subject_name):
    # Знайти оцінки студентів у окремій групі з певного предмета
    scores_in_group_subject = session.query(Student.name, Score.score).\
        join(Group).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()
    return scores_in_group_subject

def select_8(teacher_name):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів
    avg_teacher_scores = session.query(func.avg(Score.score)).join(Subject).join(Teacher).\
        filter(Teacher.name == teacher_name).scalar()
    return avg_teacher_scores

def select_9(student_name):
    # Знайти список курсів, які відвідує певний студент
    courses_attended_by_student = session.query(Subject.name).join(Score).join(Student).\
        filter(Student.name == student_name).distinct().all()
    return courses_attended_by_student

def select_10(student_name, teacher_name):
    # Список курсів, які певному студенту читає певний викладач
    courses_taught_to_student = session.query(Subject.name).join(Teacher).join(Score).\
        join(Student).filter(Student.name == student_name, Teacher.name == teacher_name).distinct().all()
    return courses_taught_to_student

# Виконання запитів і виведення результатів для тестування
if __name__ == "__main__":
    results = {
        "select_1": select_1(),
        "select_2": select_2("Math"), 
        "select_3": select_3("Math"), 
        "select_4": select_4(),
        "select_5": select_5("John Doe"), 
        "select_6": select_6("Group A"), 
        "select_7": select_7("Group A", "Math"), 
        "select_8": select_8("John Doe"), 
        "select_9": select_9("Alice Smith"), 
        "select_10": select_10("Alice Smith", "John Doe") 
    }

    for key, value in results.items():
        print(f"Result for {key}: {value}")

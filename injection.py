from datacenter.models import Schoolkid, Chastisement, Mark, Commendation, Lesson, Subject
from random import randint


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[1, 2, 3])
    for mark in bad_marks:
        mark.points = randint(4, 5)
        mark.save()

def remove_chastisements(schoolkid):
    chasticements = Chastisement.objects.filter(schoolkid=schoolkid)
    chasticements.delete()

def get_subject(title, year):
    return Subject.objects.filter(title=title, year_of_study=year)[0]

def get_kid_lessons(schoolkid, subject):
    return Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject=subject)

def create_commendations(text, schoolkid, lessons):
    for lesson in lessons:
        Commendation.objects.create(text=text, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher,
                                    created=lesson.date)

def main():
    vanya = Schoolkid.objects.filter(full_name__contains='Фролов Иван')[0]
    fix_marks(vanya)
    remove_chastisements(vanya)
    math = get_subject('Математика', vanya.year_of_study)
    kid_lessons = get_kid_lessons(vanya, math)
    create_commendations('Безупречная работа!', vanya, kid_lessons)


if __name__ == '__main__':
    main()

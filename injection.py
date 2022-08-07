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


def create_commendations(text, schoolkid, lessons):
    for lesson in lessons:
        Commendation.objects.create(text=text, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher,
                                    created=lesson.date)

def main(name='Фролов Иван'):
    try:
        kid = Schoolkid.objects.get(full_name__contains=name)
        fix_marks(kid)
        remove_chastisements(kid)
        math = Subject.objects.get(title='Математика', year_of_study=kid.year_of_study)
        kid_lessons = Lesson.objects.filter(subject=math, year_of_study=kid.year_of_study, group_letter=kid.group_letter)
        create_commendations('Безупречная работа!', kid, kid_lessons)
    except (AttributeError, Schoolkid.DoesNotExist):
        print('Ученик с таким ФИО найден')
    except (AttributeError, Subject.DoesNotExist):
        print('Предмет не найден')
    except (AttributeError, Schoolkid.MultipleObjectsReturned):
        print('Уточните ФИО ученика')
    except (AttributeError, Subject.MultipleObjectsReturned):
        print('Слишком много математик расплодилось. Нужна конкретика')


if __name__ == '__main__':
    main()

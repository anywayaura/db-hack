from datacenter.models import Schoolkid, Chastisement, Mark, Commendation, Lesson, Subject

def remove_chastisements(schoolkid):
    chasticements = Chastisement.objects.filter(schoolkid=schoolkid)
    chasticements.delete()

def create_commendations(text, schoolkid, lessons):
    for lesson in lessons:
        Commendation.objects.create(text=text, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher,
                                    created=lesson.date)

def hack(name='Фролов Иван'):
    try:
        kid = Schoolkid.objects.get(full_name__contains=name)
        Mark.objects.filter(schoolkid=kid, points__in=[1, 2, 3]).update(points=5)
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


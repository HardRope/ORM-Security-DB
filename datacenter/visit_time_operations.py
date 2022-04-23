from django.utils.timezone import localtime

def get_duration(visit):
    '''Возвращает продолжительность визита в total_seconds'''
    enter_time = visit.entered_at
    leave_time = visit.leaved_at
    if not leave_time:
        leave_time = localtime()
    visit_duration = (leave_time - enter_time)
    return int(visit_duration.total_seconds())


def format_duration(duration):
    '''Возвращает список строк часы-минуты в формате [00, 00]'''
    duration_time = [str(duration // 3600), str((duration % 3600) // 60)]
    for val, time in enumerate(duration_time):
        if len(time) == 1:
            duration_time[val] = '0' + time
    return duration_time

def get_strange(duration):
    '''Возвращает True при продолжительности визита больше 1 часа'''
    return duration > 3600
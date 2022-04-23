from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.visit_time_operations import get_duration, format_duration, get_strange
from django.shortcuts import render

def storage_information_view(request):

    open_visits = Visit.objects.filter(leaved_at=None)
    open_visits_serialized = []

    for visit in open_visits:
        name = visit.passcard.owner_name
        enter_time = visit.entered_at

        visit_duration = get_duration(visit)
        duration_time = '{} ч. {} мин.'.format(*format_duration(visit_duration))

        is_strange = get_strange(visit_duration)

        about_visit = {
            'who_entered': name,
            'entered_at': enter_time,
            'duration': duration_time,
            'is_strange': is_strange
        }

        open_visits_serialized.append(about_visit)

    context = {
        'non_closed_visits': open_visits_serialized,
    }
    return render(request, 'storage_information.html', context)

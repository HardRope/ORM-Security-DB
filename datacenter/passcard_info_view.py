from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.visit_time_operations import get_duration, format_duration, get_strange
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = Visit.objects.filter(passcard=passcard)

    serialazed_visits = []

    for visit in this_passcard_visits:
        enter_time = visit.entered_at

        visit_duration = get_duration(visit)
        duration_time = '{}:{}'.format(*format_duration(visit_duration))

        is_strange = get_strange(visit_duration)

        about_visit = {
            'entered_at': enter_time,
            'duration': duration_time,
            'is_strange': is_strange
        }

        serialazed_visits.append(about_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialazed_visits
    }
    return render(request, 'passcard_info.html', context)

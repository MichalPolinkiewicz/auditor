# Create your views here.
from typing import List

from django.shortcuts import render
from django.http import HttpResponse

# auditor/2/audit/
from auditor.models import Target


def target_audit(request, target_id):
    return HttpResponse(target_id)


# auditor/2/result/
def target_results(request, target_id):
    return HttpResponse("run audit for target with id", target_id)


# auditor/audit
def audit(request):
    targets = Target.objects.all()
    for t in targets:
        print(t)

    return HttpResponse('run audits for all targets')


# auditor/results
def results(request):
    return HttpResponse("results soon")


# menu wyboru - pokaz ostatnie rezultaty, edytuj konfiguracje, wykonaj audyt
# auditor
def index(request):
    return HttpResponse(render(request, 'auditor/index.html', {}))


def run_audits(targets: List[Target]):
    for t in targets:
        run_single_audit(t)


def run_single_audit(target: Target):
    print('run audit for target:', target)

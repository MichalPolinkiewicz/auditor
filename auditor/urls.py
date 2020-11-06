from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # auditor/audit
    path('audit/', views.audit, name='audit'),
    # auditor/results
    path('results/', views.results, name='results'),
    # auditor/audit/2
    path('audit/<int:target_id>/', views.target_audit, name='target_audit'),
    # auditor/results/2
    path('results/<int:target_id>/', views.target_results, name='target_results'),
]
from django.urls import path
from .views import AddCreditsView, AutomationCaptureView, AutomationBlastView, TaskSendMailView, TaskPaymentView

urlpatterns = [
    path('automation-capture/', AutomationCaptureView.as_view(), name='automation-capture'),
    path('automation-blast/', AutomationBlastView.as_view(), name='automation-blast'),
    path('task-sendmail/', TaskSendMailView.as_view(), name='task-sendmail'),
    path('task-payment/', TaskPaymentView.as_view(), name='task-payment'),
    path('add-credits/', AddCreditsView.as_view(), name='add-credits'),
]

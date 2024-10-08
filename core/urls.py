# core/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    RegisterUserView,
    UpdateUserView,
    AddCreditsView,
    AutomationCaptureView,
    AutomationBlastView,
    TaskSendMailView,
    TaskPaymentView,
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", RegisterUserView.as_view(), name="register_user"),
    path("user/<int:pk>/update/", UpdateUserView.as_view(), name="update_user"),
    path(
        "automation-capture/",
        AutomationCaptureView.as_view(),
        name="automation-capture",
    ),
    path("automation-blast/", AutomationBlastView.as_view(), name="automation-blast"),
    path("task-sendmail/", TaskSendMailView.as_view(), name="task-sendmail"),
    path("task-payment/", TaskPaymentView.as_view(), name="task-payment"),
    path("add-credits/", AddCreditsView.as_view(), name="add-credits"),
]

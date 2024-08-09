from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

class AddCreditsView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        amount = request.data.get("amount")
        if not amount or float(amount) <= 0:
            return Response({"error": "Valor inválido."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.balance += float(amount)
        request.user.save()
        return Response({"message": "Créditos adicionados com sucesso.", "new_balance": request.user.balance})

class AutomationCaptureView(APIView):
    permission_classes = [IsAuthenticated]
    cost = 10.00 

    def get(self, request):
        request.user.balance -= self.cost
        request.user.save()
        return Response({"message": "Automation Capture"})

class AutomationBlastView(APIView):
    permission_classes = [IsAuthenticated]
    cost = 15.00

    def get(self, request):
        request.user.balance -= self.cost
        request.user.save()
        return Response({"message": "Automation Blast"})

class TaskSendMailView(APIView):
    permission_classes = [IsAuthenticated]
    cost = 5.00

    def get(self, request):
        request.user.balance -= self.cost
        request.user.save()
        return Response({"message": "Task Send Mail"})

class TaskPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    cost = 20.00

    def get(self, request):
        request.user.balance -= self.cost
        request.user.save()
        return Response({"message": "Task Payment"})
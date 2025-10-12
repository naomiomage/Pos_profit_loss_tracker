from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from .models import Transaction
from .serializers import TransactionSerializer


# ✅ List & Create Transactions
class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ✅ Retrieve, Update, Delete a Transaction
class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


# ✅ Profit/Loss Summary
class ProfitLossSummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        total_income = (
            Transaction.objects.filter(user=user, transaction_type='deposit')
            .aggregate(Sum('amount'))['amount__sum']
            or 0
        )

        total_expenses = (
            Transaction.objects.filter(user=user, transaction_type__in=['withdrawal', 'expense'])
            .aggregate(Sum('amount'))['amount__sum']
            or 0
        )

        net_profit_or_loss = total_income - total_expenses

        data = {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_profit_or_loss": net_profit_or_loss,
        }

        return Response(data)

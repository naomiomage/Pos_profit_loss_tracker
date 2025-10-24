from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.contrib.auth.models import User

from .models import Transaction
from .serializers import TransactionSerializer

# ==============================
# List & Create Transactions
# ==============================
class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]  # anyone can access

    def perform_create(self, serializer):
        # Assign the first user in the database (superuser or first created user)
        default_user = User.objects.first()
        serializer.save(user=default_user)


# ==============================
# Retrieve, Update, Delete a Transaction
# ==============================
class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]  # anyone can access

    def get_queryset(self):
        return Transaction.objects.all()


# ==============================
# Profit/Loss Summary
# ==============================
class ProfitLossSummaryView(APIView):
    permission_classes = [permissions.AllowAny]  # anyone can access

    def get(self, request):
        # Simple totals
        total_inflow = Transaction.objects.filter(transaction_type='deposit').aggregate(Sum('amount'))['amount__sum'] or 0
        total_outflow = Transaction.objects.filter(transaction_type__in=['withdrawal', 'expense']).aggregate(Sum('amount'))['amount__sum'] or 0
        total_charges = Transaction.objects.filter(transaction_type='charge').aggregate(Sum('amount'))['amount__sum'] or 0
        net_balance = (total_inflow + total_charges) - total_outflow

        data = {
            "Total Deposits (Customers Gave You Cash)": total_inflow,
            "Total Withdrawals (You Gave Cash to Customers)": total_outflow,
            "Total Expenses (Your Spending)": total_outflow,  # separate later if needed
            "Total Charges (Profit Earned)": total_charges,
            "Net Balance": net_balance
        }
        return Response(data)

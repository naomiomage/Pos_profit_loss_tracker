from django.urls import path
from .views import TransactionListCreateView, TransactionDetailView, ProfitLossSummaryView

urlpatterns = [
    path('', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('summary/', ProfitLossSummaryView.as_view(), name='profit-loss-summary'),
]


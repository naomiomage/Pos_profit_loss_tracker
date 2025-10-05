# Pos\_profit\_loss\_tracker

An API to help POS agents track daily profit and loss.



This is a Django REST Framework project that helps POS agents record their daily transactions (deposit, withdrawal, transfer, expenses, and charges) and automatically calculate profit or loss.



💡 Project Overview



This week focused on building the core functionality — the Transaction API.

Users (POS agents) can now create, view, update, and delete transactions in their account.

Each transaction is tied to a user and includes its type, amount, description, and date.



✅ Progress (Week 3)



Completed:



Set up Django project and GitHub repository



Created transactions app



Added Transaction model



Built CRUD API endpoints using Django REST Framework



Tested endpoints successfully with authentication



Endpoints working now:



GET /api/transactions/ → List user’s transactions



POST /api/transactions/ → Add a new transaction



PUT /api/transactions/{id}/ → Update a transaction



DELETE /api/transactions/{id}/ → Delete a transaction



⚙️ Tech Stack



Python 3



Django



Django REST Framework



SQLite (default database)



📅 Next Steps (Week 4)



Build Reports App to calculate daily profit \& loss



Add date-range summaries



Implement JWT Authentication for users



🔗 Repository



GitHub Link: https://github.com/your-username/Pos\_profit\_loss\_tracker



👩‍💻 Author



Naomi Omage

ALX Capstone Project (Week 3)


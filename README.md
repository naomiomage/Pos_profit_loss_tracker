# POS Profit \& Loss Tracker



An API designed to help POS agents track daily profit and loss.



This Django REST Framework project enables POS agents to record their daily transactions (deposit, withdrawal, transfer, expenses, and charges) and automatically calculate profit or loss.

It provides a clear overview of financial performance and helps agents make informed decisions.



## Project Overview



The POS Profit \& Loss Tracker simplifies financial tracking for POS agents.

It allows users to:



* Record all types of daily transactions.



* Automatically calculate daily profit and loss.



* View summaries of total income, expenses, and charges.



* Manage transactions securely through authentication.



* Each transaction is tied to a registered user and includes details such as type, amount, description, and date.



### **Key Features**



User authentication and secure access



CRUD operations for transactions



Automatic profit and loss summary calculation



Filter transactions by date or type



Easy-to-use RESTful API endpoints



#### Completed Tasks



Set up Django project and GitHub repository



Created the transactions app and Transaction model



Built CRUD API endpoints using Django REST Framework



Implemented summary endpoint to calculate profit and loss





#### API Endpoints

##### Method	Endpoint	Description

GET	/api/transactions/	Retrieve all user transactions

POST	/api/transactions/	Add a new transaction

GET	/api/transactions/summary/	View total profit and loss summary

PUT	/api/transactions/{id}/	Update a specific transaction

DELETE	/api/transactions/{id}/	Delete a specific transaction



##### Tech Stack



Python 3



Django



Django REST Framework



SQLite (default database)





##### Future Improvements



Add frontend interface for easier interaction



Include export options (PDF or Excel)



Add email reports for daily profit and loss summaries





##### Repository



https://github.com/naomiomage/Pos\_profit\_loss\_tracker



##### Author

Naomi Omage

ALX Capstone Project (Final Submission)



Naomi Omage

ALX Capstone Project (Final Submission)


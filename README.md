Student Management System 

This project is a Student Management System built using Python and Tkinter for the GUI, SQLite for the database, and PIL for image handling. The system allows for student attendance management, including login and attendance tracking by course, year, and department.

Features

	1.	Login System: Allows users to log in with a username and password, and verifies the credentials against an SQLite database.
	2.	Attendance Management:
	•	Users can mark student attendance by selecting students who are absent.
	•	Attendance is saved in the SQLite database for future reference.
	3.	Course, Year, and Department Filtering: Attendance can be recorded based on course, year, and department.

Prerequisites

Ensure you have the following installed:

	•	Python 3.x
	•	Tkinter (comes pre-installed with Python)
	•	Pillow: Used for handling images
 
 pip install pillow
 
 SQLite: Used for storing login credentials and attendance data


 How to Run the Project

	1.	Clone the repository:git clone https://github.com/yourusername/student-management-system.git
cd student-management-system

Install Dependencies:
	•	Install the necessary Python libraries:pip install pillow


 Database Setup:
	•	The system uses an SQLite database named srms.db.
	•	Create the following tables in the database for login credentials and attendance storage:


 Run the Program:
	•	Execute the Python script:python main.py

 Code Overview

	1.	Login System:
	•	Users log in using their username and password, which are validated against the login table in the SQLite database.
	•	If successful, the system transitions to the attendance marking page.
	2.	Attendance Marking:
	•	Attendance is marked by selecting roll numbers. Green indicates present, and red indicates absent.
	•	Upon submission, the selected absentees are stored in the attendence table in the SQLite database.
	3.	SQLite Database:
	•	Stores user login credentials in the login table.
	•	Attendance details, including absentees, are stored in the attendence table.

Sample Usage

	1.	Login Page:
	•	Enter the course, year, department, login name, and password.
	•	Click the “Login” button to authenticate.
	2.	Attendance Page:
	•	Mark students who are absent by toggling their roll number button (red indicates absent, green indicates present).
	•	Click “Submit” to save the attendance in the database.

Future Enhancements

	1.	Add user role management (admin, teacher).
	2.	Generate attendance reports for students.
	3.	Add a more secure authentication system.

License

This project is licensed under the MIT License.

Feel free to contribute or suggest improvements!

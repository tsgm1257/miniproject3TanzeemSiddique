### INF601 - Advanced Programming in Python
### Tanzeem Siddique
### Mini Project 3


# Mini Project 3 - Expense Tracker with Enhanced Authentication

## Description

This project extends a basic Flask expense tracker application by adding robust user authentication features. It includes user registration, login, and logout functionalities, enhanced with Bootstrap modals for user feedback. The application utilizes a SQLite database for user management and session handling for secure user sessions.

### Key features include:

* **User Registration:** Allows new users to register with a unique username, first name, last name, and password.
* **User Login:** Enables registered users to log in using their credentials.
* **User Logout:** Provides a secure way for users to log out of their session.
* **Bootstrap Modals:** Displays success and error messages using Bootstrap modals for a better user experience.
* **Database Integration:** Uses SQLite to store user data securely.
* **Session Management:** Manages user sessions to maintain login status.

## Getting Started


### Dependencies

1.  **Install Required Packages:**
    * Install the packages using pip:
    ```
    pip install -r requirements.txt
    ```

2.  **Setup Database:**
    * Initialize the SQLite database using Flask:
    ```
    flask --app flaskr init-db
    ```

### Executing program

1.  **Run the Application:**
    * Start the Flask development server:
    ```
    flask --app flaskr run
    ```

### Output

* **Registration:** Navigate to `/auth/register` to create a new user account.
* **Login:** Navigate to `/auth/login` to log in with an existing account.
* **Logout:** Click the "Log Out" link in the navigation bar to end the session.
* **Add Expenses:** After logging in, use the dashboard to add new expense entries.
* **Edit Expenses:** Modify existing expense entries through the dashboard interface.
* **Delete Expenses:** Remove expense entries as needed.
* **Add Categories:** Create and manage expense categories to organize your expenses.
* The application will display success or error messages using Bootstrap modals after each authentication and expense related action.

## Authors

Contributors names and contact info

ex. Tanzeem Siddique

## Acknowledgments

Inspiration, code snippets, etc.
* [Flask](https://flask.palletsprojects.com/en/stable/tutorial/)
* [Bootstrap](https://flask.palletsprojects.com/en/stable/tutorhttps://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [YouTube](https://www.youtube.com/watch?v=Yry14DldSvs)
* [YouTube](https://chatgpt.com/share/67df4d0f-a480-8013-a2f3-7c73353eccc8https://chatgpt.com/share/67df4d0f-a480-8013-a2f3-7c73353eccc8)
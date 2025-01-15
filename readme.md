# PDUT

This is an example project using Django, Python's unittest testing framework, and a custom, testable sub-library.

---

## Work Instructions

1. **Checkout this project**
   - Clone or download the repository.
2. **Set up dependencies**
   - Run:
     ```bash
     pip install django
     ```
3. **Open the folder in VS Code**
   - Navigate to the project folder and open it in your preferred editor.
4. **Activate the virtual environment**
   - Run:
     ```bash
     env\Scripts\activate
     ```

---

## Running the Django App

### Initial Setup (required only once):
1. Navigate to the project folder:
   ```bash
   cd MyDjangoProject
   ```
2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Subsequent Runs:
- Start the development server:
  ```bash
  python manage.py runserver
  ```

---

## Running the Unit Tests

1. Navigate to the `sub_project` directory:
   ```bash
   cd MyDjangoProject\sub_project
   ```
2. Discover and run all tests:
   ```bash
   python -m unittest discover
   ```

---

Enjoy exploring the project! If you have any questions, feel free to ask.

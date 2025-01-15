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

## Additional Instructions

### Exploring Unit Test Examples
1. Navigate to the [Tokenizer file](MyDjangoProject/sub_project/tokenizer.py) to view the implementation of a tokenizer function.
2. Navigate to the [Tokenizer test file](MyDjangoProject/sub_project/test_tokenizer.py) to see unit tests written for the tokenizer function. These tests provide examples of using Python's `unittest` framework.

### Viewing the Tokenizer in Action
1. Navigate to the [Main App views file](MyDjangoProject/MainApp/views.py) to see how the `tokenizer` function is used within a Django view.
2. The view demonstrates integrating a custom Python function from a sub-library into a Django application.

---

Enjoy exploring the project! If you have any questions, feel free to ask.

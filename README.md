# BDD Test Project

## Project Overview

This project demonstrates Behavior-Driven Development (BDD) testing techniques applied to multiple applications. It includes sample applications and their corresponding BDD tests using the Behave framework.

## Components

### Applications

1. **HRM (Human Resource Management) Application**
   - A PyQt5-based desktop application for employee management
   - Features include adding, displaying, and managing employee records

2. **Todo Web Application**
   - A Flask-based web application for managing to-do tasks
   - Features include adding and deleting tasks

### Testing Framework

- **Behave**: Python BDD testing framework
- Feature files written in Gherkin syntax
- Step definitions implemented in Python

## Installation

1. Clone the repository:
   ```
   git clone git@github.com:tran-the-lam/BDD_Test.git
   cd BDD_Test
   ```

2. Install dependencies:
   ```
   pip install behave PyQt5 flask
   ```

## Usage

### HRM Application

Run the HRM application:
```
python source_code/hrm.py
```

### Todo Web Application

Run the Todo web application:
```
cd source_code/todo-app
python app.py
```

Access the application in your browser at:
```
http://127.0.0.1:5001
```

## Contributors
- [Hoàng Trương](https://github.com/truonganhhoang) 
- [Hong-Nhung Nguyen](https://github.com/nhunguet)
- [The-Lam Tran](https://github.com/tran-the-lam)

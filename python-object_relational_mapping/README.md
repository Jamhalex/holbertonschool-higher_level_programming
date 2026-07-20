# Python - Object-relational mapping

## Description

This project introduces the fundamentals of **Object-Relational Mapping (ORM)** in Python by connecting Python applications to a MySQL database.

The project is divided into two parts:

- **MySQLdb (mysqlclient):** Interacting directly with a MySQL database using SQL queries from Python.
- **SQLAlchemy ORM:** Mapping Python classes to database tables and manipulating database records through Python objects instead of writing SQL queries.

The objective is to understand how Python communicates with relational databases while learning the advantages of ORM abstraction.

---

## Learning Objectives

By the end of this project, you should be able to explain:

- How to connect a Python script to a MySQL database
- How to execute SQL queries from Python
- How to retrieve data from a database
- How to insert data into a database
- What Object-Relational Mapping (ORM) is
- The advantages of using an ORM
- How SQLAlchemy maps Python classes to database tables
- How to manipulate database records using Python objects

---

## Technologies Used

- Python 3.8.5
- MySQL 8.0
- MySQLdb (mysqlclient 2.0.3)
- SQLAlchemy 1.4.22
- Ubuntu 20.04 LTS
- pycodestyle 2.7.*

---

## Project Structure

```
python-object_relational_mapping/
│
├── 0-select_states.py
├── 1-filter_states.py
├── 2-my_filter_states.py
├── 3-my_safe_filter_states.py
├── 4-cities_by_state.py
├── 5-filter_cities.py
├── 6-model_state.py
├── ...
└── README.md
```

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQL Server 8.0
- mysqlclient 2.0.x
- SQLAlchemy 1.4.x
- All Python files must:
  - start with `#!/usr/bin/python3`
  - be executable
  - end with a new line
  - follow **pycodestyle 2.7**
  - include module, class, and function documentation

---

## Installation

### Install MySQL

```bash
sudo apt update
sudo apt install mysql-server
```

Verify installation:

```bash
mysql --version
```

---

### Install MySQLdb

```bash
sudo apt install python3-dev
sudo apt install libmysqlclient-dev
sudo apt install zlib1g-dev

sudo pip3 install mysqlclient==2.0.3
```

Verify:

```python
python3

>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```

---

### Install SQLAlchemy

```bash
sudo pip3 install SQLAlchemy==1.4.22
```

Verify:

```python
python3

>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```

---

## Running the Programs

Example:

```bash
./0-select_states.py root root hbtn_0e_0_usa
```

or

```bash
python3 0-select_states.py root root hbtn_0e_0_usa
```

---

## Concepts Covered

### MySQLdb

- Connecting to MySQL
- Creating cursors
- Executing SQL queries
- Fetching results
- Closing database connections

Example:

```python
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="my_db"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM states")
rows = cursor.fetchall()

cursor.close()
conn.close()
```

---

### SQLAlchemy ORM

SQLAlchemy removes the need to manually write SQL queries by representing database tables as Python classes.

Example:

```python
session.query(State).order_by(State.id).all()
```

Instead of writing:

```sql
SELECT * FROM states ORDER BY id;
```

---

## Key Concepts

- Relational Database
- MySQL
- SQL
- Python Database API
- Cursor
- Transactions
- Object Relational Mapping (ORM)
- SQLAlchemy Engine
- Session
- Declarative Base
- Model
- Primary Key
- Foreign Key

---

## Resources

- MySQLdb Documentation
- SQLAlchemy Documentation
- SQLAlchemy ORM Tutorial
- Python SQLAlchemy Cheatsheet
- Flask SQLAlchemy Documentation

---

## Author

**Johnson Alexander**

Holberton School

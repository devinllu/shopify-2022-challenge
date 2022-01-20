## Shopify Intern Challenge 2022

This project is built with Flask and SQL Alchemy and manages dependencies in a virtual environment.

To install dependencies, in the project root directory, assuming a Mac environment:

```pip install virtualenv```
```virtualenv venv```
```source venv/bin/activate```
```pip install -r requirements.txt```

Now you can run the app! Type:

```python app.py```

## A couple notes:

- If there is no database upon the server restarting, then the server will generate a new database with 4 rows of fake data.
- Supports all CRUD operations.
- Exports data to CSV by clicking the CSV button. It will be saved to the project's root directory.
- The Name attribute is a primary key, so you cannot create 2 postings with the same identical name. If it's a problem, this will be fixed in the project's next release (disclaimer: which is "probably" never).

Enjoy the project!
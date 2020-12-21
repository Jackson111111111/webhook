from MiddleKit.Run import MySQLObjectStore

store = MySQLObjectStore()
query = 'DROP TABLE students'
# <yes> <report> PYTHON_INJECTION_SQL c8d15e
store.executeSQL(query)
# <no> <report>
store.executeSQL('SELECT * FROM table')

# <yes> <report> PYTHON_INJECTION_SQL f5e2fc
cursor.execute('INSERT INTO table VALUES (%s, %s, %s)', var1, var2, var3)
# <no> <report>
cursor.execute('SELECT * FROM table') # FIXME

from django.db import connection
id = 14
cursor = connection.cursor()
# <yes> <report> PYTHON_INJECTION_SQL f5e2fc
cursor.execute("SELECT foo FROM bar WHERE baz = '30%%' AND id = %s", id)
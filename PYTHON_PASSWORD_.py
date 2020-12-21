# <yes> <report> PYTHON_PASSWORD_EMPTY 607f01
password = ""
# <yes> <report> PYTHON_PASSWORD_NULL c37c10
pwd = None
# <yes> <report> PYTHON_PASSWORD_HARDCODED eed164
password = "hardcoded"
# <yes> <report> PYTHON_PASSWORD_HARDCODED eed164
some_object.psswd = "also_hardcoded"

p_w_d = "not_so_hardcoded"
# <no> <report>
password = p_w_d
# <no> <report>
password = '%s%s' % (pswd1, pswd2)

from django.contrib.auth.models import User
# <yes> <report> PYTHON_PASSWORD_HARDCODED 12d164
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
# <yes> <report> PYTHON_PASSWORD_EMPTY 22d164
user2 = User.objects.create_user('paul', 'maccartney@thebeatles.com', '')

u = User.objects.get(username='john')
# <yes> <report> PYTHON_PASSWORD_HARDCODED 33d164
u.set_password('new password')

from django.contrib.auth import authenticate
# <yes> <report> PYTHON_PASSWORD_EMPTY 17kf67
user = authenticate(username='john', password='')


# Взяла все возможные варианты подключения к бд из http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
import MySQLdb
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="john",         # your username
                     # <yes> <report> PYTHON_PASSWORD_HARDCODED 17kf65
                     passwd="megajonhy",  # your password
                     db="jonhydb")
import peewee
from peewee import *
# <yes> <report> PYTHON_PASSWORD_EMPTY 17kf67
db = MySQLDatabase('jonhydb', user='john',passwd='')

import mysql.connector  
# <yes> <report> PYTHON_PASSWORD_HARDCODED 17kf65
cnx = mysql.connector.connect(user='scott', password='tiger',
                              host='127.0.0.1',
                              database='employees')
self._userCreationLoop(
            uname=user1,
            host='localhost',
            # <yes> <report> PYTHON_PASSWORD_HARDCODED 17kf65
            password='pwd`\'"1',
            new_password='pwd`\'"1b',
            connection_user=self.user,
            connection_pass=self.password
        )

password_sql = '%(password)s'

import django.utils.crypto
# <yes> <report> PYTHON_PASSWORD_EMPTY 1kmm67
hash = pbkdf2('', salt, iterations, digest=self.digest)
# <yes> <report> PYTHON_PASSWORD_EMPTY 17kf67
hash = pbkdf2(password='', salt, iterations, digest=self.digest)

import hashlib
# <yes> <report> PYTHON_PASSWORD_NULL yuca99
hashlib.pbkdf2_hmac('sha256', None, salt, 100000)

# <yes> <report> PYTHON_PASSWORD_HARDCODED 17kf65
hash = pbkdf2(password='word', salt, iterations, digest=self.digest)

# <yes> <report> PYTHON_PASSWORD_HARDCODED the7ts
hash = pbkdf2('word', salt, iterations, digest=self.digest)





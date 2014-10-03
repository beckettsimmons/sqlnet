sqlnet
======

A DB API v2.0 compatible wrapper to .NET SqlClient


What is it?
-----------

sqlnet aims to bring the ease and eloquence of python. It is designed to be compliant with the Python Database API Specification v2.0 as described in PEP-249_, so it is consistent with many other python database connectivity modules.

One main motivation for this project is the ease of Windows Authentication. You are not forced to pass usernames and password in the connection string.

This project it still very much a work in progress and current only partially implements the DB-API. Also, it is still horribly slow as it has to translate code to .NET through the pythonnet package and has yet been optimized for that.

Installation
------------

sqlnet depends very closely with the pythonnet_ package. Therefore; pythonnet is the only dependency needed. 

Unfortunately, pythonnet must be installed manually and is only fully supported on Windows (Running under Mono in Linux still has problems). Read `this page <http://pythonnet.sourceforge.net/readme.html>`_ 
for more details with installing pythonnet

Once all dependencies are installed, simply install sqlnet with::

    $pip install sqlnet


Example
-------

>>> import sqlnet
>>> connection = sqlnet.connect(
...     host='.\TEST_DATABASE',
...     user='user1',
...     db='testing',
...     trusted_connection='yes'
... )
>>> cursor = con.cursor()
>>> cursor.execute("CREATE TABLE test_table(pid int, name varchar(32));")
>>> cursor.execute("INSERT INTO test_table (pid, name) values (4, 'John Doe');")
>>> cursor.execute("SELECT * FROM ;")
>>> for row in cursor:
...     print row
[4, u'John Doe']
>>> connection.commit()

Licensing
---------

Please see the file called LICENSE_.

.. _SqlClient: http://msdn.microsoft.com/en-us/library/System.Data.SqlClient(v=vs.110).aspx

.. _pythonnet: http://pythonnet.sourceforge.net/

.. _PEP-249: http://legacy.python.org/dev/peps/pep-0249/

.. _LICENSE: ./LICENSE

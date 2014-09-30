import mock
import sys

# Some hackery here. Replacing the whole SqlClient module with Mock objects.
sql_mock = mock.MagicMock()  
# Get the connect() method to return another magic mock.
sql_mock.SqlConnection.connect = mock.MagicMock(return_value=mock.MagicMock())
sys.modules['System.Data.SqlClient'] = sql_mock

import dbapi20
import unittest
import sqlnet

class TestComplianceSqlnet(dbapi20.DatabaseAPI20Test):
    driver = sqlnet
    connect_args = ()
    connect_kw_args = {'dsn': 'dbname=dbapi20_test'}

    def setUp(self):
        dbapi20.DatabaseAPI20Test.setUp(self)

    def tearDown(self):
        pass
        ##dbapi20.DatabaseAPI20Test.tearDown(self)

if __name__ == '__main__':
    unittest.main()


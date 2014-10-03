import mock
import sys

# Some hackery here. Replacing the whole SqlClient with Mock objects.
# Maybe this isn't the easiest way to be mocking everythign out...
sql_mock = mock.MagicMock()  
# Get the connect() method to return another magic mock.
sql_mock.SqlConnection.connect = mock.MagicMock(
    return_value=mock.MagicMock()
)
# Mock out command to return a command reader.
def get_reader():
    reader_mock = mock.MagicMock()
    reader_mock.Read = mock.MagicMock(side_effect=[True, False])
    reader_mock.FieldCount = 1
    reader_mock.GetValue = mock.MagicMock(
        return_value='dummy field value'
    )
    return reader_mock

command_mock = mock.MagicMock()
command_mock.ExecuteReader = mock.MagicMock(side_effect=get_reader)
sql_mock.SqlCommand = mock.MagicMock(
    return_value=command_mock
)
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


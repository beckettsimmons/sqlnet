import mock
import unittest

import sqlnet
import dbapi20

class TestComplianceSqlnet(dbapi20.DatabaseAPI20Test):
    driver = sqlnet
    connect_args = ()
    connect_kw_args =dict(
        host='.\\TESTING',
        user='user',
        db='testing',
        trusted_connection='yes'
    )

    def setUp(self):
        dbapi20.DatabaseAPI20Test.setUp(self)

    def tearDown(self):
        dbapi20.DatabaseAPI20Test.tearDown(self)

if __name__ == '__main__':
    unittest.main()


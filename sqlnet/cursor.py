import clr

clr.AddReference('System.Data')
from System.Data.SqlClient import SqlCommand

from result import Result

class Cursor(object):
    """ sqlnet database cursor class.

    This class facilitates the retrieval, addition, removal, etc, of
    database records.
    """

    def __init__(self, connection, transaction):
        """ Initialise, just save connection """
        self.connection = connection
        self.transaction = transaction
        self.result = None


    def execute(self, sql):
        """ Prepare a database query or command.

        Args:
            sql (str): A SQL database query or command.

        Returns:
            Cursor: DB-API compliant cursor class.
        """
        self.command = SqlCommand(sql, self.connection, self.transaction)
        self.go()
        self.result = Result(self)

        return self

    def fetchone(self):
        return self.result.fetchone()

    def __iter__(self):
        """ Yield next value in the command result. """
        yield self.fetchone()

    def go(self):
        """ Actually execute/commit cursor command on database. """
        self.command.ExecuteNonQuery()

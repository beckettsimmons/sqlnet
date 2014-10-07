import clr

clr.AddReference('System.Data')
from System.Data.SqlClient import SqlCommand

from utils import use_docstring_from
from result import Result

class Cursor(object):
    """ sqlnet database cursor class.

    This class facilitates the retrieval, addition, removal, etc, of
    database records.
    """

    def __init__(self, connection):
        """ Initialise, just save connection """
        self.connection = connection
        self.result = None
        self.array_size = 1


    def execute(self, sql):
        """ Prepare a database query or command.

        Args:
            sql (str): A SQL database query or command.

        Returns:
            Cursor: DB-API compliant cursor class.
        """
        self.command = SqlCommand(
            sql,
            self.connection.connection,
            self.connection.transaction
        )
        self.result = Result(self)

        return self

    @use_docstring_from(Result.fetchone)
    def fetchone(self):
        return self.result.fetchone()

    @use_docstring_from(Result.fetchmany)
    def fetchmany(self, size=None):
        return self.result.fetchmany(size)

    @use_docstring_from(Result.fetchall)
    def fetchall(self):
        return self.result.fetchall()

    def __iter__(self):
        """ Yield next value of the command result. """
        row = self.fetchone()
        while row != None:
            yield row
            row = self.fetchone()

    def go(self):
        """ Actually execute/commit cursor command on database. """
        self.command.ExecuteNonQuery()

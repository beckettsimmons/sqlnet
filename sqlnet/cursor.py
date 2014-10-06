import clr

clr.AddReference('System.Data')
from System.Data.SqlClient import SqlCommand

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

    def fetchone(self):
        """ Fetches the next result from last command. """
        return self.result.fetchone()

    def fetchmany(self, size=None):
        """ Fetches number of rows from last command specified by size.

        Args:
            size (int, optional): Number of rows to fetch.
                If size exceeds the amount of remaining rows in the
                result, returns remaining rows.
                If no size given, default is cursor.array_size.
        """
        return self.result.fetchmany(size)

    def fetchall(self):
        return self.result.fetchall()

    def __iter__(self):
        """ Yield next value in the command result. """
        yield self.fetchone()

    def go(self):
        """ Actually execute/commit cursor command on database. """
        self.command.ExecuteNonQuery()

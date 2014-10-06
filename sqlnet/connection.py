import clr

clr.AddReference('System.Data')

from System.Data.SqlClient import SqlConnection
from cursor import Cursor

class Connection(object):
    """ The sqlnet database conection class. """

    from sqlnet_exceptions import Warning, Error, InterfaceError,\
        DataError, DatabaseError, OperationalError, IntegrityError,\
        InternalError, NotSupportedError, ProgrammingError

    def __init__(self, *args, **kwargs):
        """ Initialise from arguments given. """
        self.connection = self.create_connection(*args, **kwargs)
        self.connection.Open()

        # Immediately create a new transaction.
        self.transaction = self.connection.BeginTransaction()

        # Turn off auto-commit.
        cursor = self.cursor()
        cursor.execute('SET IMPLICIT_TRANSACTIONS ON;')

    def cursor(self):
        """ Create and return a new cursor.

        Returns:
            Cursor: DB-API compliant cursor class.
        """
        return Cursor(self)
    
    def create_connection(*args, **kwargs):
        """ Create a database connection based on arguments.

        Arguments further documented in sqlnet.connect() method.
        """
        connection_string = ""

        # Parse host param
        host = kwargs.get('host', None)
        if host != None:
            connection_string += "Server={host};".format(host=host)

        # Parse database param.
        database = kwargs.get('db', None)
        if database != None:
            connection_string += "Database={database};".format(
                database=database
            )

        # Parse trusted_connection param.
        trusted_connection = kwargs.get('trusted_connection', False)
        connection_string +=\
            "Trusted_Connection={trusted_connection};".format(
                trusted_connection=trusted_connection
            )

        return SqlConnection(connection_string)

    # TODO: This should be fleshed out so that we can quickly parse params.
    def parse_param(self, param_name):
        pass

    def close(self):
        """ Closes self.connection and renders it unusable. """
        self.connection.Close()

    def commit(self):
        """ Commit current transaction to database and begin new one. """
        # Commit the current transaction on the connection.
        self.transaction.Commit()

        # Create new transaction because each transaction can
        # only be used once.
        self.transaction = self.connection.BeginTransaction()

    def rollback(self):
        """ Roll back the current transaction. """
        self.transaction.Rollback()

        # Create new transaction because each transaction can
        # only be used once.
        self.transaction = self.connection.BeginTransaction()


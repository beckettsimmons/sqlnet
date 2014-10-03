""" Beginnings of a SQL .NET DB-API.

Not even close to being DB-API 2.0 complient, but for now we'll wing it.
"""

from connection import Connection

from sqlnet_exceptions import Warning, Error, InterfaceError,\
    DataError, DatabaseError, OperationalError, IntegrityError,\
    InternalError, NotSupportedError, ProgrammingError

# Globals
threadsafety = 1
apilevel = "2.0"
paramstyle = "format"

def connect(*args, **kwargs):
    """ Constructor for creating a database connection class.

    Keyword Args:
        host (str): name of host to connect to.
        db (str): name of database to connect to.
        trusted_connection (str): Wether or not to used Windows
            Authentication. Either "yes" or "no".

    Returns:
        Connection: Python DB-API compliant database connection class.
    """

    return Connection(*args, **kwargs)

__all__ = [
    'connect',

    'threadsafety', 'apilevel', 'paramstyle',

    'Warning', 'Error', 'InterfaceError', 'DataError', 'DatabaseError',
    'OperationalError', 'IntegrityError', 'InternalError',
    'NotSupportedError', 'ProgrammingError',
]

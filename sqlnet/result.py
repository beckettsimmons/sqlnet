class Result():
    """ A result object created by Cursor query execution. """

    def __init__(self, cursor):
        self.cursor = cursor
        self.rows = self.init_rows()
        self.row_index = 0
        self.row_count = len(self.rows)

    def init_rows(self):
        """ Initialize result rows from command. """
        reader = self.cursor.command.ExecuteReader()
        rows = []
        # For each row in table. Append list of all field values.
        while reader.Read():
            rows.append(
                [
                    reader.GetValue(ii) for ii in range(
                        reader.FieldCount
                    )
                ]
            )
        reader.Close()
        tuple(rows)
        return rows

    def fetchone(self):
        """ Fetch next row from the result of the last command. """
        # If no more rows left to fetch, return none.
        if self.row_index + 1 > self.row_count - 1:
            return None

        self.row_index += 1
        return self.rows[self.row_index]

    def fetchmany(self, size):
        """ Like fetchone, but fetches the specified number of rows.

        Args:
            size (int, optional): Number of rows to fetch.
                If size exceeds the amount of remaining rows in the
                result, returns remaining rows.
                If no size given, default is cursor.array_size.
        """
        rows = []
        for i in range(size):
            row = self.fetchone()
            if row == None:
                break
            rows.append(row)

        tuple(rows)
        return rows

    def fetchall(self):
        """ Like fetchmany, but fetches all of the remaining rows. """
        return self.fetchmany(len(self.rows))

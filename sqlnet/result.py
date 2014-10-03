class Result():
    """ A result object created by Crusor query execution. """

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
        """ Return current row from self.rows """
        
        # If no more rows left to fetch, return none.
        if self.row_index + 1 > self.row_count - 1:
            return None

        self.row_index += 1
        return self.rows[self.row_index]

# sqlite_lib : SQLite3 helper library

## Information

### Module
+ Type: Library/module

### Description
+ Library containing various SQLite3 Relational Database helper/support functions and objects for improving the efficacy of implementing SQLite3 in python projects

## Documentations

### Packages
- pyutils.libraries

### Modules
- pyutils.libraries
    - `.sqlite_lib`

### Classes
- pyutils.libraries.sqlite_lib

### Data Types/Objects
- sqlite3
    - `.Connection()`
        + `.Cursor()`

### Functions
- pyutils.libraries.sqlite_lib
    - `.open_db(db_Name="file.db")`: Open Database file and return object
        - Parameter Signature/Headers
            - db_Name : The name of the database file (.db|.sqlite3) to open and read
                + Type: String
                + Default Value: "file.db"

        - Return
            - con : The SQLite3 Connection Object
                + Type: sqlite3.Connection()

    - `.convert_Dictionary(search_Res:list, columns:list)`: Convert search result list into dictionary, with each result mapped to the column name according to the index
        - Parameter Signature/Headers
            - search_Res : Specify the list of search results you returned from the query
                + Type: List

            - columns : Specify list of all columns used in the search query to obtain the search result list
                + Type: List

        - Return
            - new_dict : A new dictionary object containing the query results iteratively mapped to the column name according to the index of the query result element
                + Type: Dictionary

    - `.generate_Cursor(con)`: Generate the cursor pointing to the database connection object (i.e. like a mouse in a GUI application thats used to point to a memory address containing the database data)
        - Parameter Signature/Headers
            - con : The SQLite3 Connection Object
                + Type: sqlite3.Connection()

        - Return
            - cur : The SQLite3 Database Connection cursor/pointer object
                + Type: sqlite3.Connection().Cursor()

    - `.close_Connection(con)`: Close the SQLite3 Connection
        - Parameter Signature/Headers
            - con : The SQLite3 Connection Object
                + Type: sqlite3.Connection()

    - `.close_Cursor(cur)`: Close the SQLite3 Database Connection Cursor object
        - Parameter Signature/Headers
            - cur : The SQLite3 database connection cursor/pointer object you wish to close
                + Type: sqlite3.Connection().Cursor()

    - `.execute_command(cur, cmd_str)`: Execute SQL command only
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor
            - cmd_str : The command string you wish to execute
                + Type: String

    - `.execute_and_fetch(cur, cmd_str)`: Execute SQL command and fetch the result
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor
            - cmd_str : The command string you wish to execute
                + Type: String
        - Return
            - rows : Return all rows returned from the query fetch
                + Type: List

    - `.get_Values(cur, table_Name, col_Name="*")`: Query and retrieve values of the specified column from the specified table
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor

            - table_Name : Specify the table name you wish to query from
                + Type: string

            - col_Name : Specify the target column within the table you wish to query
                + Type: String
                + Default Value: "*"

        - Return
            - rows : List containing all the results of the query from the database table
                + Type: List

    - `.get_first_Value(cur, table_Name, col_Name="*")`: Query and retrieve the first result of the specified column from the specified table
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor

            - table_Name : Specify the table name you wish to query from
                + Type: string

            - col_Name : Specify the target column within the table you wish to query
                + Type: String
                + Default Value: "*"

        - Return
            - row : String containing the first result returned from the querying of the database
                + Type: String

    - `.get_Ascending(cur, table_Name, cols, order="")`: Obtain the highest/greatest value in a column of a table
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor

            - table_Name : Name of the table to target
                + Type: String

            - cols : List of all columns to retrieve
                + Type: List

            - order : The order condition; specify the column to order with
                + Type: String

        - Return Output
            - rows : List containing all the results of the query from the database table
                + Type: List

    - `.get_Descending(cur, table_Name, cols, order="")`: Obtain the highest/greatest value in a column of a table
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor

            - table_Name : Name of the table to target
                + Type: String

            - cols : List of all columns to retrieve
                + Type: List

            - order : The order condition; specify the column to order with
                + Type: String

        - Return
            - rows : List containing all the results of the query from the database table
                + Type: List

    - `.get_all_Tables(cur)`: List all tables
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                Type: SQLite3.Cursor

        - Return
            - rows: Get all values from the querying of the table 'sqlite_master'
                + Type: List

    - `.get_row_ID(cur, table_Name, col_Name, filter_Val)`: Find the row ID/number of the specified filter string within the column of a table
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor

            - table_Name : Name of the table to target
                + Type: String

            - cols : List of all columns to retrieve
                + Type: List

            - filter_Val : The target filter keyword string you wish to check if is in the table query results
                + Type: String

        - Return
            - row_id : List of all Row IDs within the target table (+ column) that contains the provided filter keyword string
                + Type: List

    - `.get_Conditional(cur, table_Name, result_Cols, filter_Conditions:dict)`: Search and get a specified filter value/condition in a table
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor

            - table_Name : Name of the table to target
                + Type: String

            - result_Cols : List of all columns to retrieve
                + Type: List

            - filter_Conditions : Key-Value (Dictionary) mapping of the search/conditional columns and values
                + Type: Dictionary

        - Return
            - rows : List containing all the results of the query from the database table
                + Type: List

    - `.search_Value(cur, table_Name, result_Cols, filter_Col, filter_Value)`: Search for a specified filter value/condition in a table
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor

            - table_Name : Name of the table to target
                + Type: String

            - result_Cols : List of all columns to retrieve
                + Type: List

            - filter_Col : List of columns you wish to "filter" and search for; must match the number of elements as 'filter_Value'
                + Type: List

            - filter_Value : List of values corresponding to the element index(es)/position of 'filter_Col' that you wish to filter and search for; must match the number of elements as 'filter_Col'
                + Type: List

        - Return
            - rows : List containing all the results of the query from the database table
                + Type: List

    - `.create_Table(cur, table_Name, table_Columns)`: Create a new table in the database
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor

            - table_Name : Name of the table to target
                + Type: String

            - table_Columns : String containing the database table schema/definitions
                + Type: String
                + Format Structure: [table_name] [data_type] [NULL|NOT NULL] [PRIMARY|FOREIGN KEY] [constraints] 
                - Examples:
                    1. "row_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
                        table_1_string TEXT
                        table_2_integer int NOT NULL"

    - `.validate_table_Exists(cur, table_Name)`: Query and check if table exists in the database
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor

            - table_Name : Name of the table to target
                + Type: String

        - Return
            - table_Exists : Flag if table exists or not
                + Type: Boolean

    - `.insert_Row(con, cur, target_Table, new_Data=None, index=-1, commit=False)`: Insert a new row between existing rows in the database (C.R.U.D, Update)
        - Parameter Signature/Headers
            - Positionals
                - con : The SQLite3 connection object created after opening the database
                    + Type: SQLite3.Connection
                - cur : The cursor generated from an SQLite connection object
                    + Type: SQLite3.Cursor
                - target_Table : The table to insert into
                    + Type: String
            - Optionals
                - new_Data : List of all rows to insert/append into the table
                    + Type: List of Lists
                    + Default Value: None
                - index : The index position to insert into; Enter '-1' to append as the newest element
                    + Type: Integer
                    + Default Value: -1
                - commit : Flag to automatically commit/dont commit
                    + Type: Bool
                    + Default Value: False

        - Return
            - The number of rows affected
                + Type: Integer

    + `.update_Row()`: Update/Modify/Replace data in a row (C.R.U.D - Update) (TODO)
    + `.delete_Row()`: Delete a row from a table in the database (C.R.U.D - Delete) (TODO)

    - `.filter_Highest(cur, table_Name, cols, order="")`: Obtain the highest/greatest value in a column of a table
        - Parameter Signature/Headers
            - cur : The cursor generated from an SQLite connection object
                + Type: SQLite3.Cursor
            - table_Name : Name of the table to target
                + Type: String
            - cols : List of all columns to retrieve
                + Type: List
            - order : The order condition; specify column and ASC for Ascending and DESC for Descending
                + Type: String
                + Default Values: ""
        - Return
            - row : String containing the first result returned from the querying of the database
                + Type: String


### Attributes/Variables


### Usage
- Database C.R.U.D operations
    ```python
    import os
    import sys
    from pyutils.libraries.sqlite_lib import sqlite3, validate_table_Exists, get_Values, get_row_ID, get_all_Tables, create_Table, insert_Row, close_Cursor, close_Connection

    def main():
        # Initialize Variables
        con = None 
        cur = None
        db_Path = "/path/to/db"
        db_Name = "file.db"
        db_fullName = "{}/{}".format(db_Path, db_Name)
        database_Schema = {
            "tables" : [
                # Keys = 
                #   - row_id
                #   - table_Name
                #   - table_Columns
                {"row_id" : 0, "table_Name" : "movie", "table_Columns" : "title, year, score"}
            ]
        }
        database_Tables = database_Schema["tables"]

        # Check null value
        if (db_Path != None) and (db_Name != None):
            # Check if database exists
            if not os.path.isfile(db_fullName):
                # File does not exist
                print("Database {} does not exist, creating...".format(db_Name))

            try:
                """
                Connect to SQLite3 database and return the connection object
                """
                con = sqlite3.connect(db_Name)

                print("[+] Connected to database: {}".format(db_Name))

                """
                Generate the cursor pointing to the database connection object
                - i.e. 
                    - like a mouse in a GUI application thats used to point to a memory address containing the database data
                """
                cur = con.cursor()

                print("[+] Cursor has been generated.")

                """
                Create database table(s)
                """
                print("=====================")
                print("Create Database Table")
                print("=====================")

                for table_id in range(len(database_Tables)):
                    # Get current table
                    curr_table = database_Tables[table_id]

                    # Get table schema
                    table_Name = curr_table["table_Name"]
                    table_Columns = curr_table["table_Columns"]

                    # Check table exists
                    print("Verifying table [{}] exists...".format(table_Name))
                    if validate_table_Exists(cur, table_Name):
                        print("[-] table {} is in database.".format(table_Name))
                    else:
                        # Create table
                        # Execute SQL command
                        print("table [{}] does not exists, creating table...".format(table_Name))
                        create_Table(cur, table_Name, table_Columns)

                        # Verify new table has been created
                        if validate_table_Exists(cur, table_Name):
                            print("[+] table {} has been created.".format(table_Name))
                        else:
                            print("[-] error creating table {}".format(table_Name))

                    print("")

                """
                List all tables
                """
                print("===============")
                print("List all tables")
                print("===============")
                res_All = get_all_Tables(cur)
                print("All Tables: {}".format(res_All))

                """
                Insert Data
                """
                target_Table = "movie"
                new_Data = [('Monty Python and the Holy Grail', 1975, 8.2), ('And Now for something completely different', 1971, 7.5)]
                rows_Affected = insert_Row(con, cur, target_Table, new_Data, commit=True)
                print("Rows Affected: {}".format(rows_Affected))

                """
                List all data in table
                """
                target_Table = "movie"
                target_Columns = "*"
                # Fetch all results from the result output
                out = get_Values(cur, target_Table, target_Columns)

                print("==============")
                print("List all Rows")
                print("==============")
                print(out)

                """
                Get Row ID of the search value
                """
                # Fetch row id
                row_id = get_row_ID(cur, target_Table, "year", "1971")

                if len(row_id) == 0 :
                    print("No rows returned.")
                else:
                    print("Row ID: {}".format(row_id))
            except Exception as ex:
                print("[-] Exception caught: {}".format(ex))
            finally:
                # Close SQLite3 connection cursor after use
                close_Cursor(cur)

                # Close SQLite3 connection after use
                close_Connection(con)
        else:
            print("Empty file path/name provided: [Path: {}, Name: {}]".format(db_Path, db_Name))

    if __name__ == "__main__":
        main()
    ```

## Wiki

## Resources

## References

## Remarks


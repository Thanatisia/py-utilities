import os
import sys
import pypkgs.libraries.sqlite_lib as sqlite_lib

def test_sqlite_lib():
    """
    Test library 'sqlite_lib'
    """
    # Initialize Variables
    con = None 
    cur = None
    db_Path = "."
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
            con = sqlite_lib.open_db(db_Name)

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
                if sqlite_lib.validate_table_Exists(cur, table_Name):
                    print("[-] table {} is in database.".format(table_Name))
                else:
                    # Create table
                    # Execute SQL command
                    print("table [{}] does not exists, creating table...".format(table_Name))
                    sqlite_lib.create_Table(cur, table_Name, table_Columns)

                    # Verify new table has been created
                    if sqlite_lib.validate_table_Exists(cur, table_Name):
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
            res_All = sqlite_lib.get_all_Tables(cur)
            print("All Tables: {}".format(res_All))

            """
            Insert Data
            """
            target_Table = "movie"
            new_Data = [('Monty Python and the Holy Grail', 1975, 8.2), ('And Now for something completely different', 1971, 7.5)]
            rows_Affected = sqlite_lib.insert_Row(con, cur, target_Table, new_Data, commit=True)
            print("Rows Affected: {}".format(rows_Affected))

            """
            List all data in table
            """
            target_Table = "movie"
            target_Columns = "*"
            # Fetch all results from the result output
            out = sqlite_lib.get_Values(cur, target_Table, target_Columns)

            print("==============")
            print("List all Rows")
            print("==============")
            print(out)

            """
            Get Row ID of the search value
            """
            # Fetch row id
            row_id = sqlite_lib.get_row_ID(cur, target_Table, "year", "1971")

            if len(row_id) == 0 :
                print("No rows returned.")
            else:
                print("Row ID: {}".format(row_id))
        except Exception as ex:
            print("[-] Exception caught: {}".format(ex))
        finally:
            # Close SQLite3 connection cursor after use
            sqlite_lib.close_Cursor(cur)

            # Close SQLite3 connection after use
            sqlite_lib.close_Connection(con)
    else:
        print("Empty file path/name provided: [Path: {}, Name: {}]".format(db_Path, db_Name))

def debug():
    """
    Unit Test
    """
    # Initialize Variables
    unit_test_Menu = {
        0 : ["Exit", None],
        1 : ["sqlite_lib.py", test_sqlite_lib]
    }

    def print_unit_Tests():
        for k,v in unit_test_Menu.items():
            print("{} => {}".format(k,v[0]))

    # Create a menu to loop and process what application to run
    while True:
        # Print out all tests
        print_unit_Tests()

        # Try to get user's test ID
        try:
            test_ID = int(input("Which test would you like to run?: "))

            if test_ID == 0:
                # Break condition
                break
            else:
                # Get test function
                unit_test_Values = unit_test_Menu[test_ID]
                unit_test_Func = unit_test_Values[1]

                # Process test ID
                unit_test_Func()
        except Exception as ex:
            print("Invalid test option: [{}]".format(ex))

        # Print new line
        print("")


if __name__ == "__main__":
    debug()


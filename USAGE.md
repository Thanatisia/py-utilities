# USAGE and Recipes

## Table of Contents
- [Recipes](#recipes)
    - Packages
        - Libraries
            + [apg.py](#apg.py)
            + [mkparser.py](https://github.com/Thanatisia/makefile-parser-python/blob/main/USAGE.md)
            + [sqlite_lib.py](#sqlite_lib.py)
- [Scripts](#scripts)
    + de-duplicator.py

## Recipes
### Libraries
#### apg.py
- Simple Android project file structure
    ```python
    import os
    import sys
    from pypkgs.libraries import apg

    def main():
        # To initialize for a Windows environment
        apgEnv = apg.APGWindows()

        # To initialize for a Linux environment
        apgEnv = apg.APGLinux()

        # To initialize the Generator
        apgGen = apg.AndroidProjectGenerator()

        # To setup environment
        apgEnv.setup_Env()
        
        # To download dependencies
        apgGen.dl_Dependencies()

        ## Generate template project structure
        apgGen.generate_template_Project 

        ## Populate project source files
        apgGen.populate_template_Project

        # Create gradle files
        apgGen.populate_build_Files

    if __name__ == "__main__":
        main()
    ```

#### sqlite_lib.py
- Database C.R.U.D operations
    ```python
    import os
    import sys
    from path.to.packages.libraries.sqlite_lib import sqlite3, validate_table_Exists, get_Values, get_row_ID, get_all_Tables, create_Table, insert_Row, close_Cursor, close_Connection

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

## Scripts
- de-duplicator
    - Setup
        - Dependencies
        - Pre-Requisites
    - Synopsis/Syntax
        ```console
        python -m pypkgs.scripts.de-duplicator {options} <arguments>
        ```
    - Parameters
        - Positionals
            1. Source filename
            2. dataset source : Specify this to indicate the URL's domain source; This is used to split and remove unnessary queries from links
                - yt | youtube : For URLs that uses youtube's domain (i.e. youtube.com/...?=search-queries)
                - none : Ignore; just remove duplicates and dont truncate/split
        - Optionals

- apg-generate
    - Information
        - Notes
            - Please refer to the main repository that holds this script [Thanatisia/android-project-generator python](https://github.com/Thanatisia/android-project-generator/tree/main/app/languages/python) for the latest updates
    - Setup
        - Dependencies
            - android-sdk
                + cmdline-tools
            + gradle
        - Pre-Requisites
            - Set environment variables in your shell
                - Linux
                    + `ANDROID_HOME="/path/to/android-sdk"`
                    + `ANDROID_USER_HOME="/path/to/user/home/.config/android"`
                    + `ANDROID_EMULATOR_HOME="[ANDROID_USER_HOME]/emulator"`
                    + `ANDROID_AVD_HOME="[ANDROID_USER_HOME]/avd"`
                    + `PATH+="[ANDROID_EMULATOR_HOME]:[ANDROID_HOME]/tools:[ANDROID_HOME]/platform-tools:[ANDROID_HOME]/cmdline-tools/latest/bin:"`
                - Windows
                    + `SET ANDROID_HOME="\path\to\android\sdk\root"`
                    + `SET ANDROID_USER_HOME="\path\to\user\home\.config\android"`
                    + `SET ANDROID_EMULATOR_HOME="[ANDROID_USER_HOME]\emulator"`
                    + `SET ANDROID_AVD_HOME="[ANDROID_USER_HOME]\avd"`
                    + `SET PATH="%PATH%;[ANDROID_EMULATOR_HOME];[ANDROID_HOME]\tools;[ANDROID_HOME]\platform-tools;[ANDROID_HOME]\cmdline-tools\latest\bin;"`
    - Synopsis/Syntax
        ```console
        python -m pypkgs.scripts.apg-generate {options} <arguments>
        ```
    - Parameters
        - Positionals
        - Optionals
    - Usage
        - Display help
            ```console
            python -m pypkgs.scripts.apg-generate --help
            ```



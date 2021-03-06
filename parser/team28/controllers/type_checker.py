from utils.decorators import singleton
from models.database import Database
from models.table import Table
from models.column import Column

from storageManager import jsonMode  # TODO Change storage manager


@singleton
class TypeChecker(object):  # TODO messages
    def __init__(self):
        self._typeCheckerList = []

    def getList(self):
        return self._typeCheckerList

    # --- Databases
    # Method to search a database in type checker
    def searchDatabase(self, databaseName: str) -> Database:
        for db in self._typeCheckerList:
            if db.name == databaseName:
                return db
        return None

    # Method to create a database in type checker
    def createDatabase(self, databaseName: str):
        dbStatement = jsonMode.createDatabase(databaseName)

        if dbStatement == 0:
            self._typeCheckerList.append(Database(databaseName))
            print('Database created successfully')
        elif dbStatement == 1:
            print(f"Can't create database '{databaseName}'")
        elif dbStatement == 2:
            print('Database exists')

    # Method to update the name of a database in type checker
    def updateDatabase(self, databaseOld: str, databaseNew: str):
        dbStatement = jsonMode.alterDatabase(databaseOld, databaseNew)

        if dbStatement == 0:
            database = self.searchDatabase(databaseOld)
            database.name = databaseNew
            print('Database updated successfully')
        elif dbStatement == 1:
            print(f"Can't update database '{databaseOld}'")
        elif dbStatement == 2:
            print("Database doesn't exist")
        elif dbStatement == 3:
            print(f"Database '{databaseNew}' already exists")

    # Method to remove a database in type checker
    def deleteDatabase(self, databaseName: str):
        dbStatement = jsonMode.dropDatabase(databaseName)

        if dbStatement == 0:
            database = self.searchDatabase(databaseName)
            self._typeCheckerList.remove(database)
            print('Database deleted successfully')
        elif dbStatement == 1:
            print(f"Can't drop database '{databaseName}'")
        elif dbStatement == 2:
            print("Database doesn't exist")

    # TODO def showDatabases

    # --- Tables
    # Method to search a table in database
    def searchTable(self, database: Database, tableName: str) -> Table:
        if database:
            for tb in database.tables:
                if tb.name == tableName:
                    return tb
            return None

        print('No database selected')
        return None

    # Method to create a table in database
    def createTable(self, database: Database, tableName: str, columns: int) -> Table:
        if not database:
            print('No database selected')
            return None

        dbStatement = 0  # j.createTable(database.name, tableName, columns)

        if dbStatement == 0:
            table = Table(tableName)
            database.tables.append(table)
            print('Table created successfully')
            return table
        elif dbStatement == 1:
            print(f"Can't create table '{tableName}'")
        elif dbStatement == 2:
            print("Database doesn't exist")
        elif dbStatement == 3:
            print(f"Table '{tableName}' already exists")
        return None

    # Method to update the name of a table in database
    def updateTable(self, database: Database, tableOld: str, tableNew: str):
        if not database:
            print('No database selected')
            return

        dbStatement = 0  # j.alterTable(database.name, tableOld, tableNew)

        if dbStatement == 0:
            table = self.searchTable(database, tableOld)
            table.name = tableNew
            print('Table updated successfully')
        elif dbStatement == 1:
            print(f"Can't update Table '{tableOld}'")
        elif dbStatement == 2:
            print("Database doesn't exist")
        elif dbStatement == 3:
            print(f"Table '{tableOld}' doesn't exist")
        elif dbStatement == 4:
            print(f"Table '{tableNew}' already exists")

    # Method to remove a table in database
    def deleteTable(self, database: Database, tableName: str):
        if not database:
            print('No database selected')
            return

        dbStatement = 0  # j.dropTable(database.name, tableName)

        if dbStatement == 0:
            table = self.searchTable(database, tableName)
            database.tables.remove(table)
            print('Table deleted successfully')
        elif dbStatement == 1:
            print(f"Can't drop table '{tableName}'")
        elif dbStatement == 2:
            print("Database doesn't exist")
        elif dbStatement == 3:
            print(f"Unknown table '{tableName}'")

    # TODO def definePK
    # TODO def defineFK
    # TODO def showTables

    # --- Columns
    # Method to search a column in table
    def searchColumn(self, table: Table, columnName: str) -> Column:
        if table:
            for col in table.columns:
                if col.name == columnName:
                    return col
        return None

    # Method to create a column in table
    def createColumnTable(self, table: Table, column: Column):
        if not self.searchColumn(table, column.name):
            table.columns.append(column)
            return
        print(f"Duplicate column name '{column.name}'")

    # Method to remove a database in type checker
    def deleteColumn(self, database: Database, tableName: Table, columnName: Column):
        if not database:
            print('No database selected')
            return

        dbStatement = 0  # TODO j.alterDropColumn(database.name,table.name,clN)

        if dbStatement == 0:
            table = self.searchTable(database, tableName)
            column = self.searchColumn(table, columnName)
            if column:
                table.remove(column)
                print('Column deleted successfully')
                return
            print(f"Can't DROP COLUMN `{columnName}` Check that it exists")
        elif dbStatement == 1:
            print(f"Can't DROP COLUMN `{columnName}`")
        elif dbStatement == 2:
            print("Database doesn't exist")
        elif dbStatement == 3:
            print(f"Unknown table '{tableName}'")
        elif dbStatement == 4:
            print('Out of range column')

    # Method to add a column in table
    def alterAddColumn(self, database: Database, table: Table, column: Column):
        if not database:
            print('No database selected')
            return

        dbStatement = 0  # j.alterAddColumn(database.name, table.name)

        if dbStatement == 0:
            if not self.searchColumn(table, column.name):
                table.columns.append(column)
                print('Table updated successfully')
                return
            print(f"Duplicate column name '{column.name}'")
        elif dbStatement == 1:
            print(f"Can't update Table '{table.name}'")
        elif dbStatement == 2:
            print("Database doesn't exist")
        elif dbStatement == 3:
            print("Table doesn't exist")

    # TODO def extractTable
    # TODO def extractRangeTable

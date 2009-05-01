from optparse import OptionParser
import sys

class CLI(object):

    color = {
        "PINK": "\033[95m", 
        "BLUE": "\033[94m", 
        "CYAN": "\033[96m",
        "GREEN": "\033[92m", 
        "YELLOW": "\033[93m", 
        "RED": "\033[91m",
        "GRAY": "\033[90m",
        "END": "\033[0m", 
    }

    def __init__(self):
        self.__config_parser()

    def __config_parser(self):
        self.__parser = OptionParser()

        self.__parser.add_option("-v", "--version", 
                dest="schema_version", 
                default=None, 
                help="Schema version to migrate to. If not provided will migrate to the last version available in the migrations directory.")
        
        self.__parser.add_option("-c", "--config", 
                dest="config_file", 
                default="simple-db-migrate.conf", 
                help="Use a specific config file. If not provided, will search for 'simple-db-migrate.conf' in the current directory.")
                        
        self.__parser.add_option("--showsql", 
                action="store_true", 
                dest="show_sql", 
                default=False, 
                help="Show all SQL statements executed.")

        self.__parser.add_option("--showsqlonly", 
                action="store_true", 
                dest="show_sql_only", 
                default=False, 
                help="Show all SQL statements that would be executed but DON'T execute them in the database.")

        self.__parser.add_option("--create", "--new", 
                dest="new_migration", 
                default=None, 
                help="Create migration file with the given nickname. The nickname should contain only lowercase characters and underscore '_'. Example: 'create_table_xyz'.")
                
        self.__parser.add_option("--drop", "--drop-database-first",
                action="store_true", 
                dest="drop_db_first", 
                default=False, 
                help="Drop database before running migrations to create everything from scratch. Useful when the database schema is corrupted and the migration scripts are not working.")

    def get_parser(self):
        return self.__parser

    def parse(self):
        return self.__parser.parse_args()
        
    def error_and_exit(self, msg):
        self.msg("[ERROR] %s\n" % msg, "RED")
        sys.exit(1)
        
    def info_and_exit(self, msg):
        self.msg("%s\n" % msg, "BLUE")
        sys.exit(0)
    
    def msg(self, msg, color="CYAN"):
        print "%s%s%s" % (self.color[color], msg, self.color["END"])

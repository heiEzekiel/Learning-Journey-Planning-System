#Just run the script to test and rmb to pip install libs
import unittest, time
from sqlalchemy.sql import text
from tests.frontend_test.db import engine as temp_engine
from backend.content_updater import main as cu_main
    
class Reset_DB(unittest.TestCase):
    def test_temp(self):
        def read_file(filename):
            fh = open(filename, "r")
            try:
                return fh.read()
            finally:
                fh.close()
        sql_query = read_file("test_related_db/LJPS_demo.sql")
        engine = temp_engine
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql = str(text(sql_query))
        text_list = sql.split(";")
        for row in text_list:
            if row != "":
                row = row + ";"
                cursor.execute(row)
                connection.commit()
        cursor.close()
        connection.close()
        
        cu_main
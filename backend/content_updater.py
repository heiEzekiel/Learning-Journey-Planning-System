from sqlalchemy import create_engine as ce
import pandas as pd
import os
mysql_engine = ce("mysql+mysqlconnector://admin:SoftwareProject@spm.czdb9a0r4ea9.ap-southeast-1.rds.amazonaws.com:3306/LJPS_DB")
#mysql_engine = ce("mysql+mysqlconnector://root@localhost:3306/LJPS_DB")

# import contextlib
# from sqlalchemy import MetaData

# meta = MetaData()

# with contextlib.closing(mysql_engine.connect()) as con:
#     trans = con.begin()
#     for table in reversed(meta.sorted_tables):
#         con.execute(table.delete())
#     trans.commit()

dir = os.path.join(os.getcwd(), "raw_data")
files = os.listdir(dir) 
last = files.pop(1)
files.append(last)
for file in files:
    table_name = file.split(".")[0].capitalize()
    sql_query = "select * from " + table_name + ";"
    sqldf = pd.read_sql(sql_query, mysql_engine)
    csv_file = os.path.join(dir,file)
    df = pd.read_csv(csv_file, encoding_errors='ignore', index_col=False)
    df = df.fillna('')
    df.columns = map(str.lower, df.columns)
    if table_name == "Registration":
        sqldf["reg_id"]=sqldf["reg_id"].apply(str)
        df["reg_id"]=df["reg_id"].apply(str)
        df = df[~df["reg_id"].isin(sqldf["reg_id"])]
    df = df.merge(sqldf, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
    df.to_sql(table_name, mysql_engine, if_exists='append', index=False)
    print(table_name, "done!")
print("\nAll Tables Updated!")
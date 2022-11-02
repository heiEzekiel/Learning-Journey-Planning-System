import sqlalchemy
engine = sqlalchemy.create_engine("mysql+mysqlconnector://root@localhost:3306/LJPS_DB")
#engine = sqlalchemy.create_engine("mysql+mysqlconnector://admin:SoftwareProject@spm.czdb9a0r4ea9.ap-southeast-1.rds.amazonaws.com:3306/LJPS_DB")
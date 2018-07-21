SECRET_KEY = 'CHANGE_ME'
# database connection uri
#SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://appdb/Pass_Word_2018@129.146.166.76:1521/pdb1.sub07182009420.gartnerdemovcn.oraclevcn.com'
#SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://appdb/Pass_Word_2018@mydb'

SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://appdb:Pass_Word_2018@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=129.146.166.76)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=pdb1.sub07182009420.gartnerdemovcn.oraclevcn.com)))'

STATIC_ROOT = None



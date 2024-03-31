from dotenv import dotenv_values

env_vars = dotenv_values('.env')
# print(env_vars)
_dbhost=env_vars["dbhost"]
_dbuser=env_vars["dbuser"]
_dbpass=env_vars["dbpass"]


mysql_config = {
    'db_host': _dbhost,
    'db_user': _dbuser,
    'db_pwd': _dbpass,
    'db': 'test_db',
    'db_port': 3306,
}

from MySQLEngine import DBInterface

if __name__ == "__main__":
  mysql_db = DBInterface()
  mysql_connection = mysql_db.result_engine
  table="t_table1"
  data={'id':int(item['id']),'username':int(item['username'])}
  mysql_connection.update(table,data)
  print("数据已成功存储MySQL数据库中。")
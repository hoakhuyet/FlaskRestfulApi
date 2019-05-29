import pymysql.cursors
import datetime

conn = pymysql.connect(host='localhost', user='neik', password='123', db='db1', cursorclass=pymysql.cursors.DictCursor)

def _login(username, password):
	with conn.cursor() as cursor:
		sql = "SELECT * FROM account"
		cursor.execute(sql)
		records = cursor.fetchall()
		for row in records:
			if username == row['username'] and password == row['password']:
				return True
	return False

def _message(user, message):
	currentDateTime = datetime.datetime.now()
	with conn.cursor() as cursor:
		sql = "INSERT INTO message (date, user, message) VALUES (\'" + str(currentDateTime) + "\',\'" + user + "\',\'" + message + "\')"
		result = cursor.execute(sql)
		conn.commit()
	return result

def _getMessage(id_message):
	data = list()
	with conn.cursor() as cursor:
		sql = "SELECT * FROM message WHERE id >" +  id_message
		result = cursor.execute(sql)
		records = cursor.fetchall()
		for row in records:
			data.append(row)
	return data


def _userlog(ip, user, request, action, status):
	currentDateTime = datetime.datetime.now()
	with conn.cursor() as cursor:
		sql = "INSERT INTO userlog (ip, time, user, action, request, status) VALUES (\'"+ ip + "\', \'" + str(currentDateTime) + "\', \'" + user + "\', \'" + action + "\', \'" + request + "\', \'" + status + "\')"
		cursor.execute(sql)
		conn.commit()
	return sql

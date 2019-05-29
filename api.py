import logging
from flask import Flask, render_template, json, jsonify, request, Response
from server import _login, _message, _getMessage, _userlog

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('login.html')

@app.route('/chatserver', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if _login(username, password):
		_userlog(request.remote_addr, username, request.method + request.full_path,  "login", "success")
		return render_template('message.html', result = username)
	else:
		_userlog(request.remote_addr, username, request.method + request.full_path,  "login", "failed")
		return render_template('login.html')


@app.route('/message', methods=['GET'])
def message():
	user = request.args.get('user')
	message = request.args.get('message')
	_message(user, message)
	_userlog(request.remote_addr, user, request.method + request.full_path,  "send message", "success")
	return Response(status=200)

@app.route('/getmessage', methods=['GET'])
def get_message():
	id_message = request.args.get('id_message')
	data = _getMessage(id_message)
	return jsonify(data)
if __name__ == '__main__':
	app.run(host='0.0.0.0')

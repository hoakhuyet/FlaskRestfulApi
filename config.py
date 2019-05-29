class Response(object):

 SUCCESS = {'code': 200, 'message': 'Success.'}
 ERROR = {'code': 500, 'message': 'Fail.'}
 NOT_FOUND = {'code': 404, 'message': 'Not found.'}

 def __init__(self):
   self.code = 0
   self.message = ''
   self.data = {}

 def create(self, params, data={}):
   self.code = params['code']
   self.message = params['message']
   self.data = data

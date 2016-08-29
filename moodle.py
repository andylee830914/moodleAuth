from jupyterhub.auth import Authenticator
from jupyterhub.auth import PAMAuthenticator
from tornado import gen
import urllib.parse
import urllib.request
import json

class NCKUAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
        nckumoodle='http://moodle.ncku.edu.tw/login/token.php'
        moodle = {'username' : data['username'], 'password' : data['password'],'service':'ncku_moodle_app'}
        moodledata = urllib.parse.urlencode(moodle)
        moodledata = moodledata.encode('ascii')
        req = urllib.request.Request(nckumoodle, moodledata)
        with urllib.request.urlopen(req) as response:
            respond = response.read().decode('utf8')
        decoded = json.loads(respond)

        if decoded.get('token'):
            return data['username']
        else:
            PAMAuthenticator.service = 'login'
            username = yield PAMAuthenticator.authenticate(PAMAuthenticator,handler,data)
            return username

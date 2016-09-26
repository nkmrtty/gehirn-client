# coding: utf-8
import ConfigParser


class GehirnClient(object):
    def __init__(self):
        self.TOKEN_KEY, self.SECRET_KEY = self.read_config()

    def read_config(self):
        config = ConfigParser.ConfigParser()
        if config.read('./config.ini'):
            TOKEN_KEY = config.get('gehirn', 'token_key')
            SECRET_KEY = config.get('gehirn', 'secret_key')
            return TOKEN_KEY, SECRET_KEY
        else:
            self.configuration()
            return self.read_config()

    def configuration(self):
        TOKEN_KEY = raw_input('Input your TOKEN KEY >').decode('utf-8')
        SECRET_KEY = raw_input('Input your SECRET KEY >').decode('utf-8')

        config = ConfigParser.RawConfigParser()
        config.add_section('gehirn')
        config.set('gehirn', 'token_key', TOKEN_KEY)
        config.set('gehirn', 'secret_key', SECRET_KEY)

        with open('config.ini', 'wb') as fp:
            config.write(fp)

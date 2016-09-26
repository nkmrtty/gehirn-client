# coding: utf-8
import base64
import ConfigParser
import json
import sys
import urllib
import urllib2


# Gehirn API endpoints
ENDPOINTS = dict(
    zones="https://api.gis.gehirn.jp/dns/v1/zones"
)


class GehirnClient(object):
    def __init__(self):
        self.TOKEN_KEY, self.SECRET_KEY = self.read_config()
        self.credential = base64.b64encode("{}:{}".format(
            urllib.quote(self.TOKEN_KEY), urllib.quote(self.SECRET_KEY)))

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

    def request_get(self, url):
        req = urllib2.Request(url)
        req.add_header('Authorization', 'Basic {}'.format(self.credential))
        try:
            res = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            print "{}: {}".format(e, url)
            sys.exit(1)
        return json.loads(res.read())

    def get_all_zones(self):
        zones = self.request_get(ENDPOINTS['zones'])
        return zones

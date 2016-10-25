# gehirn-client

An API client for [Gehitn Web Services](https://www.gehirn.jp)

## Requirements

* Python 2.7.x

## Examples
### DDNS

```python
import urllib2
import json
from gehirn import GehirnClient


# get Grobal IP
url = 'http://httpbin.org/ip'
gip = json.loads(urllib2.urlopen(url).read())['origin']

zone_name = 'your.zone'
record_name = 'record.your.zone'
values = {u'records': [{u'address': unicode(gip)}]}

c = GehirnClient()
c.update_record(zone_name, record_name, values)
```
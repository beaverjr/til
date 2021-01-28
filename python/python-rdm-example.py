import datetime
import csv
from redminelib import Redmine
from redminelib.exceptions import ResourceNotFoundError

redmine = Redmine('https://xxxxxxxxxxxxx', key='xxxxxxxxxxxxxx')
#APIキーを入力

issues = redmine.issue.filter(
    project_id='xx',
    cf_x='aa|bb',
    tracker_id='xx'
)
for issue in issues:
   values = [x['value'] for x in issue.custom_fields if x['id'] == xx]
   value = ip_addresses[0] if len(ip_addresses) else ''
   print ('%d:%s:%s' % (issue.id, issue.subject, value))

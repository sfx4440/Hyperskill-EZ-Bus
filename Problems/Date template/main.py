import re


good_string = '03.12.2008'
bad_string = '03-12-2008'
template = re.escape(good_string)

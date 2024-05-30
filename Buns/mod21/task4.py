import re
from sqlalchemy import event
from task1 import Student


@event.listens_for(Student.__table__, 'before_insert')
def check_phone_format(mapper, connection, target):
    phone_pattern = r'\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}'
    if not re.match(phone_pattern, target.phone):
        raise ValueError('Invalid phone number format')

import pytz
from datetime import datetime, timedelta

timezones = [
    'Pacific/Apia',
    'Pacific/Chatham',
    'Pacific/Auckland',
    'Asia/Anadyr',
    'Australia/Lord_Howe',
    'Australia/Yancowinna',
    'Pacific/Port_Moresby',
    'Australia/Darwin',
    'Pacific/Palau',
    'Australia/Eucla',
    'Australia/Perth',
    'Asia/Tomsk',
    'Indian/Cocos',
    'Indian/Chagos',
    'Asia/Kathmandu',
    'Asia/Kolkata',
    'Indian/Maldives',
    'Asia/Kabul',
    'Indian/Mahe',
    'Asia/Tehran',
    'Europe/Riga',
    'Europe/Berlin',
    'Europe/London',
    'Atlantic/Cape_Verde',
    'America/Godthab',
    'America/St_Johns',
    'America/Araguaina',
    'America/Barbados',
    'America/Atikokan',
    'America/Belize',
    'America/Creston',
    'America/Anchorage',
    'America/Adak',
    'Pacific/Marquesas',
    'Pacific/Honolulu',
    'Pacific/Niue',
]

lowest_seconds_remaining = 86401
tz_to_pick = ''

col1 = 'Timezone'
col2 = 'Current time'
col3 = 'Seconds until midnight'
print('+----------------------+----------------------------------+------------------------+')
print(f'| {col1:20} | {col2:32} | {col3:18} |')
print('+----------------------|----------------------------------|------------------------+')

for tz in timezones:
    now = datetime.now(pytz.timezone(tz))
    next_midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    seconds_remaining = (next_midnight - now).seconds

    if seconds_remaining < lowest_seconds_remaining:
        lowest_seconds_remaining = seconds_remaining
        tz_to_pick = tz

    if seconds_remaining < 300:
        addendum = '**** TEST NOW ****'
    elif seconds_remaining < 600:
        addendum = '--- GET READY ---'
    elif seconds_remaining < 1200:
        addendum = '<20m'
    elif seconds_remaining < 1800:
        addendum = '<30m'
    else:
        addendum = ''

    print(f'| {tz:20} | {datetime.now(pytz.timezone(tz))} | {seconds_remaining:22} | {addendum}')

print('+----------------------+----------------------------------+------------------------+')
print('')
print(f'Timezone closest to midnight: {tz_to_pick}')
print('')

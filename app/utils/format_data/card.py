def format_code(raw_data: str):
    raw_data = str(raw_data).rstrip()
    try:
        if (len(raw_data.split('|')) == 2) and ('Баланс:' in raw_data) and ('Карта:' in raw_data):
            link = raw_data.split(':')[-1]
            code = link.split('-')[-1]
        elif len(raw_data.split(':')) >= 2 and len(raw_data.split(':')[1]) == 16:
            code = raw_data.split(':')[1]
        elif len(raw_data) == 16:
            code = raw_data
        elif len(raw_data.split('-')[-1]) == 16:
            code = raw_data.split('-')[-1]
        elif len(raw_data.split()[1]) == 16:
            code = raw_data.split()[1]
        else:
            code = None
    except:
        code = None
    return code

def format_promo_code(raw_data: str):
    raw_data = raw_data.replace('/start', '').strip()
    if len(raw_data) == 36:
        return raw_data
    if len(raw_data.split(':')) == 2 and len(raw_data.split(':')[0]) == 36:
        return raw_data.split(':')[0]

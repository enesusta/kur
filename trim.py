def trim(change):
    change = change.strip()
    change = change.replace('\n', '')
    change = change.replace(' ', '')
    return change
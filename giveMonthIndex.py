

def giveMonthIndex(data):
    month = data.lower()
    if 'jan' in month:
        return '01'
    elif 'feb' in month:
        return '02'
    elif 'mar' in month:
        return '03'
    elif 'apr' in month:
        return '04'
    elif 'may' in month:
        return '05'
    elif 'jun' in month:
        return '06'
    elif 'jul' in month:
        return '07'
    elif 'aug' in month:
        return '08'
    elif 'sep' in month:
        return '09'
    elif 'oct' in month:
        return '10'
    elif 'nov' in month:
        return '11'
    elif 'dec' in month:
        return '12'
    else:
        return ''

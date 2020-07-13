def get_percentage(number, digit=-1):
    if digit == -1:
        va = (round(number * 100))
        return f"{va}%"
    else:
        va = (round(number*100, digit))
        return f"{va}%"

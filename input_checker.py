import datetime

def check_args(args):
    ret = False
    if len(args) == 1:
        print('Insufficient Parameters. You need to supply a date.')
    if len(args) >= 2:
        date = args[1]
        if(is_valid_date(date)):
            ret = True
    return ret

def is_valid_date(date):
    retr = False
    if len(date) != 8:
            print('Date is not in valid format, valid format is "YYYYMMDD".')
    else:
        try:
            days = int(date[6:8])
            months = int(date[4:6])
            year = int(date[0:4])
            asked_day = datetime.date(year,months,days)
            today = datetime.date.today()
            if (today < asked_day):
                print('Date is not valid, please don\'t use future dates.')
            else:
                retr = True
        except:
            print('Date is not valid, valid format is "YYYYMMDD". Please use only numbers.')
    return retr
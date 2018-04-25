import numpy as np
import pandas as pd

FESTIVAL = {
    20180101: '元旦',
    20180215: '除夕',
    20180302: '元霄节',
    20180405: '清明节',
    20180501: '劳动节',
    20180504: '青年节',
    20180601: '儿童节',
    20180618: '端午节',
    20180910: '教师节',
    20180924: '中秋节',
    20181001: '国庆节',
    20181017: '重阳节'
}

HOLIDAY_IN_LAW = {
    20180101: '元旦',
    20180215: '除夕',
    20180216: '春节',
    20180219: '春节',
    20180220: '春节',
    20180221: '春节',
    20180405: '清明节',
    20180406: '清明节',
    20180501: '劳动节',
    20180618: '端午节',
    20180924: '中秋节',
    20181001: '国庆节',
    20181002: '国庆节',
    20181003: '国庆节',
    20181004: '国庆节',
    20181005: '国庆节'
}

WORKDAY = {
    20180211: '春节调休',
    20180224: '春节调休',
    20180408: '清明调休',
    20180428: '五一调休',
    20180929: '国庆调休',
    20180930: '国庆调休'
}


def is_festival(row):
    date = row.date
    date_int = int(date.strftime('%Y%m%d'))
    return True if date_int in FESTIVAL else False


def is_weekend(row):
    return False if 1 <= row.day_of_week <= 5 else True


def is_work_day(row):
    date = row.date
    date_int = int(date.strftime('%Y%m%d'))
    if date_int in WORKDAY:
        return True
    if date_int in HOLIDAY_IN_LAW:
        return False
    return False if row.is_weekend else True


def is_deal_day(row):
    return True if not row.is_weekend and row.is_work_day else False


def main():
    dates = pd.date_range('20180101', '20181231')
    df = pd.DataFrame(dates, columns=['date'])
    df['day'] = df.apply(lambda row: row.date.day, axis=1)
    df['month'] = df.apply(lambda row: row.date.month, axis=1)
    df['quarter'] = df.apply(lambda row: row.date.quarter, axis=1)
    df['year'] = df.apply(lambda row: row.date.year, axis=1)
    df['week'] = df.apply(lambda row: row.date.weekofyear, axis=1)
    # 1-7
    df['day_of_week'] = df.apply(lambda row: row.date.dayofweek + 1, axis=1)
    df['is_month_start'] = df.apply(lambda row: row.date.is_month_start, axis=1)
    df['is_month_end'] = df.apply(lambda row: row.date.is_month_end, axis=1)
    df['days_in_month'] = df.apply(lambda row: row.date.days_in_month, axis=1)
    df['is_quarter_start'] = df.apply(lambda row: row.date.is_quarter_start, axis=1)
    df['is_quarter_end'] = df.apply(lambda row: row.date.is_quarter_end, axis=1)
    df['is_year_start'] = df.apply(lambda row: row.date.is_year_start, axis=1)
    df['is_year_end'] = df.apply(lambda row: row.date.is_year_end, axis=1)
    df['is_leap_year'] = df.apply(lambda row: row.date.is_leap_year, axis=1)
    df['is_weekend'] = df.apply(lambda row: is_weekend(row), axis=1)
    df['is_festival'] = df.apply(is_festival, axis=1)
    df['is_work_day'] = df.apply(is_work_day, axis=1)
    df['is_deal_day'] = df.apply(is_deal_day, axis=1)
    print(df)
    df.to_csv('dates.csv')


if __name__ == '__main__':
    main()

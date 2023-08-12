from enum import Enum
from pytz import timezone
from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from dateutil.relativedelta import relativedelta


class DateValues:

    @staticmethod
    def get_current_date():
        """
        Return current date

        :returns: current date
        :rtype: str
        """
        return datetime.now(timezone('Asia/Seoul')).strftime(DateFormat.yyyyMMdd.value)

    @staticmethod
    def get_before_one_day():
        """
        Return yesterday's date

        :returns: date of yesterday
        :rtype: str
        """
        return (datetime.now(timezone('Asia/Seoul')) - relativedelta(days=1)).strftime(DateFormat.yyyyMMdd.value)

    @staticmethod
    def get_before_one_month(base_day: str = None):
        """
        Return Last month

        :returns: last month (format: yyyyMM)
        :rtype: str
        """
        if base_day:
            month_len = 6
            day_len = 8
            if len(base_day) not in [month_len, day_len]:
                raise ValueError("Length of base_day is not allowed.")
            return (datetime.strptime((base_day[:6] + "01"), DateFormat.yyyyMMdd.value) - relativedelta(
                months=1)).strftime(DateFormat.yyyyMM.value)
        return (datetime.now(timezone('Asia/Seoul')) - relativedelta(months=1)).strftime(DateFormat.yyyyMM.value)


class DateFormat(Enum):
    yyyyMMddHHmmss = "%Y%m%d%H%M%S"
    yyyyMMdd = "%Y%m%d"
    yyyyMM = "%Y%m"
    formattedYyyyMMddHHmmss = "%Y-%m-%d %H:%M:%S"

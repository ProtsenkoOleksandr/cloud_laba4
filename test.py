from json import *
import requests
import sys
from datetime import *


def Obj_Scan_Date(begin_point, limit_point, delta=timedelta(days=1)):
    temporary_var = begin_point
    while temporary_var <= limit_point:
        yield temporary_var
        temporary_var += delta


def main():
    with open(sys.argv[1], "a", encoding="utf-8") as txt:
        for info in Obj_Scan_Date(date(2021, 1, 1), date(2021, 1, 31), delta=timedelta(days=1)):
            my_time = str(info).replace("-", "")
            content = requests.get(
                "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={0}&date={1}&json".format(
                    sys.argv[2], my_time))
            dump(content.json(), txt, sort_keys=False, ensure_ascii=False, separators=(',', ': '), indent=4)

    with open(sys.argv[1], "r", encoding="utf-8") as txt:
        new_content = txt.read().replace("][", ",")

    with open(sys.argv[1], "a", encoding="utf-8") as txt:
        txt.write(new_content)


if __name__ == "__main__":
    main()

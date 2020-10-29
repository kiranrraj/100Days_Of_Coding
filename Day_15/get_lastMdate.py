# Title  : Get last modified date of a file
# Author : Kiran raj R.
# Date   : 29:10:2020

import os
import time


def get_last_mtime(file_url):

    file_details = os.stat(file_url)
    m_date = time.localtime(file_details.st_mtime)
    m_year, m_month, m_day, m_hour, m_min, m_sec = m_date[0:6]
    # print(m_year, m_month, m_day, m_hour, m_min, m_sec)
    print(
        f"Last modified date of '{file_url}' is on {m_day}/{m_month}/{m_year}, time {m_hour}:{m_min}:{m_sec}")


get_last_mtime('cdn.txt')
get_last_mtime('vb_Virtualization_issue.txt')

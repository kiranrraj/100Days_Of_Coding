# Title  : Check for leap year
# Author : Kiran raj R.
# Date   : 29:10:2020

leap_fs = [1584, 1588, 1592, 1596, 1600, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636,
           1640, 1644, 1648, 1652, 1656, 1660, 1664, 1668, 1672, 1676, 1680, 1684, 1688, 1692, 1696, 1704,
           1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 1748, 1752, 1756, 1760, 1764, 1768,
           1772, 1776, 1780, 1784, 1788, 1792, 1796, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836,
           1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904,
           1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968,
           1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

ly_set1 = [1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932,
           1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984,
           1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

mixed_years = [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
               2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2020]


def leap_year(year_in_list):

    for years in year_in_list:
        if years % 400 == 0 or years % 4 == 0 and years % 100 != 0:
            print(f"{years} is a Leap year")
        else:
            print(f"{years} not a Leap year")


leap_year(mixed_years)
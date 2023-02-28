import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%B"))


x = datetime.datetime(2005, 3, 14)
print(x)
print(x.strftime("%A"))

"""
%a	Weekday, short version	Wed	Try it »
%A	Weekday, full version	Wednesday	Try it »
%w	Weekday as a number 0-6, 0 is Sunday	3	Try it »
%d	Day of month 01-31	31	Try it »
%b	Month name, short version	Dec	Try it »
%B	Month name, full version	December	Try it »
%m	Month as a number 01-12	12	Try it »
%y	Year, short version, without century	18	Try it »
%Y	Year, full version	2018	Try it »
%H	Hour 00-23	17	Try it »
%I	Hour 00-12	05	Try it »
%p	AM/PM	PM	Try it »
%M	Minute 00-59	41	Try it »
%S	Second 00-59	08	Try it »
%f	Microsecond 000000-999999	548513	Try it »
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	Try it »
%U	Week number of year, Sunday as the first day of week, 00-53	52	Try it »
%W	Week number of year, Monday as the first day of week, 00-53	52	Try it »
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	Try it »
%C	Century	20	Try it »
%x	Local version of date	12/31/18	Try it »
%X	Local version of time	17:41:00	Try it »
%%	A % character	%	Try it »
%G	ISO 8601 year	2018	Try it »
%u	ISO 8601 weekday (1-7)	1	Try it »
%V	ISO 8601 weeknumber (01-53)	01
"""
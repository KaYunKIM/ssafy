inline = 14000605
calendar = {
    1:1024,
    2:512,
    3:256,
    4:128,
    5:64,
    6:32,
    7:16,
    8:8,
    9:4,
    10:2
}
one_hour = 25+5*15
one_day = one_hour*12

day= inline//one_day
inline%=one_day

hour = inline//one_hour
inline%=one_hour
hour+=9

minute = 0
if inline in [24, 39, 54,69,84,99]:
    minute+=1
if inline >= 25:
    inline-=25
    if inline >= 15:
        minute = inline//15
        inline %= 15
    else:
        minute+=1
minute*=20

one_year= sum(calendar.values())
year= day//one_year+2020
day%=one_year

month = 1
while day - calendar[month] >= 0:
    day-=calendar[month]
    month+=1

print('year',year,'month',month, 'day',day, 'hour', hour, 'minute', minute, 'remain people', inline)
print('{}년 {}월 {}일 {}시 {}분 출발'.format(year,month,day,hour,minute))
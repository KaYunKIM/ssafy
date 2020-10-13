inline = 1200202
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
day = 1
while day*one_day < inline:
    day+=1
day-=1
print('day',day, day*one_day)
inline-=day*one_day
hour = 1
while hour*one_hour < inline:
    hour+=1
hour-=1
print('hour',hour, hour*one_hour, inline)
inline-=hour*one_hour
hour+=9
minute = 0
if inline >= 25:
    inline-=25
    minute+=1
    if inline >= 15:
        while minute*15 < inline:
            inline-=minute*15
            minute+=1
    print('minute',minute-1)
print('minute',minute)
minute*=2
# elif inline <= 1:


one_year= sum(calendar.values())
year= day//one_year+2020
day = day%one_year
month = 1
while day - calendar[month] >= 0:
    day-=calendar[month]
    month+=1
print('year',year,'month',month, 'day',day, 'hour', hour, 'minute', minute, 'remain people', inline)
print('{}년 {}월 {}일 {}시 {}분 출발'.format(year,month,day,hour,minute))


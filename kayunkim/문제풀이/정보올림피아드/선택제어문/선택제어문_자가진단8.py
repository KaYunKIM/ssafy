T = float(input())

if 0<= T <= 4.5:
    if T >= 4.0:
        print('scholarship')
    elif T >= 3.0:
        print('next semester')
    elif T >= 2.0:
        print('seasonal semester')
    else:
        print('retake')

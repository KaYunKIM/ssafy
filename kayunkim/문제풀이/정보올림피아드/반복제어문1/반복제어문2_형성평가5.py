while True:
    B = int(input())
    H = int(input())
    tw = B*H/2
    print('Base = Height = Triangle width = {}'.format(tw))
    inp = input('Continue? ')
    if inp == 'Y' or 'y':
        continue
    else:
        break
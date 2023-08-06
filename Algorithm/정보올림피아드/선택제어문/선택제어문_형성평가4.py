num = int(input())

animals = {1:'dog', 2:'cat', 3:'chick'}

if num in animals.keys():
    print('Number? {}'.format(animals[num]))
else:
    print("Number? I don't know.")
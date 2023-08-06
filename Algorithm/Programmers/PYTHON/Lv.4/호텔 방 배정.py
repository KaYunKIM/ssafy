def solution(k, room_number):
    answer = []
    room = {}
    for i in range(len(room_number)):
        if room_number[i] in room:   #if room.get(room_number[i],0)
            temp = [room_number[i]]
            h = room[room_number[i]]
            while True:
                if h in room:     #if room.get(h,0)
                    temp.append(h)
                    h = room[h]
                else:
                    room[h] = h+1
                    room_number[i] = h
                    break
            for j in temp:
                room[j] = h+1
        else:
            room[room_number[i]] =room_number[i]+1
    return room_number
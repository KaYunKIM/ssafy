def solution(cacheSize, cities):
    answer = 0
    cities = [city.lower() for city in cities]
    temp = []

    if cacheSize != 0:
        for city in cities:
            if city in temp:  # cache hit
                temp.remove(city)
                temp.append(city)
                answer += 1

            else:  # cache miss
                if len(temp) < cacheSize:
                    temp.append(city)

                else:
                    temp.pop(0)
                    temp.append(city)

                answer += 5
    else:
        return len(cities) * 5

    return answer
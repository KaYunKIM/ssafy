def my_sqrt():
    x, y = 1, n
    result = 1

    while abs(result**2 -n) > 0.00000001:
        result = (x+y) /2
        if result **2 < n:
            x = result
        else:
            y = result
    return result

print('my_sqrt:\t',my_sqrt(2))

import math
print('math.sqrt:\t',math.sqrt(2))
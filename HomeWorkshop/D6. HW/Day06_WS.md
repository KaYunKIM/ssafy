# Day06_WS

### 1. 

``` 
class Circle:
    pi =3.14
    x = 0
    y = 0
    r = 0

    def __init__(self,r,x,y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return(self.x, self.y)
```

```
cir = Circle(3,2,4)
```

```
cir.area() 		#28.259999999999998
```

```
cir.circumference() 	#18.84
```


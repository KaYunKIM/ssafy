# Day07_WS

### 1. 

``` 
class Animal:
    def __init__(self,name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')
```

```
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def walk(self):
        print(f'{self.name}! 달린다!')
        
    def run(self):
        print(f'{self.name}! 달린다!')
```

```
dog = Dog('멍멍이')
```

```
dog.walk()		#멍멍이! 달린다!
```

```
dog.run()       #멍멍이! 달린다!
```



```
class Bird(Animal):
    def __init__(self,name):
        super().__init__(name)
    def fly(self):
        print(f'{self.name}! 푸드덕!')
```

```
bird = Bird('구구')
```

```
bird.walk()		#구구! 걷는다!
```

```
bird.eat()		#구구! 먹는다!
```

```
bird.fly()		#구구! 푸드덕!
```
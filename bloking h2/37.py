class MyNumbers:
    def _iter_(self):
        self.a = 1
        return self
    
    def _next_(self):
        x = self.a
        self.a += 1
        return x
    
mycalss = MyNumbers()
myiter = iter(mycalss)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
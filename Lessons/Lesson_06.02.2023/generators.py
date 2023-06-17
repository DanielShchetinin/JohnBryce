def my_gen():
    n = 1
    print("This is printed first")
    yield n
    print("After the first one!")
    
    n += 1
    print("This is printed second time")
    yield n
    
    n += 1
    print("This is a last time!")
    yield n
    
    

if __name__ == '__main__':
    a = my_gen()
    
    val1 = next(a)
    print(val1)
    
    val1 = next(a)
    print(val1)
    
    val1 = next(a)
    print(val1)
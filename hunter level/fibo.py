def fib2(n):
    
     result = []
     a, b = 0, 1
     while b < n:
         result.append(b)   
         a, b = b, a+b
     return result

if __name__ == '__main__':
    output=fib2(100)
    print output

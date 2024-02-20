# try, except, else e finally

try:
   print(1) 
#    8/0
    
except ZeroDivisionError:
    print('Dividiu por 0')
else:
    print('Não deu erro')
finally:
       print(2)

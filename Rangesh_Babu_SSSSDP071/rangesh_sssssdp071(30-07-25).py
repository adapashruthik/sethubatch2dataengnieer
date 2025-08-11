Value=int(input("How many lines? : "))
 for i in range(1, Value + 1):
 print(" " * (Value- i), end="")
 print("*" * (2 * i- 1))
 #Howmanylines? : 7
 '''
 *
 ***
 *****
 *******
 *********
 *********** '''
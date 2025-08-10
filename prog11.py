try:
    a=input("Enter any string with alternate character and digit: ")
    print("Result: ",end="")
    for i in range(0,len(a),2):
        print(a[i]*int(a[i+1]),end="")
except ValueError:
    print("String should have alternate character and digit")
print("If you want to say 'Hello' enter the 1 button")
print("If you want to exit enter the 2 button")

button = int(input("Enter: "))

a =1
while a == 1:
    if button == 1:
        print("Hello")
        break
    else:
        print("Goodbye")
        break


str = input('Enter the Value: ')
str1 = str[::-1]
if str1 == str:
    print(f"Yes \nThis valuse ({str}) is palindrom ")
else: print(f"No \nThis valuse ({str}) is not palindrom")
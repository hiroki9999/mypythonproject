count ＝ 0
while True:
    str = input("enter a string: ")
    for letter in str:
      if letter == 'a':
          count +=1
          break

    print(count , "strings with letter 'a'")

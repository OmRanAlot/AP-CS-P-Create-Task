import random
import time

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '~', '?', '.']
include_characters = []
exclude_characters = []
running = True
simple = False
rerun = False


def generatePwd(lengthOfPwd, type):
  password = ""
  if (type == "s"):
    for i in range(0, lengthOfPwd):
      temp = random.randint(0, 1)
      if temp == 1:
        password += random.choice(letters)
      else:
        password += random.choice(numbers)
    return password

  elif (type == "a"):
    password = ""
    #create password with only included letters
    
    for i in range(len(include_characters)):
      password += include_characters[i]

    for i in range(lengthOfPwd - len(password)):
      temp = random.randint(0, 4)
      location = random.randint(0, lengthOfPwd)
      temp1 = password[:location]
      temp2 = password[location:]
      if temp == 0 or temp == 1:
        tempAgain = random.randint(0, 1)
        letter = random.choice(letters) if tempAgain == 0 else random.choice(
            letters).upper()

        while (letter in exclude_characters):
          letter = random.choice(letters) if tempAgain == 0 else random.choice(
              letters).upper()
        temp1 += letter

      elif temp == 2:
        num = random.choice(numbers)
        while (num in exclude_characters):
          num = random.choice(numbers)
        temp1 += num

      else:
        sym = random.choice(symbols)
        while (sym in exclude_characters):
          sym = random.choice(symbols)
        temp1 += sym

      password = temp1 + temp2
    return password


print("Welcome to my password generator!")
simpleOrAdv = input(
    str("Type either \"s\" or \"a\" for simple or advanced passwords based on your preferences."
        ))

#choose whether the user chooses simple or advanced passwords
while (simpleOrAdv != "s" or simpleOrAdv != "a"):
  if (simpleOrAdv == "s"):
    print("You have chosen simple passwords.")
    simple = True
    break

  elif (simpleOrAdv == "a"):
    simple = False
    print("You have chosen advanced passwords.")
    break

  else:
    print("Invalid input. Please try again.")
    simpleOrAdv = input(
        str("Type either s or a for simple or advanced passwords based on your preferences."
            ))

print("")

while (running):
  #simple passwords
  if (simple):
    print("Your password will contain only letters and numbers.")
    time.sleep(1)
    passwordLength = int(input("How long would you like your password to be?"))
    time.sleep(3)
    print("Your password is: ")
    print(generatePwd(passwordLength, "s"))
    time.sleep(1.5)
    more_adv = input(
        '\n Would you like to create a more advanced password?(y/n)')
    if more_adv == 'y':
      simple = False
      print("Setting mode to advanced passwords.")
    else:
      print("")
      print("Enjoy your password!")
      break

  #advanced passwords
  else:
    time.sleep(1)
    print(
        "Your password will contain lowercase and uppercase letters, numbers, and symbols."
    )
    time.sleep(1)
    print(
        "You can also customize which characters you want to include or exlcude in your password."
    )
    time.sleep(1)

    #Get characters to include in password
    include = str(
        input(
            "Type 1 character you would want to include in your password (if none, type \"quit\" to quit)"
        ))
    while (include != "quit"):
      include_characters.append(include)
      include = str(
          input(
              "Type 1 character you would want to include in your password (type \"quit\" to quit)"
          ))

    print("")
    #get characters to exlcude in password
    exclude = str(
        input(
            "Type 1 character you would want to exclude in your password (if none, type \"quit\" to quit)"
        ))

    while (exclude != "quit"):
      for i in include_characters:
        if (exclude == i):
          print(
              "You cannot exclude a character that is already included. Please try again."
          )
          exclude = str(
              input(
                  "Type 1 character you would want to exclude in your password (type \"quit\" to quit)"
              ))
      exclude_characters.append(exclude)
      exclude = str(
          input(
              "Type 1 character you would want to exclude in your password (type \"quit\" to quit)"
          ))

    #get length of password
    passwordLength = int(input("How long would you like your password to be?"))
    if (passwordLength < len(include_characters)):
      print(
          "Your password will only contain the characters you included, and some might not be in your password."
      )

    time.sleep(3)
    pwd = generatePwd(passwordLength, "a")
    print("Your password is: ")
    print(str(pwd) + "\n")
    time.sleep(0.5)
    print("Enjoy your password!")
    break

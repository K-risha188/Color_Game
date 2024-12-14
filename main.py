import random
colors = ["blue","pink","purple","orange","black","white","red","yellow","green"]


def gameplay():
   game_win = 0
   game_lost= 0



   print("\nWelcome to the Color Game!\n")
   name = input("Please enter your name : ")

   print("\nChoices : "
        "\n1.Start Game"
        "\n2.Exit")
   choice = int(input("\nEnter your choice: "))
   u_color = ''


   while True:
    m_color = random.choice(colors)
    if choice == 1:
     attempts = 5
     wins = 0
     while attempts >= 1:
      u_color=input("\nenter your color : ").lower()
      if u_color not in colors:
        print("\nInvalid color!")
        attempts-=1
        print("\nNumber of attempts left = ", attempts)
        continue
      elif u_color == m_color:
        print("YOU WON :)\n")
        wins += 1
        break
      else:
        attempts -= 1
        print("Wrong guess :/ ")
        print("Number of attempts left = ",attempts)
        continue
     print("Color chosen by machine is : " + m_color)
     if wins > 0:
      game_win+=1
     else:
       game_lost+=1

     print("\n1> See score board and exit"
        "\n2> Play again"
        "\n3> Exit")
     new_choice = int(input("Enter your choice : "))

     if new_choice == 1:
      print("\n" + "Name : Krisha"
                   "\nGames won = ", game_win,
            "\nGames lost = ", game_lost)
      exit(0)
     elif new_choice == 2:
      continue
     else:
      print("\nThank you for playing " + name)
      exit(0)

    else:
     print("Thank you for participating " + name + " :)")
     exit(0)

if __name__ == "__main__":
    gameplay()


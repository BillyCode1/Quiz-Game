print("Hello there!")

playing = input("Do you want to play a game? ")
points = 0

if playing != "yes":
  quit()

print("Okay! Let's play a quiz game :)")

answer = input("Going towards the sun, what is the next planet after Earth: ")
if answer == "venus":
  print("Correct! +1 Points")
  print(" ")
  points += 1
else:
  print("Incorrect!")

answer = input("Going away from the sun, what is the next planet after Earth: ")
if answer == "mars":
  print("Correct! +1 Points")
  print(" ")
  points += 1
else:
  print("Incorrect!")

answer = input("What is the name of the force which keeps the planets in orbit around the sun?: ")
if answer == "gravity":
  print("Correct! +1 Points")
  print(" ")
  points += 1
else:
  print("Incorrect!")

answer = input("Which planet is closest to the sun?: ")
if answer == "mercury":
  print("Correct! +1 Points")
  print(" ")
  points += 1
else:
  print("Incorrect!")

answer = input("Which planet is named after the Roman god of war?: ")
if answer == "mars":
  print("Correct! +1 Points")
  print(" ")
  points += 1
else:
  print("Incorrect!")

answer = input("Which is the largest moon of Saturn?: ")
if answer == "titan":
  print("Correct! +1 Points")
  print(" ")
  points += 1
else:
  print("Incorrect!")

if points < 6:
  print(f"You scored {points} points")

elif points == 6:
  print(f"Congratulations! you got {points} full points!")

def main(type):
  x = 0 
  print(type)
  if type=="wl":
  #a while loop 
    while (x <5):
      print(x)
      x = x + 1
  elif type=="fl":
  #a for loop 
    for x in range(5,10):
      print(x)
  elif type=="cl":
  #a for loop over a collection 
    days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    for d in days:
      print(d) 

  elif type=="en":
  # enumerate() function to get index 
    directions = ["East", "West", "North", "South", "SouthWest", "NorthEast", "NorthWest"]
    for i, d in enumerate(directions):
      print (i,d) 
  
  else:
    print("Invalid loop type specified")  

if __name__ == "__main__":
  main('wl')

def main():
  print("Keep it logically awesome.")
  print("This is a random quote.")
  print("Hope this solves the problem.")  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

if __name__== "__main__":
  main()

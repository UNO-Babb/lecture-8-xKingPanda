def main():
  myFile = open("mlb_output.csv", 'r')
  
#print for every line
  for line in myFile:
    print(line.strip()) # Use strip() to remove any trailing newline characters

  myFile.close()


if __name__ == '__main__':
  main()

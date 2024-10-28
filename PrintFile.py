def main():
  myFile = open("qbdata.txt", 'r')

  for line in myFile:
    info = line.split(",")

    #print (info)
    if info[1] == '"NE"':
      print(line)
    

  myFile.close()


if __name__ == '__main__':
  main()

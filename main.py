def main():
  pitching = open("MLB_Pitching.csv", 'r')
  team_data = []

  #get the import info out of pitching and store into team_data
  for team in pitching:
    data = team.split(",")
    team_data.append([data[0], "",  data[3], data[4], data[5], data[7]])
    #team name, blank, RA/G, W, L, ERA
  print(team_data)

  pitching.close()

  hitting = open("MLB_Hitting.csv", 'r')
  lineNum = 0
  for team in hitting:
    data = team.split(",")
    team_data[lineNum][1] = data[3]
    lineNum +=

  #process all the data in hitting and add to the correct portion of the team_data

  hitting.close()


  outFile = open("mlb_output.csv", 'w')

  #process each line of the team_data and save to the output file.
  output = ""
  for team in team_data:
    team = str(team)
    team = team.replace("[","")
    team = team.replace("]","")
    team = team.replace("'","")
    output = output + team + "\n"
    
  outFile.write(output)

  outFile.close()

if __name__ == '__main__':
  main()

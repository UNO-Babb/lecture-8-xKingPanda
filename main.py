def main():
  pitching = open("MLB_Pitching.csv", 'r')
  team_data = []
  pitching.readline()#reads first line, skips header

  #get the import info out of pitching and store into team_data
  for team in pitching:
    data = team.split(",")
    if data[0]:  # Ensure there is a team name
        team_data.append([data[0], "",  data[3], data[4], data[5], data[7]])
        #team name, blank, RA/G, W, L, ERA

  pitching.close()

  hitting = open("MLB_Hitting.csv", 'r')
  hitting.readline()#skips the first header and goes straight to first line
  lineNum = 0
  for team in hitting:
    data = team.strip().split(",")
    if lineNum < len(team_data) and data[0]:  # Check for valid data and team name
        team_data[lineNum][1] = data[3]
    lineNum += 1

  #process all the data in hitting and add to the correct portion of the team_data

  hitting.close()


  outFile = open("mlb_output.csv", 'w')

  #process each line of the team_data and save to the output file.
  output = ""
  
  #this could be used to make it cleaner
  # team_str = ",".join(team)  # Join the list items into a comma-separated string
  #output += team_str + "\n"

  for team in team_data:
    team = str(team)
    team = team.replace("[","")
    team = team.replace("]","")
    team = team.replace("'","")
    output += team + "\n"  # Add a newline at the end of each line
    
  outFile.write(output)
  outFile.close()

if __name__ == '__main__':
  main()

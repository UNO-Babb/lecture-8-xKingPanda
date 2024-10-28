

def print_mlb_output(team_data):
    # Open the combined MLB output file for reading
    outFile = open("mlb_output.csv", 'w')

    # Print each line in the file
    outFile.write("Team Name,R/G,RA/G,W,L,ERA\n")

    for team in team_data:
        # Convert the list to a string and format it manually
        team_str = str(team)
        team_str = team_str.replace("[", "")
        team_str = team_str.replace("]", "")
        team_str = team_str.replace("'", "")
        outFile.write(team_str + "\n")  # Write each team data line to the file

    outFile.close()

import csv
import random
num = random.randint(0,556)

# Rk,Player,Age,Team,Pos,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS,Awards

players = []

# Open the CSV file
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    # Convert the CSV to a list of rows
    data = list(csv_reader)

    # Print the data
    for row in data:
        players.append(row)

teams = {
    "ATL": "Atlanta Hawks", 
    "BOS": "Boston Celtics",
    "CHO": "Charlotte Hornets",
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Cavaliers",
    "DAL": "Dallas Mavericks",
    "DEN": "Denver Nuggets",
    "DET": "Detroit Pistons",
    "GSW": "Golden State Warriors",
    "HOU": "Houston Rockets",
    "IND": "Indiana Pacers",
    "LAC": "Los Angeles Clippers",
    "LAL": "Los Angeles Lakers",
    "MEM": "Memphis Grizzlies",
    "MIA": "Miami Heat",
    "MIL": "Milwaukee Bucks",
    "MIN": "Minnesota Timberwolves",
    "NOP": "New Orleans Pelicans",
    "NYK": "New York Knicks",
    "BRK": "Brooklyn Nets",
    "OKC": "Oklahoma City Thunder",
    "ORL": "Orlando Magic",
    "PHI": "Philadelphia 76ers",
    "PHO": "Phoenix Suns",
    "POR": "Portland Trail Blazers",
    "SAC": "Sacramento Kings",
    "TOR": "Toronto Raptors",
    "UTH": "Utah Jazz",
    "WAS": "Washington Wizards",
    "2TM": "Two Teams",
    "SAS": "San antonio Spurs",
    "3TM": "Three Teams"


}


player = players[num]
player_name = player[1]
player_team = teams[player[3]] if player[3] in teams else player[3]
player_ppg = player[29]
player_age = player[2]
player_position = player[4]
Player_assists = player[24]
Player_blocks = player[26]
Player_steals = player[25]



def main():
    print("Hint 1: They are on this team: ", player_team)
    guess = input("Enter a guess: ")
    
    if guess == player_name:
        return print("Correct!")
    else:
        print("Incorrect!")
    
    
    print("Hint 2: Their points per game is: ", player_ppg)
    guess = input("Enter a guess: ")
    
    if guess == player_name:
        return print("Correct!")
    else:
        print("Incorrect!")
    
        print("Hint 3: There age is: ", player_age)
        guess = input("Enter a guess: ")
    
        if guess == player_name:
            return print("Correct!")
        else:
            print("Incorrect!")

    print("Hint 4: There position is: ", player_position)
    guess = input("Enter a guess: ")

    if guess == player_name:
        return print("Correct!")
    else:
        print("Incorrect!")
    
    
    


    print("Hint 5: There assists per game is: ", Player_assists)
    guess = input("Enter a guess: ")

    if guess == player_name:
        return print("Correct!")
    else:
        print("Incorrect!")





    print("Hint 6: There blocks per game is: ", Player_blocks)
    guess = input("Enter a guess: ")

    if guess == player_name:
        return print("Correct!")
    else:
        print("Incorrect!")




    print("Hint 7: There steals per game is: ", Player_steals)
    guess = input("Enter a guess: ")

    if guess == player_name:
        return print("Correct!")
    else:
        print("Incorrect!")



    print(player_name)

main()
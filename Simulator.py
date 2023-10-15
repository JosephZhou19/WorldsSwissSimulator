import random
class Team:
    def __init__(self, name):
        self.name = name
        self.opponents = []
        self.wins = 0
        self.losses = 0
class Standing:
    def __init__(self, name, wins, losses):
        self.name = name
        self.teams = []
        self.wins = wins
        self.losses = losses
T1 =   Team("T1    ")
TL =   Team("TL    ")
C9 =   Team("Cloud9")
MAD =  Team("MAD   ")
GenG = Team("Gen.g ")
GAM =  Team("Gam   ")
JDG =  Team("JDG   ")
BDS =  Team("BDS   ")
G2 =   Team("G2    ")
DK =   Team("DK    ")
NRG =  Team("NRG   ")
WBG =  Team("WBG   ")
FN =   Team("Fnatic")
LNG =  Team("LNG   ")
BLG =  Team("BLG   ")
KT =   Team("KT    ")
                   
matchups = [[T1, TL], [C9, MAD], [GenG, GAM], [JDG, BDS], [G2, DK], [NRG, WBG], [FN, LNG], [BLG, KT]]
zerozero = Standing("0-0", 0, 0)
zerozero.teams = [T1, TL, C9, MAD, GenG, GAM, JDG, BDS, G2, DK, NRG, WBG, FN, LNG, BLG, KT]
onezero = Standing("1-0", 1, 0)
zeroone = Standing("0-1", 0, 1)
twozero = Standing("2-0", 2, 0)
oneone = Standing("1-1", 1, 1)
zerotwo = Standing("0-2", 0, 2)
twoone = Standing("2-1", 2, 1)
onetwo = Standing("1-2", 1, 2)
twotwo = Standing("2-2", 2, 2)
qualified = Standing("Qualified", 3, 100)
matchup = matchups.pop(0)
day = 0
standings = [zerozero, onezero, zeroone, twozero, oneone, zerotwo, twoone, onetwo, twotwo, qualified]
print("Type h for help\n Type s for Standings\n Type r for record of all teams \n Type m for next match \n Type d for all matches for the day \n Type q to quit")]
print("Matchup: " + matchup[0].name + " vs." + matchup[1].name)
print("Type 1 for team 1, 2 for team2")
while(True):
    response = input()
    if response == "h":
        print("Type h for help\n Type s for Standings\n Type r for record of all teams \n Type m for next match \n Type d for all matches for the day \n Type q to quit")
    elif response == "s":
        toPrint = ""
        for standing in standings:
            toPrint += standing.name + "         "
        print(toPrint)
        for i in range(0, len(zerozero.teams)):
            toPrint = ""
            for j in range(0, len(standings)):
                if i < len(standings[j].teams):
                    toPrint += standings[j].teams[i].name + "      "
                else:
                    toPrint += "      " + "      "
            print(toPrint)
    elif response == "r":
        for i in range(0, len(zerozero.teams)):
            team = zerozero.teams[i]
            toPrint = team.name + " " + str(team.wins) + ":" + str(team.losses) + " "
            for opp in team.opponents:
                toPrint += opp + " "
            print(toPrint)
    elif response == "m":
        print("Matchup: " + matchup[0].name + " vs." + matchup[1].name)
        print("Type 1 for team 1, 2 for team2")
    elif response == "d":
        for match in matchups:
            print(match[0].name + " vs." + match[1].name)
    elif response == "1" or response == "2":
        if matchup == []:
            print("No matches left")
        else:
            winner = matchup.pop(int(response) - 1)
            loser = matchup.pop()
            print(winner.name + " beats " + loser.name)
            winner.wins += 1
            loser.losses += 1
            winner.opponents.append(loser.name + "-W")
            loser.opponents.append(winner.name + "-L")
            for standing in standings:
                if standing.wins == 3 and standing.wins == winner.wins:
                    standing.teams.append(winner)
                if standing.wins == winner.wins and standing.losses == winner.losses:
                    standing.teams.append(winner)
                if standing.wins == loser.wins and standing.losses == loser.losses:
                    standing.teams.append(loser)
            if len(matchups) == 0:
                day += 1
                if day == 5:
                    f = open("stats.txt", "a+")
                    toPrint = ""
                    for standing in standings:
                        toPrint += standing.name + "         "
                    f.write(toPrint + "\n")
                    for i in range(0, len(zerozero.teams)):
                        toPrint = ""
                        for j in range(0, len(standings)):
                            if i < len(standings[j].teams):
                                toPrint += standings[j].teams[i].name + "      "
                            else:
                                toPrint += "      " + "      "
                        f.write(toPrint + "\n")
                    f.close()
                    print("Thats all the matches. Data saved to stats.txt")
                else:
                    for standing in standings:
                        if standing.wins + standing.losses == day:
                            teamsPlaying = []
                            for team in standing.teams:
                                teamsPlaying.append(team)
                            while len(teamsPlaying) > 0:
                                newMatch = [teamsPlaying.pop()]
                                newMatch.append(teamsPlaying.pop(random.randint(0, len(teamsPlaying) - 1)))
                                matchups.append(newMatch)
            if matchup == [] and len(matchups) != 0:
                matchup = matchups.pop(0)
                print("Matchup: " + matchup[0].name + " vs." + matchup[1].name)
                print("Type 1 for team 1, 2 for team2")
    elif response == "q":
        break
    else:
        print("That wasn't a proper response")
    





from collections import OrderedDict


filename = "football-league-results.txt"
def leagueResult():
    with open(filename) as league_result:
    #    league_result.next()
        teamGoalPerforrmance = []
        clubNamesList = []
        goalDiff = []
        for team in league_result:
            team = team.split()
            clubNames = []
            clubData = []

            for data in team:
                try:
                    data = int(data)
                    clubData.append(data)

                except ValueError:
                    stringData = str(data)
                    if stringData != "-":
                        clubNames.append(stringData)
                    pass

            if len(clubData) > 0:
                goalFor = int(clubData[4])
                goalAgainst = int(clubData[5])
                del clubNames[:1]
                clubNames = ' '.join(clubNames)
                clubNamesList.append(clubNames)
                goalDiff.append(goalFor - goalAgainst)

        teamGoalPerforrmance = dict(zip(clubNamesList,goalDiff))
        sortedTeams = []
        for team, diff in teamGoalPerforrmance.items():
            print "%s: %s" % (team, diff)
            sortedTeams = OrderedDict(diff.items() key=lambda x: x[1])
                #print clubNames, goalFor, goalAgainst
        #print teamGoalPerforrmance
leagueResult()

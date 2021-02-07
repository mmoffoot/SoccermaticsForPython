#Load in Statsbomb competition and match data
#This is a library for loading json files.
import json

#Load the competition file
#Got this by searching 'how do I open json in Python'
with open('Statsbomb/data/competitions.json') as f:
    competitions = json.load(f)

#Self select manually a competition ID from the data, such as 72 or 43
competition_id=43

#Extract the Season id so the related file can be found

for competition in competitions:
    if (competition_id == competition['competition_id']):
#        print("The competition ID is " + str(competition['competition_id']))
        season_id=competition['season_id']

#Load the list of matches for this competition
with open('Statsbomb/data/matches/'+str(competition_id)+'/'+str(season_id)+'.json') as f:
    matches = json.load(f)

#Look inside matches (Only run these if in an IDE like Anaconda)
#matches[0]
#matches[0]['home_team']
#matches[0]['home_team']['home_team_name']
#matches[0]['away_team']['away_team_name']

#Print all match results
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    home_score=match['home_score']
    away_score=match['away_score']
    describe_text = 'The match between ' + home_team_name + ' and ' + away_team_name
    result_text = ' finished ' + str(home_score) +  ' : ' + str(away_score)
    print(describe_text + result_text)

#Now lets find a match we are interested in
home_team_required ="Sweden"
away_team_required ="England"
team_required ="Sweden"

#Find ID for the match
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==home_team_required) and (away_team_name==away_team_required):
        match_id_required = match['match_id']
        print(home_team_required + ' vs ' + away_team_required + ' has id:' + str(match_id_required))
    if (home_team_name==team_required) or (away_team_name==team_required):
        home_score=match['home_score']
        away_score=match['away_score']
        describe_text = 'The Sweden match between ' + home_team_name + ' and ' + away_team_name
        result_text = ' finished ' + str(home_score) +  ' : ' + str(away_score)
        print(describe_text + result_text)

#Exercise:
#1, Edit the code above to print out the result list for the Mens World cup
#2, Edit the code above to find the ID for England vs. Sweden
#3, Write new code to write out a list of just Sweden's results in the tournament.

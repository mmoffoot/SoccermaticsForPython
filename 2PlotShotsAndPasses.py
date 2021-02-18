#Make a shot map and a pass map using Statsbomb data
#Set match id in match_id_required.

#Function to draw the pitch
import matplotlib.pyplot as plt
import numpy as np
from copy import copy

#Size of the pitch in yards (!!!)
pitchLengthX=120
pitchWidthY=80

#ID for England vs Sweden Womens World Cup
match_id_required = 69301
home_team_required ="England Women's"
away_team_required ="Sweden Women's"

# Load in the data
# I took this from https://znstrider.github.io/2018-11-11-Getting-Started-with-StatsBomb-Data/
file_name=str(match_id_required)+'.json'

#Load in all match events
import json
with open('Statsbomb/data/events/'+file_name) as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)

#get the nested structure into a dataframe
#store the dataframe in a dictionary with the match id as key (remove '.json' from string)
from pandas import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

#A dataframe of shots
shots = df.loc[df['type_name'] == 'Shot'].set_index('id')

#Draw the pitch
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','white')

# Have this thing about pitches being green.
fig.set_facecolor('green')
ax.patch.set_facecolor('green')

#Plot the shots
for i,shot in shots.iterrows():
    x=shot['location'][0]
    y=shot['location'][1]

    goal=shot['shot_outcome_name']=='Goal'
    team_name=shot['team_name']

    circleSize=2
    circleSize=np.sqrt(shot['shot_statsbomb_xg']*15)

    if (team_name==home_team_required):
        if goal:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="white")
            plt.text((x+1),pitchWidthY-y+1,shot['player_name'])
        else:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="white")
            shotCircle.set_alpha(.2)
    elif (team_name==away_team_required):
        if goal:
            shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="yellow")
            plt.text((pitchLengthX-x+1),y+1,shot['player_name'])
        else:
            shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="yellow")
            shotCircle.set_alpha(.2)
    ax.add_patch(shotCircle)


plt.text(5,83,away_team_required + ' shots')
plt.text(80,83,home_team_required + ' shots')
plt.text(80,-3,'Data provided by StatsBomb', fontsize=6)

fig.set_size_inches(10, 7)
fig.savefig('Output/shots.pdf', dpi=100)
fig.savefig('Output/shots.png', dpi=300)
plt.show()

#Exercise:
#1, Create a dataframe of passes which contains all the passes in the match

#A dataframe of passes
passes = df.loc[df['type_name'] == 'Pass'].set_index('id')

# Plot the starting point of the pass
(anotherFig,by) = createPitch(pitchLengthX,pitchWidthY,'yards','white')

anotherFig.set_facecolor('green')
by.patch.set_facecolor('green')

for i,tpass in passes.iterrows():
    x=tpass['location'][0]
    y=tpass['location'][1]

    team_name=tpass['team_name']

    circleSize=1

    if (team_name==home_team_required):
            passCircle=plt.Circle((pitchLengthX-x,pitchWidthY-y),circleSize,color="white")
            passCircle.set_alpha(.7)
    elif (team_name==away_team_required):
            passCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="yellow")
            passCircle.set_alpha(.7)
    by.add_patch(passCircle)


plt.text(5,83,away_team_required + ' originating pass')
plt.text(80,83,home_team_required + ' originating pass')
plt.text(80,-3,'Data provided by StatsBomb', fontsize=6)

anotherFig.set_size_inches(10, 7)
anotherFig.savefig('Output/passes.pdf', dpi=100)
anotherFig.savefig('Output/passes.png', dpi=300)
plt.show()


#2, Plot the start point of every Sweden pass. Attacking left to right.
(SwePasses,cz) = createPitch(pitchLengthX,pitchWidthY,'yards','white')

SwePasses.set_facecolor('green')
cz.patch.set_facecolor('green')

for i,tswepass in passes.iterrows():
    x=tswepass['location'][0]
    y=tswepass['location'][1]

    team_name=tswepass['team_name']

    circleSize=1

    if (team_name==away_team_required):
            SwepassCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="yellow")
            SwepassCircle.set_alpha(.7)
            #if (tswepass['player_name'] == 'Rut Hedvig Lindahl'):
            #    plt.text((x+1),pitchWidthY-y+1,tswepass['player_name'])
            cz.add_patch(SwepassCircle)


plt.text(5,83,away_team_required + ' originating passes')
plt.text(80,-3,'Data provided by StatsBomb', fontsize=6)

SwePasses.set_size_inches(10, 7)
SwePasses.savefig('Output/SWEpasses.pdf', dpi=100)
SwePasses.savefig('Output/SWEpasses.png', dpi=300)
plt.show()


#3, Plot only passes made by Caroline Seger (she is Sara Caroline Seger in the database)
(SwePassPlayer,dw) = createPitch(pitchLengthX,pitchWidthY,'yards','white')

SwePassPlayer.set_facecolor('green')
dw.patch.set_facecolor('green')

for i,tswepassplayer in passes.iterrows():
    x=tswepassplayer['location'][0]
    y=tswepassplayer['location'][1]

    team_name=tswepassplayer['team_name']

    circleSize=1

    if (team_name==away_team_required):
        if (tswepassplayer['player_name'] == 'Sara Caroline Seger'):
            playerpassing = tswepassplayer['player_name']
            SwePassPlayerCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="yellow")
            SwePassPlayerCircle.set_alpha(.7)
            dw.add_patch(SwePassPlayerCircle)


plt.text(5,83,away_team_required + ' ' + playerpassing + ' originating passes')
plt.text(80,-3,'Data provided by StatsBomb', fontsize=6)

SwePassPlayer.set_size_inches(10, 7)
SwePassPlayer.savefig('Output/SWEpassesSCS.pdf', dpi=100)
SwePassPlayer.savefig('Output/SWEpassesSCS.png', dpi=300)
plt.show()



#4, Plot arrows to show where the passes went
(SwePassPlayerDir,eu) = createPitch(pitchLengthX,pitchWidthY,'yards','white')

SwePassPlayerDir.set_facecolor('green')
eu.patch.set_facecolor('green')

for i,tswepassplayerdir in passes.iterrows():
    #Just checking the Keys of the list
    #print (', '.join(map(str, tswepassplayerdir.items())))

    #Originally had the pass locations stored here.
    x_start=tswepassplayerdir['location'][0]
    y_start=tswepassplayerdir['location'][1]
    x_end=tswepassplayerdir['pass_end_location'][0]
    y_end=tswepassplayerdir['pass_end_location'][1]

    team_name=tswepassplayerdir['team_name']

    circleSize=1

    playerpassingdir = tswepassplayerdir['player_name']

    if (team_name==away_team_required):
        if (playerpassingdir == 'Sara Caroline Seger'):
            playernowpassing=playerpassingdir

            SwePassPlayerDirCircle=plt.Circle((x_start,pitchWidthY-y_start),circleSize,color="yellow")
            SwePassPlayerDirCircle.set_alpha(.7)
            eu.add_patch(SwePassPlayerDirCircle)

            #David's code
            #dx=x_end-x_start
            #dy=y_end-y_start
            #passLineDirection=plt.Arrow(x_start,pitchWidthY-y_start,dx,dy,width=1.5,color="yellow")
            #eu.add_patch(passLineDirection)

            #My version 1
            #x_values=[x_start, x_end]
            #y_values=[pitchWidthY-y_start, pitchWidthY-y_end]
            #passLineDirection=plt.plot(x_values, y_values)
            #eu.annotate('', xy=(x_start,pitchWidthY-y_start), xytext=(x_end, pitchWidthY-y_end),
            #    arrowprops={'arrowstyle': '<-'}, va='center')

            #My version 2
            dx=x_end-x_start
            dy=(pitchWidthY-y_end)-(pitchWidthY-y_start)
            passLineDirection=plt.Arrow(x_start,pitchWidthY-y_start,dx,dy,width=1.5,color="yellow")
            eu.add_patch(passLineDirection)



plt.text(5,83,away_team_required + ' ' + playernowpassing + ' originating passes')
plt.text(80,-3,'Data provided by StatsBomb', fontsize=6)

SwePassPlayerDir.set_size_inches(10, 7)
SwePassPlayerDir.savefig('Output/SWEpassesdirectionSCS.pdf', dpi=100)
SwePassPlayerDir.savefig('Output/SWEpassesdirectionSCS.png', dpi=300)
plt.show()


#5, Plot arrows of a player in a specific minute to show where the passes went
# and correlate to Youtube footage of the match

(SwePassPlayerDirCor,ft) = createPitch(pitchLengthX,pitchWidthY,'yards','white')

SwePassPlayerDirCor.set_facecolor('green')
ft.patch.set_facecolor('green')

for i,tswepassplayerdircor in passes.iterrows():
    #Just checking the Keys of the list
    #print (', '.join(map(str, tswepassplayerdir.items())))

    #Originally had the pass locations stored here.
    x_start=tswepassplayerdircor['location'][0]
    y_start=tswepassplayerdircor['location'][1]
    x_end=tswepassplayerdircor['pass_end_location'][0]
    y_end=tswepassplayerdircor['pass_end_location'][1]

    team_name=tswepassplayerdircor['team_name']

    circleSize=1

    playerpassingdircor = tswepassplayerdircor['player_name']

    if (team_name==away_team_required):
        if (playerpassingdircor == 'Rut Hedvig Lindahl' and tswepassplayerdircor['minute']==11):
            playernowpassing=playerpassingdircor

            SwePassPlayerDirCorCircle=plt.Circle((x_start,pitchWidthY-y_start),circleSize,color="yellow")
            SwePassPlayerDirCorCircle.set_alpha(.7)
            eu.add_patch(SwePassPlayerDirCorCircle)

            #David's code
            dx=x_end-x_start
            dy=y_end-y_start
            passLineDirectionCor=plt.Arrow(x_start,pitchWidthY-y_start,dx,dy,width=1.5,color="yellow")
            ft.add_patch(passLineDirectionCor)
            ft.annotate('FoT Code from Youtube', xy=(x_start,pitchWidthY-y_start), xytext=(x_end, y_end-25))

            dx=x_end-x_start
            dy=(pitchWidthY-y_end)-(pitchWidthY-y_start)
            anotherPassLineDirectionCor=plt.Arrow(x_start,pitchWidthY-y_start,dx,dy,width=1.5,color="yellow")
            ft.add_patch(anotherPassLineDirectionCor)
            ft.annotate('Update based on match video footage', xy=(x_start,pitchWidthY-y_start), xytext=(x_end, pitchWidthY-y_end))

            #My version
            #x_values=[x_start, x_end]
            #y_values=[pitchWidthY-y_start, pitchWidthY-y_end]
            #passLineDirection=plt.plot(x_values, y_values)
            #eu.annotate('', xy=(x_start,pitchWidthY-y_start), xytext=(x_end, pitchWidthY-y_end),
            #    arrowprops={'arrowstyle': '<-'}, va='center')


plt.text(5,83,away_team_required + ' ' + playernowpassing + ' originating passes')
plt.text(80,-3,'Created by Miguel Ponce de Leon / @miguelpdl . Data provided by StatsBomb', fontsize=6)

SwePassPlayerDirCor.set_size_inches(10, 7)
SwePassPlayerDirCor.savefig('Output/SWEpassesdirectionRHL.pdf', dpi=100)
SwePassPlayerDirCor.savefig('Output/SWEpassesdirectionRHL.png', dpi=300)
plt.show()

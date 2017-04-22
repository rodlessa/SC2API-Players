import requests;
import json;
import time;

def players():
    r = requests.get('http://localhost:6119/game/'); #load the sc2 json
    sc2data = json.loads(r.content)
    player = sc2data['players'] #store players data
    player1 = player[0]['name'] #get first player name
    player2 = player[1]['name'] #get second player name
    playerrace1 = player[0]['race'] #get first player race
    playerrace2 = player[1]['race'] #get second player race
    print ("Playing: ",'{} {} {} {} {}'.format(player1,playerrace1," vs ", player2,playerrace2), file=open("output.txt", "w")) #prints and format players names and race
    time.sleep(5) #checks info each 5 seconds

x = 1
while True:
    players()
    x+=1
import requests
import urllib.parse
import json
import csv 


#1. Define your variables normally w spaces
raw_name_game = "Bé Ly"
tag_line = "Ramen"

#2. Let Python encode the name
safe_name_game = urllib.parse.quote(raw_name_game)

#3. Use f string ti inject variable to url 
url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{safe_name_game}/{tag_line}"

#4. pack secret key into header
headers = {
    "X-Riot-Token" : "Your Riot Token"
}
#5. send the request and print the answer
response = requests.get(url,headers=headers)
print(response.status_code)
print(response.json())

data = response.json()
my_puuid = data["puuid"]
print("My PUUID is:" , my_puuid)

match_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{my_puuid}/ids?start=0&count=5"
match_response = requests.get(match_url,headers=headers)
match_ids = match_response.json()
print("My Recent Matches", match_ids)

wins = 0
total_games = len(match_ids)
total_kills = 0
total_gold = 0

print(f"\nAnalyzing {total_games} recent matches...")
print()


for match_id in match_ids:
    details_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(details_url, headers=headers)
    match_data = response.json()
    #print(json.dumps(match_data, indent=4))

    participants = match_data["info"]["participants"]

    for player in participants:
        if player["puuid"] == my_puuid:

            if player["win"] == True:
                wins += 1

            total_kills += player["kills"]

            total_gold += player["goldEarned"]


win_rate = (wins / total_games) * 100
print(f"You won {wins} out of {total_games} games.")
print(f"Your recent win rate is: {win_rate}%")

print()

kill_rate = (total_kills / total_games)
print(f"You killed {total_kills} enemies out of {total_games} games.")
print(f"Your recent kill rate is: {kill_rate}%")

print()

gold_rate = (total_gold / total_games)
print(f"You earned {total_gold} gold out of {total_games} games.")
print(f"Your recent gold rate is: {gold_rate} gold per game")

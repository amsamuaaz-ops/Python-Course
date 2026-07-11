team1 = 20
team2 = 40
team3 = 60
team4 = 65
team5 = 85

average = team1 + team2 + team3 + team4 + team5/5

star_per_point = 2
total_points = team1 + team2 + team3 + team4 + team5
totalstarpoints = total_points*star_per_point

box = 25
store_points = totalstarpoints//box
left_overstars = totalstarpoints % box

lastweek = 240
thisweek = 270
if thisweek > lastweek:
    print("This week has greater points then last week")
else:
    print("This week has lesser points then the last week")


team_url = str(input("Enter team ID: ")) # entering id of team(слава нб)

def getting_forum_url(team): # getting forum url method
    return f"https://liches.org/forum/team-{team}"

print(getting_forum_url(team_url)) # принтим результат


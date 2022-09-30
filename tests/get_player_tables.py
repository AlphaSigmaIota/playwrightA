import random, math

player = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6', 'Player7', 'Player8', 'Player9']

table_count = 2
table_size = math.ceil(len(player)/table_count)
print(f"Players on each table ({table_count} Tables): {table_size}")

for i in range(0, table_count):
    max_amount = table_size if table_size <= len(player) else len(player)
    print(max_amount)
    player_selection = random.sample(player, max_amount)
    print(f"Table {i+1}: {player_selection}")

    for player_name in player_selection:
        player.remove(player_name)

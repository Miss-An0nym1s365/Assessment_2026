game_history = []

history_item = f"Round: {rounds_played} - {round_feedback}"

game_history.append(history_item)

if rounds_played > 0:
    # Calculate Statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

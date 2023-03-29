def calculate_score(rolls_string):
    rolls = rolls_string.split()
    score = 0
    frame_index = 0
    for frame in range(1, len(rolls) + 1):
        if rolls[frame_index] == "X":
            score += 10
            score += sum(
                [
                    int(rolls[i])
                    for i in range(frame_index + 1, frame_index + 3)
                    if i < len(rolls)
                ]
            )
            frame_index += 1
        elif "/" in rolls[frame_index]:
            score += 10
            if len(rolls) > frame_index + 2:
                score += int(rolls[frame_index + 2])
            frame_index += 2
        else:
            score += sum([int(rolls[i]) for i in range(frame_index, frame_index + 2)])
            frame_index += 2
        if frame == 10 and (
            rolls[frame_index - 2] == "X" or "/" in rolls[frame_index - 2]
        ):
            if rolls[frame_index - 2] == "X":
                score += sum(
                    [int(rolls[i]) for i in range(frame_index, frame_index + 2)]
                )
            else:
                score += int(rolls[frame_index])
    return score

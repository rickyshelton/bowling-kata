from enum import Enum, auto
from dataclasses import dataclass


class FrameType(Enum):
    NORMAL = auto()
    STRIKE = auto()
    SPARE = auto()
    FINAL = auto()


@dataclass
class Frame:
    type: FrameType
    first_roll_score: int
    second_roll_score: int
    third_roll_score: int

    def score(self):
        return self.first_roll_score + self.second_roll_score + self.third_roll_score


def parse_frame_string(frame_string, is_final_frame):
    frame_type = None
    roll_scores = [0, 0, 0]
    rolls_list = list(frame_string)

    for roll_index, roll in enumerate(rolls_list):
        if roll == "X":
            frame_type = FrameType.STRIKE
            roll_scores[roll_index] = 10
        elif roll == "/":
            frame_type = FrameType.SPARE
            roll_scores[roll_index] = 10 - roll_scores[roll_index - 1]
        else:
            frame_type = FrameType.NORMAL
            roll_scores[roll_index] = int(roll)

    if is_final_frame:
        frame_type = FrameType.FINAL

    return Frame(frame_type, roll_scores[0], roll_scores[1], roll_scores[2])


def get_spare_bonus(next_frame):
    return next_frame.first_roll_score


def get_strike_bonus(next_frame, second_next_frame):
    bonus = 0
    if next_frame.type == FrameType.STRIKE:
        bonus += next_frame.score()
        bonus += second_next_frame.first_roll_score
    else:
        bonus += next_frame.first_roll_score + next_frame.second_roll_score
    return bonus


def get_score(game):
    total_score = 0
    frames_list = []
    frames_strings = game.split()
    num_frames = len(frames_strings)

    # build frame list
    for frame_index, frame_string in enumerate(frames_strings):
        is_final_frame = frame_index == num_frames - 1
        frame = parse_frame_string(frame_string, is_final_frame)
        frames_list.append(frame)

    # iterate over frames list and get scores
    for frame_index, frame in enumerate(frames_list):
        total_score += frame.score()

        if frame.type == FrameType.SPARE:
            next_frame = frames_list[frame_index + 1]
            total_score += get_spare_bonus(next_frame)

        if frame.type == FrameType.STRIKE:
            next_frame = frames_list[frame_index + 1]
            second_next_frame = (
                frames_list[frame_index + 2]
                if next_frame.type == FrameType.STRIKE
                else None
            )

            total_score += get_strike_bonus(next_frame, second_next_frame)

    return total_score

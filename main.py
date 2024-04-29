from enum import Enum


class Intervals(Enum):
    major_pentatonic = [0, 2, 4, 7, 9]
    minor_pentatonic = [0, 3, 5, 7, 10]
    major_blues = [0, 2, 3, 4, 7, 9]
    minor_blues = [0, 3, 5, 6, 7, 10]


class Notes(Enum):
    A = 'A'
    As = 'A#'
    B = 'B'
    C = 'C'
    Cs = 'C#'
    D = 'D'
    Ds = 'D#'
    E = 'E'
    F = 'F'
    Fs = 'F#'
    G = 'G'
    Gs = 'G#'


def get_enum_index(value):
    for i, member in enumerate(Notes):
        if member == value:
            return i


def get_enum(index):
    for i, member in enumerate(Notes):
        if i == index:
            return member.value


def get_pentatonic_scale(root_note, intervals):
    root_index = get_enum_index(root_note)

    scale_notes = [(root_index + interval) % 12 for interval in intervals.value]

    scale_notes_values = [get_enum(note_index) for note_index in scale_notes]

    return scale_notes_values


def print_fretboard():
    pentatonic_scale = get_pentatonic_scale(Notes.C, Intervals.major_pentatonic)
    strings = [Notes.E, Notes.B, Notes.G, Notes.D, Notes.A, Notes.E]

    for s in strings:
        line = '| '
        for i in range(23):
            note_index = (get_enum_index(s) + i) % 12
            if get_enum(note_index) in pentatonic_scale:
                line += ' '
                line += get_enum(note_index)
                if len(get_enum(note_index)) == 1:
                    line += ' '
            else:
                line += ' - '

            if i == 0:
                line += ' | '
        line += ' |'
        print(line)

    line = '\n| '
    for i in range(23):
        line += ' ' + str(i)
        if len(str(i)) == 1:
            line += ' '
        if i == 0:
            line += ' | '
    line += ' |'
    print(line)


if __name__ == '__main__':
    print_fretboard()

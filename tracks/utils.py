from mutagen import mp3


def zero_pad_to_length(token: str, length: int = 2):
    pad_times = len(token) - length
    return "{}{}".format("0" * (-1 * pad_times), token) if pad_times < 0 else token[pad_times:]


def convert_to_minutes(value: float | int) -> int:
    return int(value // 60)


def convert_to_seconds(value: float | int) -> int:
    return int(value % 60)


def get_track_duration(file_obj) -> str:
    audio = mp3.MP3(fileobj=file_obj)
    audio_length = audio.info.length
    remainder_hours = audio_length % 3600
    minutes = str(convert_to_minutes(remainder_hours))
    seconds = str(convert_to_seconds(remainder_hours))
    return "{}:{}".format(zero_pad_to_length(minutes), zero_pad_to_length(seconds))

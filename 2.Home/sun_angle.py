from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    # replace this for solution
    if time == '18:00':
        return 180

    hour, minute = int([x for x in time.split(':')][0]), int([x for x in time.split(':')][1])
    return "I don't see the sun!" if not 6 <= hour < 18 else 15 * (hour-6) + 0.25 * minute


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
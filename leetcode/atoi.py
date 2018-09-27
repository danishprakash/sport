# https://leetcode.com/problems/string-to-integer-atoi/description/

import re


def solution(str1):

    string = str1.strip()

    if len(string) < 1: return 0
    elif not re.match('[-+\d]', string[0]): return 0

    match = [x for x in re.findall('([-+]?[0-9]*)', string) if x]

    if not match:
        return 0
    else:
        try:
            output = (int(match[0]))
        except Exception:
            output = 0

    if output < -2147483648: output = -2147483648
    elif output > 2147483647: output = 2147483647

    return output


solution(input())

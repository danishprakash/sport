# https://leetcode.com/problems/unique-morse-code-words/description/

def solution(words):
    if len(words) < 1:
        return 0

    m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    code_list = list()

    for word in words:
        code = ""
        for l in word:
            code += m[ord(l)-97]
        code_list.append(code)

    com = len(set(code_list))
    return com if com > 0 else 1

solution(input())

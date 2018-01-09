class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = ''
        if str(x)[0] == '-':
            a = '-'
        return int(a + ''.join(list(map(str, ([int(x) for x in str(x) if ord(x) > 45][::-1])))))

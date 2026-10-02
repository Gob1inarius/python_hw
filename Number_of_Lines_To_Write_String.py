class Solution(object):
    def numberOfLines(self, widths, s):
        lines = 1
        cur_width = 0
        for letter in s:
            letter_width = widths[ord(letter) - ord('a')]
            if cur_width + letter_width <= 100:
                cur_width += letter_width
            else:
                lines += 1
                cur_width = letter_width
        return [lines, cur_width]
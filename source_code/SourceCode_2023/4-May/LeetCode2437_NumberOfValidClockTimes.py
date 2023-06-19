# -*-coding: utf-8-*-
# @Time  :2023/5/9 18:32
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2437_NumberOfValidClockTimes.py

'''
[2437. Number of Valid Clock Times]
You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.



Example 1:

Input: time = "?5:00"
Output: 2
Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.
Example 2:

Input: time = "0?:0?"
Output: 100
Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.
Example 3:

Input: time = "??:??"
Output: 1440
Explanation: There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.


Constraints:

time is a valid string of length 5 in the format "hh:mm".
"00" <= hh <= "23"
"00" <= mm <= "59"
Some of the digits might be replaced with '?' and need to be replaced with digits from 0 to 9.
'''


class Solution:
    def countTime(self, time: str) -> int:

        res = 1

        res = res * 10 if time[-1] == '?' else res
        res = res * 6 if time[-2] == '?' else res

        if time[0] == '2':
            return res if time[1] != '?' else 4 * res
        else:
            if time[1] == '?':
                return 20 * res + 4 * res if time[0] == '?' else 10 * res
            elif time[0] == '?':
                return res * 2 if int(time[1]) >= 4 else res * 3

        return res

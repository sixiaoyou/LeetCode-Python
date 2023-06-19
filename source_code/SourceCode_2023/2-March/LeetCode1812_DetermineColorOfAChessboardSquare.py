# -*-coding: utf-8-*-
# @Time  :2023/3/20 13:06
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1812_DetermineColorOfAChessboardSquare.py


'''
[LeetCode1812. Determine Color of a Chessboard Square]
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.



Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
Example 2:

Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
Example 3:

Input: coordinates = "c7"
Output: false


Constraints:

coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'
'''


class Solution:
    def squareIsWhiteV1(self, coordinates: str) -> bool:
        pf = 1 if coordinates[0] in 'aceg' else 0
        return True if pf ^ int(coordinates[1])%2 else False


    def squareIsWhiteV2(self, coordinates: str) -> bool:
        c1, c2 = coordinates[0], coordinates[1]
        a1, a2 = ord(c1) - 97, ord(c2) - 48
        return (a1 & 1) ^ (a2 & 1) == 0

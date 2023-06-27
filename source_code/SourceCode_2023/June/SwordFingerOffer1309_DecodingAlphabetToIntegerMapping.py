# -*-coding: utf-8-*-
# @Time  :2023/6/28 6:27
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: SwordFingerOffer1309_DecodingAlphabetToIntegerMapping.py

'''
[LeetCode1309. ������ĸ������ӳ��]
����һ���ַ��� s���������֣�'0' - '9'���� '#' ��ɡ�����ϣ������������ s ӳ��ΪһЩСдӢ���ַ���

�ַ���'a' - 'i'���ֱ��ã�'1' - '9'����ʾ��
�ַ���'j' - 'z'���ֱ��ã�'10#' - '26#'����ʾ��
����ӳ��֮���γɵ����ַ�����

��Ŀ���ݱ�֤ӳ��ʼ��Ψһ��



ʾ�� 1��

���룺s = "10#11#12"
�����"jkab"
���ͣ�"j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
ʾ�� 2��

���룺s = "1326#"
�����"acz"


��ʾ��

1 <= s.length <= 1000
s[i] ֻ�������֣�'0'-'9'���� '#' �ַ���
s ��ӳ��ʼ�մ��ڵ���Ч�ַ�����
'''


class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = ''
        while i < len(s):
            if i + 2 >= len(s):
                ans += chr(int(s[i]) + 96)
                i += 1
            else:
                if s[i+2] == '#':
                    ans += chr(int(s[i:i+2])+96)
                    i += 3
                else:
                    ans += chr(int(s[i]) + 96)
                    i += 1
        return ans
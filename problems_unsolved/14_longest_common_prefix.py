class Solution:
    def longest_common_prefix(self, list_of_strings: list) -> str:
        cls = self.__class__
        lengths_of_strings_in_list_of_strings = list()
        for string in list_of_strings:
            lengths_of_strings_in_list_of_strings.append(len(string))
        length_of_shortest_string = sorted(lengths_of_strings_in_list_of_strings)[0]
        for idx, string in enumerate(list_of_strings):
            for index in range(length_of_shortest_string):
                match_val = list_of_strings[0][index]
                if list(string)[index] == match_val:
                    continue
        return ''


_s = ['flower', 'flow', 'flight']
s = Solution()
s.longest_common_prefix(_s)
pass

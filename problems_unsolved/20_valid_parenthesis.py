class Solution:
    def isValid(self, s: str) -> bool:
        def not_(boolean) -> bool:
            return False if boolean else True
        at_curly, at_paren, at_skare = False, False, False
        closed_curly, closed_paren, closed_skare = True, True, True
        closed_curly_not, closed_paren_not, closed_skare_not = True, True, True
        open_curly, open_paren, open_skare = '{', '(', '['
        clos_curly, clos_paren, clos_skare = '}', ')', ']'
        for _char in s:
            closed_curly = not_(closed_curly) if _char in open_curly and closed_curly else closed_curly
            closed_paren = not_(closed_paren) if _char in open_paren and closed_paren else closed_paren
            closed_skare = not_(closed_skare) if _char in open_skare and closed_skare else closed_skare
            closed_curly = not_(closed_curly) if _char in clos_curly and not_(closed_curly) and closed_curly_not else closed_curly
            closed_paren = not_(closed_paren) if _char in clos_paren and not_(closed_paren) and closed_paren_not else closed_paren
            closed_skare = not_(closed_skare) if _char in clos_skare and not_(closed_skare) and closed_skare_not else closed_skare
            closed_curly_not = closed_paren and closed_skare
            closed_paren_not = closed_curly and closed_skare
            closed_skare_not = closed_curly and closed_paren
        all_closed = all([closed_curly, closed_paren, closed_skare])
        return True if all_closed else False


_input = '{[]}'
_s = Solution()
valid = _s.is_valid(_input)
pass

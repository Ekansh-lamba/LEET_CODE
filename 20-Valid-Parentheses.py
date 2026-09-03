class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for x in s:
            if x in "({[":
                st.append(x)
            else:
                if len(st) == 0:
                    return False
                elif st[-1] == "(" and x != ")":
                    return False
                elif st[-1] == "{" and x != "}":
                    return False
                elif st[-1] == "[" and x != "]":
                    return False
                else:
                    st.pop()
        if not st:
            return True
        else:
            return False

class Solution:
    def isValid(self, s: str) -> bool:
            if len(s) & 1: return False
            connections = {'(': ')', '[': ']', '{': '}'}
            opening = ['(', '[', '{']
            closing = [')', ']', '}']
            stack = []
            for c in s:
                if c in opening:
                    stack.append(c)
                if c in closing:
                    if not len(stack):
                        return False
                    toMatch = stack.pop()
                    if c != connections[toMatch]:
                        return False
            if len(stack):
                return False
            return True

if __name__ == "__main__":
    solutionObj = Solution()
    ses = ["()[]{}", "(]", "()", "([)]", "([{}])(){}[]", "{[()]){}()[]"]
    sols = [1, 0, 1, 0, 1, 1]
    ses = ['(){[()]}[()]']
    for i in range(len(ses)):
        print(i, solutionObj.isValid(ses[i]))
        
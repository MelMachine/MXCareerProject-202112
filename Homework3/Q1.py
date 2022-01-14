class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        paths = path.split('/')

        stack = []


        for i in range(len(paths)):
            if paths[i] == ".":
                continue
            elif paths[i] == "..":
                if stack:
                    stack.pop()

            elif paths[i]:
                stack.append(paths[i])

        return "/" + "/".join(stack)

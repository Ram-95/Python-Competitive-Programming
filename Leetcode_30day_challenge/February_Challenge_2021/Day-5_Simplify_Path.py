''' My Solution - O(N) Time and Space.'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialising a Stack with ''.
	st = ['']
	# Splitting the path and save it to list
        path = path.split('/')
        path = [x for x in path if x != '']
       
        n, i = len(path), 0
        while st and i < n:
	    # If current item is '..' the pop the contents of st (only if length of stack is more than 1)
            if path[i] == '..':
                if len(st) > 1:
                    st.pop()
	    # If current item is either '.' or '' or '/' then do nothing
            elif path[i] == '.' or path[i] == '' or path[i] == '/':
                pass
	    # If current item is neither of above, then append it to the stack
            else:
                st.append(path[i])
            i += 1
        
	# Join the contents of stack with '/' if stack != '' else simply return '/'
        return '/'.join(st) if len(st) > 1 else '/'

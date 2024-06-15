class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to hold matching pairs
        matching_pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_pairs:
                # Pop the top element from the stack if it's not empty; otherwise, use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the current closing bracket
                if matching_pairs[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        # The stack should be empty if the string is valid
        return not stack
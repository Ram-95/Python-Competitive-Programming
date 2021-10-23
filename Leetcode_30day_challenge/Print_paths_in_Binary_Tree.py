# Function to print all the paths of a Binary Tree | O(N) Time & Space

def get_paths(root, path, paths):
            if root is None:
                return
            path.append(root.val)
            get_paths(root.left, path, paths)
            get_paths(root.right, path, paths)
            
            
            if root.left is None and root.right is None:
                paths.append(list(path))
            
            # Pop here because, we're changing direction here.
            if path:
                path.pop()
        
        paths = []
        get_paths(root, [], paths)

def DFS(cur, target, visited: set) -> bool:
    """
    It used the system stack.
    The recursion uses the system stack.
    """
    if cur == target:
        return True
    for nei in cur.neighbors:
        if nei not in visited:
            visited.add(nei)
        if DFS(nei, target, visited):
            return True
    return False

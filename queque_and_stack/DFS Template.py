def DFS(cur, target, visited: set) -> bool:
    if cur == target:
        return True
    for nei in cur.neighbors:
        if nei not in visited:
            visited.add(nei)
        if DFS(nei, target, visited):
            return True
    return False

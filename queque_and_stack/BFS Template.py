def BFS(root, target) -> int:
    queue = []
    step = 0
    queue.append(root)
    while queue:
        for node in queue:
            if node == target:
                return step
            # Add all node neighbors into the queue
            for neighbor in node.neighbors:
                queue.append(neighbor)
            queue.pop(0)
        step += 1
    # There is no path from root to target.
    return -1


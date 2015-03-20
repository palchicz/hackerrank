from collections import deque

def convert_to_tree(g, root = None):
    queue = deque()
    tree = {}
    current = root
    if not current:
         current = list(g.keys())[0]
    queue.appendleft(current)
    while queue:
        current = queue.pop()
        if current not in tree:
            children = set(g[current]) - set(tree.keys())
            tree[current] = children
            for child in children:
                queue.appendleft(child)
    return tree

def convert_edges_to_graph(edges):
    g = {}
    for u, v in edges:
        if u not in g:
            g[u] = set()
        if v not in g:
            g[v] = set()
        g[u].add(v)
        g[v].add(u)
    return g

def get_subtree_sizes(g, root = None):
    sizes = {}
    if not g:
        return sizes
    if not root:
        root = list(g.keys())[0]
    stack = [root]
    visited = set()
    processed = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            stack.append(current)
            for child in g[current] - visited:
                stack.append(child)
            visited.add(current)
        else:
            sizes[current] = 1
            for child in g[current] & processed:
                sizes[current] += sizes[child]
            processed.add(current)

    return sizes

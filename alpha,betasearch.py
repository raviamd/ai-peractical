tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
root = 0
pruned = 0

def children(branch, depth, alpha, beta):
    global tree, root, pruned
    i = 0
    for child in branch:
        if isinstance(child, list):
            nalpha, nbeta = children(child, depth + 1, alpha, beta)
            if depth % 2 == 1:
                beta = nalpha if nalpha < beta else beta
            else:
                alpha = nbeta if nbeta > alpha else alpha
            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:
            if depth % 2 == 0 and alpha < child:
                alpha = child
            if depth % 2 == 1 and beta > child:
                beta = child
            if alpha >= beta:
                pruned += 1
                break
    
    if depth == root:
        tree = alpha if root == 0 else beta
        return alpha, beta
    else:
        return alpha, beta

def alphabeta(in_tree=tree, start=root, upper=-15, lower=15):
    global tree, root, pruned
    alpha, beta = children(tree, start, upper, lower)
    
    if __name__ == "__main__":
        print("(alpha, beta): ", alpha, beta)
        print("Result: ", tree)
        print("Times pruned: ", pruned)
    
    return alpha, beta, tree, pruned

if __name__ == "__main__":
    alphabeta()


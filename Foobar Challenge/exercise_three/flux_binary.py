def solution(h, q):
    tree = generate_tree(h)
    total_nodes = get_total_nodes_at_each_depth(h)

    """"
    Loop over each depth in the tree and build an array of the indexes in order of
    post-order traversal
    """
    for depth in range(h):

        # store last the number to increment it to the next
        last_number = 0

        # Work out how many nodes exist under each node
        for x_nodes in range(total_nodes[depth]):
            total_child_nodes = 2 ** (h - depth) - 1
            tree[depth].append(last_number + total_child_nodes)
            last_number += total_child_nodes

        """
        The above code lists out all the nodes with the number of nodes beneath them but not
        in the order of post-order traversal 

        These numbers can be converted to post-order traversal by calculating the number of nodes on above branches
        which are ordered before the current node and then using it to increment the node
        """
        increment_positions = []

        for index in range(len(tree)):
            if index == depth:
                break
            elif index != 0 and index != len(tree) - 1 and len(tree[index]) != 0:
                increment_positions.append(len(tree[index]))

        total_increment = 0

        for x in range(len(tree[depth])):
            for increment_pos in increment_positions:
                if x % increment_pos == 0 and x != 0:
                    total_increment += 1

            value = tree[depth][x]
            tree[depth][x] = value + total_increment

    answer = []

    # Loops over each index in Q and calculates which node is above
    for q_index in q:

        # return -1 if the index is at the top of the tree
        if q_index == 2 ** h - 1:
            answer.append(-1)
            continue

        # Find which row the index node is in
        for x in range(len(tree)):
            if q_index in tree[x]:
                in_row_index = tree[x].index(q_index) + 1

                # Calculate the index of the above node in it's tree list
                if in_row_index % 2 == 0:
                    above_index = in_row_index // 2
                else:
                    above_index = (in_row_index + 1) // 2

                # retrieve the answer from the tree list using the index
                answer.append(tree[x - 1][above_index - 1])

    return answer


# Gets the total number of nodes at each depth in an list with each element representing a depth
def get_total_nodes_at_each_depth(h):
    total_nodes_all_lvls = []

    for depth in range(h):
        total_nodes_all_lvls.append(2 ** depth)

    return total_nodes_all_lvls


# Builds an empty tree of the height specified
def generate_tree(h):
    tree = []

    for x in range(h):
        tree.append([])

    return tree

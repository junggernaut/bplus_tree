# Check carefully the format of the tree representation in text
# Note that the last node in each branch or level (including the root) is denoted by `-

answer1_1 = """Insert 72
`- [72]
Insert 99
`- [72, 99]
Insert 67
`- [67, 72, 99]
Insert 70
`- [67, 70, 72, 99]
Insert 52
`- [70]
   |- [52, 67]
   `- [70, 72, 99]
Insert 28
`- [70]
   |- [28, 52, 67]
   `- [70, 72, 99]
Insert 27
`- [70]
   |- [27, 28, 52, 67]
   `- [70, 72, 99]
Insert 89
`- [70]
   |- [27, 28, 52, 67]
   `- [70, 72, 89, 99]
Insert 94
`- [70, 89]
   |- [27, 28, 52, 67]
   |- [70, 72]
   `- [89, 94, 99]
Insert 10
`- [28, 70, 89]
   |- [10, 27]
   |- [28, 52, 67]
   |- [70, 72]
   `- [89, 94, 99]"""

answer1_2 = """Insert 35
`- [35]
Insert 71
`- [35, 71]
Insert 44
`- [35, 44, 71]
Insert 60
`- [35, 44, 60, 71]
Insert 81
`- [60]
   |- [35, 44]
   `- [60, 71, 81]
Insert 61
`- [60]
   |- [35, 44]
   `- [60, 61, 71, 81]
Insert 29
`- [60]
   |- [29, 35, 44]
   `- [60, 61, 71, 81]
Insert 95
`- [60, 71]
   |- [29, 35, 44]
   |- [60, 61]
   `- [71, 81, 95]
Insert 63
`- [60, 71]
   |- [29, 35, 44]
   |- [60, 61, 63]
   `- [71, 81, 95]
Insert 23
`- [60, 71]
   |- [23, 29, 35, 44]
   |- [60, 61, 63]
   `- [71, 81, 95]"""

answer1_3 = """Insert 29
`- [29]
Insert 26
`- [26, 29]
Insert 40
`- [26, 29, 40]
Insert 34
`- [26, 29, 34, 40]
Insert 65
`- [34]
   |- [26, 29]
   `- [34, 40, 65]
Insert 73
`- [34]
   |- [26, 29]
   `- [34, 40, 65, 73]
Insert 15
`- [34]
   |- [15, 26, 29]
   `- [34, 40, 65, 73]
Insert 12
`- [34]
   |- [12, 15, 26, 29]
   `- [34, 40, 65, 73]
Insert 82
`- [34, 65]
   |- [12, 15, 26, 29]
   |- [34, 40]
   `- [65, 73, 82]
Insert 44
`- [34, 65]
   |- [12, 15, 26, 29]
   |- [34, 40, 44]
   `- [65, 73, 82]"""

answer1_4 = """Insert 28
`- [28]
Insert 50
`- [28, 50]
Insert 9
`- [9, 28, 50]
Insert 44
`- [9, 28, 44, 50]
Insert 15
`- [28]
   |- [9, 15]
   `- [28, 44, 50]
Insert 68
`- [28]
   |- [9, 15]
   `- [28, 44, 50, 68]
Insert 12
`- [28]
   |- [9, 12, 15]
   `- [28, 44, 50, 68]
Insert 73
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44]
   `- [50, 68, 73]
Insert 49
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44, 49]
   `- [50, 68, 73]
Insert 62
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44, 49]
   `- [50, 62, 68, 73]"""

answer1_5 = """Insert 3
`- [3]
Insert 97
`- [3, 97]
Insert 18
`- [3, 18, 97]
Insert 96
`- [3, 18, 96, 97]
Insert 82
`- [82]
   |- [3, 18]
   `- [82, 96, 97]
Insert 84
`- [82]
   |- [3, 18]
   `- [82, 84, 96, 97]
Insert 41
`- [82]
   |- [3, 18, 41]
   `- [82, 84, 96, 97]
Insert 67
`- [82]
   |- [3, 18, 41, 67]
   `- [82, 84, 96, 97]
Insert 56
`- [41, 82]
   |- [3, 18]
   |- [41, 56, 67]
   `- [82, 84, 96, 97]
Insert 11
`- [41, 82]
   |- [3, 11, 18]
   |- [41, 56, 67]
   `- [82, 84, 96, 97]"""

answer1_6 = """Insert 8
`- [8]
Insert 13
`- [8, 13]
Insert 19
`- [8, 13, 19]
Insert 28
`- [8, 13, 19, 28]
Insert 60
`- [19]
   |- [8, 13]
   `- [19, 28, 60]
Insert 69
`- [19]
   |- [8, 13]
   `- [19, 28, 60, 69]
Insert 81
`- [19, 60]
   |- [8, 13]
   |- [19, 28]
   `- [60, 69, 81]
Insert 34
`- [19, 60]
   |- [8, 13]
   |- [19, 28, 34]
   `- [60, 69, 81]
Insert 42
`- [19, 60]
   |- [8, 13]
   |- [19, 28, 34, 42]
   `- [60, 69, 81]
Insert 51
`- [19, 34, 60]
   |- [8, 13]
   |- [19, 28]
   |- [34, 42, 51]
   `- [60, 69, 81]
Insert 84
`- [19, 34, 60]
   |- [8, 13]
   |- [19, 28]
   |- [34, 42, 51]
   `- [60, 69, 81, 84]
Insert 88
`- [19, 34, 60, 81]
   |- [8, 13]
   |- [19, 28]
   |- [34, 42, 51]
   |- [60, 69]
   `- [81, 84, 88]
Insert 74
`- [19, 34, 60, 81]
   |- [8, 13]
   |- [19, 28]
   |- [34, 42, 51]
   |- [60, 69, 74]
   `- [81, 84, 88]
Insert 91
`- [19, 34, 60, 81]
   |- [8, 13]
   |- [19, 28]
   |- [34, 42, 51]
   |- [60, 69, 74]
   `- [81, 84, 88, 91]
Insert 17
`- [19, 34, 60, 81]
   |- [8, 13, 17]
   |- [19, 28]
   |- [34, 42, 51]
   |- [60, 69, 74]
   `- [81, 84, 88, 91]
Insert 11
`- [19, 34, 60, 81]
   |- [8, 11, 13, 17]
   |- [19, 28]
   |- [34, 42, 51]
   |- [60, 69, 74]
   `- [81, 84, 88, 91]
Insert 99
`- [60]
   |- [19, 34]
   |  |- [8, 11, 13, 17]
   |  |- [19, 28]
   |  `- [34, 42, 51]
   `- [81, 88]
      |- [60, 69, 74]
      |- [81, 84]
      `- [88, 91, 99]"""

# `- [28, 70, 89]
#    |- [10, 27]
#    |- [28, 52, 67]
#    |- [70, 72]
#    `- [89, 94, 99]
answer2_1 = """
Delete 67
`- [28, 70, 89]
   |- [10, 27]
   |- [28, 52]
   |- [70, 72]
   `- [89, 94, 99]
Delete 10
`- [70, 89]
   |- [27, 28, 52]
   |- [70, 72]
   `- [89, 94, 99]
Delete 99
`- [70, 89]
   |- [27, 28, 52]
   |- [70, 72]
   `- [89, 94]
Delete 94
`- [70]
   |- [27, 28, 52]
   `- [70, 72, 89]"""

# `- [60, 71]
#    |- [23, 29, 35, 44]
#    |- [60, 61, 63]
#    `- [71, 81, 95]
answer2_2 = """
Delete 71
`- [60, 71]
   |- [23, 29, 35, 44]
   |- [60, 61, 63]
   `- [81, 95]
Delete 61
`- [60, 71]
   |- [23, 29, 35, 44]
   |- [60, 63]
   `- [81, 95]
Delete 95
`- [60]
   |- [23, 29, 35, 44]
   `- [60, 63, 81]
Delete 63
`- [60]
   |- [23, 29, 35, 44]
   `- [60, 81]
Delete 81
`- [44]
   |- [23, 29, 35]
   `- [44, 60]"""

# `- [34, 65]
#    |- [12, 15, 26, 29]
#    |- [34, 40, 44]
#    `- [65, 73, 82]
answer2_3 = """
Delete 40
`- [34, 65]
   |- [12, 15, 26, 29]
   |- [34, 44]
   `- [65, 73, 82]
Delete 82
`- [34, 65]
   |- [12, 15, 26, 29]
   |- [34, 44]
   `- [65, 73]
Delete 29
`- [34, 65]
   |- [12, 15, 26]
   |- [34, 44]
   `- [65, 73]
Delete 15
`- [34, 65]
   |- [12, 26]
   |- [34, 44]
   `- [65, 73]"""

# Insert 62
# `- [28, 50]
#    |- [9, 12, 15]
#    |- [28, 44, 49]
#    `- [50, 62, 68, 73]
answer2_4 = """
Delete 50
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44, 49]
   `- [62, 68, 73]
Delete 62
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44, 49]
   `- [68, 73]
Delete 49
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44]
   `- [68, 73]
Delete 73
`- [28]
   |- [9, 12, 15]
   `- [28, 44, 68]"""

# `- [41, 82]
#    |- [3, 11, 18]
#    |- [41, 56, 67]
#    `- [82, 84, 96, 97]
answer2_5 = """
Delete 18
`- [41, 82]
   |- [3, 11]
   |- [41, 56, 67]
   `- [82, 84, 96, 97]
Delete 67
`- [41, 82]
   |- [3, 11]
   |- [41, 56]
   `- [82, 84, 96, 97]
Delete 96
`- [41, 82]
   |- [3, 11]
   |- [41, 56]
   `- [82, 84, 97]
Delete 82
`- [41, 82]
   |- [3, 11]
   |- [41, 56]
   `- [84, 97]
Delete 97
`- [41]
   |- [3, 11]
   `- [41, 56, 84]
Delete 41
`- [41]
   |- [3, 11]
   `- [56, 84]
Delete 56
`- [3, 11, 84]"""

# The file name must be bptree.py (case sensitive)
# The class name must be BPTree (case sensitive)

# Let's fix n to be 5. That is, a node can hold up to 4 search keys
# Let's assume that there is NO duplicate key


class Node:
    def __init__(self):
        self.keys = []
        self.pointers = []
        self.parent = None

    def split_leaf_node(self, new_key):
        new_node = Node()
        self.insert_key(new_key)
        new_node.keys = self.keys[2:]
        self.keys = self.keys[:2]
        return self, new_node

    def insert_key(self, key):
        self.keys.append(key)
        self.keys.sort()


class BPTree(object):
    def __init__(self):
        self.root = Node()

    def insert_in_parent(self, left_node, insert_value, right_node):
        if left_node.parent is None:
            new_root = Node()
            new_root.keys.append(insert_value)
            new_root.pointers.append(left_node)
            new_root.pointers.append(right_node)
            left_node.parent = new_root
            right_node.parent = new_root
            self.root = new_root
        else:
            parent_node = left_node.parent
            for idx, key in enumerate(parent_node.keys):
                if insert_value < key:
                    parent_node.keys.insert(idx, insert_value)
                    parent_node.pointers.insert(idx + 1, right_node)
                    break
                elif idx == len(parent_node.keys) - 1:
                    parent_node.keys.append(insert_value)
                    parent_node.pointers.append(right_node)
                    break
            if len(parent_node.keys) < 5:
                right_node.parent = parent_node
            else:
                right_parent_node = Node()
                right_parent_node.keys = parent_node.keys[3:]
                right_parent_node.pointers = parent_node.pointers[3:]
                insert_value = parent_node.keys[2]
                parent_node.keys = parent_node.keys[:2]
                parent_node.pointers = parent_node.pointers[:3]
                for pointer in parent_node.pointers:
                    pointer.parent = parent_node
                for pointer in right_parent_node.pointers:
                    pointer.parent = right_parent_node
                self.insert_in_parent(parent_node, insert_value, right_parent_node)

    def print_tree(self, node, level, is_last, prefix):
        tree = ""
        tree += f"{prefix}{'`-' if is_last else '|-'} {node.keys}\n"
        prefix += "   " if is_last else "|  "
        for idx, pointer in enumerate(node.pointers):
            tree += self.print_tree(
                pointer, level + 1, (len(node.pointers) - 1 == idx), prefix
            )
        return tree

    def find_leaf_node(self, search_key):
        node = self.root
        while len(node.pointers) > 0:
            for idx, key in enumerate(node.keys):
                if search_key < key:
                    node = node.pointers[idx]
                    break
                elif idx == len(node.keys) - 1:
                    node = node.pointers[idx + 1]
        return node

    def find_sibling(self, node):
        parent_node = node.parent
        for idx, pointer in enumerate(parent_node.pointers):
            if pointer == node:
                if idx == 0:
                    return (
                        parent_node.pointers[1],
                        parent_node.keys[0],
                        True,
                    )
                else:
                    return (
                        parent_node.pointers[idx - 1],
                        parent_node.keys[idx - 1],
                        False,
                    )

    def insert(self, key, value):
        if len(self.root.keys) == 0:
            self.root.keys.append(key)
        else:
            leaf_node = self.find_leaf_node(key)
            if len(leaf_node.keys) < 4:
                leaf_node.insert_key(key)
            else:
                left_node, right_node = leaf_node.split_leaf_node(key)
                self.insert_in_parent(left_node, right_node.keys[0], right_node)
        print_tree = "Insert %d\n" % key
        print_tree += self.print_tree(self.root, 0, True, "")
        return print_tree

    def delete_entry(self, node, delete_key, delete_pointer):
        if delete_pointer is not None:
            node.pointers.remove(delete_pointer)
        node.keys.remove(delete_key)
        if node.parent is None:
            if len(node.pointers) == 1:
                self.root = node.pointers[0]
                self.root.parent = None
            return
        else:
            if (len(node.pointers) == 0 and len(node.keys) >= 2) or len(
                node.pointers
            ) >= 3:
                return
            else:
                (sibling, between_key, is_right) = self.find_sibling(node)
                if ((len(node.keys) + len(sibling.keys)) <= 4) and (
                    (len(node.pointers) + len(sibling.pointers)) <= 5
                ):
                    if is_right:
                        for key in node.keys:
                            if len(node.pointers) > 0:
                                sibling.keys.insert(0, between_key)
                                for pointer in node.pointers:
                                    pointer.parent = sibling
                                sibling.pointers = node.pointers + sibling.pointers
                            sibling.keys.insert(0, key)
                    else:
                        for key in node.keys:
                            if len(node.pointers) > 0:
                                sibling.keys.append(between_key)
                                for pointer in node.pointers:
                                    pointer.parent = sibling
                                    sibling.pointers.append(pointer)
                            sibling.keys.append(key)

                    self.delete_entry(node.parent, between_key, node)
                else:
                    parent = node.parent
                    between_key_idx = parent.keys.index(between_key)
                    if is_right:
                        if len(node.pointers) > 0:
                            node.keys.append(between_key)
                            moving_pointer = sibling.pointers.pop(0)
                            moving_pointer.parent = node
                            node.pointers.append(moving_pointer)
                            parent.keys[between_key_idx] = sibling.keys.pop(0)
                        else:
                            node.keys.append(sibling.keys.pop(0))
                            parent.keys[between_key_idx] = sibling.keys[0]
                    else:
                        if len(node.pointers) > 0:
                            node.keys.insert(0, between_key)
                            moving_pointer = sibling.pointers.pop()
                            moving_pointer.parent = node
                            node.pointers.insert(0, moving_pointer)
                            parent.keys[between_key_idx] = sibling.keys.pop()
                        else:
                            moving_value = sibling.keys.pop()
                            node.keys.insert(0, moving_value)
                            parent.keys[between_key_idx] = moving_value

    def delete(self, key):
        leaf_node = self.find_leaf_node(key)
        self.delete_entry(leaf_node, key, None)
        print_tree = "Delete %d\n" % key
        print_tree += self.print_tree(self.root, 0, True, "")
        return print_tree

    def show(self, insert_keys, delete_keys):
        result = ""
        for key in insert_keys:
            result += self.insert(key, key)
        for key in delete_keys:
            result += self.delete(key)
        self.root = Node()
        return result[:-1]


# IMPORTANT:
# Using a unittest library, your BPTree implementation will be imported,
# and the following code with a different input will be executed.

if __name__ == "__main__":
    bpt = BPTree()
    print(bpt.show([72, 99, 67, 70, 52, 28, 27, 89, 94, 10], []) == answer1_1)
    print(bpt.show([35, 71, 44, 60, 81, 61, 29, 95, 63, 23], []) == answer1_2)
    print(bpt.show([29, 26, 40, 34, 65, 73, 15, 12, 82, 44], []) == answer1_3)
    print(bpt.show([28, 50, 9, 44, 15, 68, 12, 73, 49, 62], []) == answer1_4)
    print(bpt.show([3, 97, 18, 96, 82, 84, 41, 67, 56, 11], []) == answer1_5)
    print(
        bpt.show(
            [8, 13, 19, 28, 60, 69, 81, 34, 42, 51, 84, 88, 74, 91, 17, 11, 99], []
        )
        == answer1_6
    )

    print(
        bpt.show([72, 99, 67, 70, 52, 28, 27, 89, 94, 10], [67, 10, 99, 94])
        == answer1_1 + answer2_1
    )
    print(
        bpt.show([35, 71, 44, 60, 81, 61, 29, 95, 63, 23], [71, 61, 95, 63, 81])
        == answer1_2 + answer2_2
    )
    print(
        bpt.show([29, 26, 40, 34, 65, 73, 15, 12, 82, 44], [40, 82, 29, 15])
        == answer1_3 + answer2_3
    )
    print(
        bpt.show([28, 50, 9, 44, 15, 68, 12, 73, 49, 62], [50, 62, 49, 73])
        == answer1_4 + answer2_4
    )
    print(
        bpt.show([3, 97, 18, 96, 82, 84, 41, 67, 56, 11], [18, 67, 96, 82, 97, 41, 56])
        == answer1_5 + answer2_5
    )

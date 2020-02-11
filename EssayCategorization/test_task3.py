import unittest
from tm_trees import *
from a2_test_task2 import set_expanded, is_leaf,set_size

def eq_tree(tree1, tree2):
    return tree1._name == tree2._name

class a2_test_task3(unittest.TestCase):
    def test_single_leaf(self):
        leaf = TMTree("leaf", [], 50)
        leaf.update_rectangles((0,0,10,20))
        self.assertEqual(leaf.get_tree_at_position((20,30)), None, "This is out of boundary None")

    def test_out_of_boundary(self):
        leaf = TMTree("leaf", [], 50)
        leaf.update_rectangles((0, 0, 10, 20))
        self.assertEqual(leaf.get_tree_at_position((10, 30)), None,
                         "This is out of boundary None")

    def test_out_of_boundary2(self):
        leaf = TMTree("leaf", [], 50)
        leaf.update_rectangles((0, 0, 10, 20))
        self.assertEqual(leaf.get_tree_at_position((0, 30)), None,
                         "This is out of boundary None")

    def test_single_leaf2(self):
        leaf = TMTree("leaf", [], 50)
        leaf.update_rectangles((0,0,10,20))
        self.assertEqual(leaf.get_tree_at_position((0,5)), leaf, "There is only one leaf in the displayed tree stasitied the condition thus you must return the leaf")

    def test_left_corner_no_expanded(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 50)
        root = TMTree("root", [leaf, leaf2], 0)
        root.update_rectangles((0,0,10,20))
        act = root.get_tree_at_position((0,0))
        self.assertEqual(act, root, "The root is the only leaf in the DISPLAYED Tree" " YOUR RESULT IS " + act._name)

    def test_left_corner_expanded(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 50)
        root = TMTree("root", [leaf, leaf2], 0)
        root.update_rectangles((0,0,10,20))
        set_expanded(root)
        act = root.get_tree_at_position((0,0))
        self.assertEqual(act, leaf, "The leaf is the only qualified leaf in the DISPLAYED Tree"+ " YOUR RESULT IS " + act._name)

    def test_vertical_bottom(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 50)
        root = TMTree("root", [leaf, leaf2], 0)
        root.update_rectangles((0, 0, 10, 20))
        set_expanded(root)
        act = root.get_tree_at_position((10, 20))
        self.assertEqual(act, leaf2,
                         "The leaf2 is the only qualified leaf in the DISPLAYED Tree"+ " YOUR RESULT IS " + act._name)

    def test_vertical_intersection(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 50)
        root = TMTree("root", [leaf, leaf2], 0)
        root.update_rectangles((0, 0, 10, 20))
        set_expanded(root)
        act = (root.get_tree_at_position((5, 10)))
        self.assertEqual(act, leaf,
                         "The leaf is the only qualified leaf in the DISPLAYED Tree"+ " YOUR RESULT IS " + act._name)

    def test_horizontal_intersection(self):
        leaf = TMTree("leaf", [], 10)
        leaf2 = TMTree("leaf2", [], 50)
        root = TMTree("root", [leaf, leaf2], 0)
        root.update_rectangles((0, 0, 20, 10))
        set_expanded(root)
        act = root.get_tree_at_position((3, 10))
        self.assertEqual(act, leaf,
                         "The leaf is the only qualified leaf in the DISPLAYED Tree"+ " YOUR RESULT IS " + act._name)

    def test_two_leaf_left(self):
        leaf = TMTree("leaf", [], 10)
        leaf2 = TMTree("leaf2", [], 50)
        root = TMTree("root", [leaf, leaf2], 0)
        root.update_rectangles((0, 0, 20, 10))
        set_expanded(root)
        act = root.get_tree_at_position((3, 10))
        self.assertEqual(act, leaf,
                         "The leaf is the only qualified leaf in the DISPLAYED Tree" + " YOUR RESULT IS " + act._name)

    def test_two_rectangle_left(self):
        leaf = TMTree("leaf", [], 10)
        leaf2 = TMTree("leaf2", [], 40)
        leaf3 = TMTree("leaf3", [], 50)
        folderA = TMTree("folderA", [leaf, leaf2], 0)
        root = TMTree("root", [folderA, leaf3], 0)
        root.update_rectangles((0, 0, 20, 10))
        root._expanded = True
        exp = folderA
        act = root.get_tree_at_position((3, 10))
        self.assertEqual(act, exp,
                         "The folderA is the only qualified leaf in the DISPLAYED Tree YOUR RESULT IS " + act._name)

    def test_three_rectangle_horizontal(self):
        leaf = TMTree("leaf", [], 10)
        leaf2 = TMTree("leaf2", [], 40)
        leaf3 = TMTree("leaf3", [], 50)
        folderA = TMTree("folderA", [leaf, leaf2], 0)
        root = TMTree("root", [folderA, leaf3], 0)
        root.update_rectangles((0, 0, 20, 10))
        root._expanded = True
        folderA._expanded = True
        exp = leaf2
        act = root.get_tree_at_position((3, 10))
        self.assertEqual(act, exp,
                         "The leaf2 is the only qualified leaf in the DISPLAYED Tree YOUR RESULT IS " + act._name)

    def test_three_rectangle_intersection(self):
        leaf = TMTree("leaf", [], 10)
        leaf2 = TMTree("leaf2", [], 40)
        leaf3 = TMTree("leaf3", [], 50)
        folderA = TMTree("folderA", [leaf, leaf2], 0)
        root = TMTree("root", [folderA, leaf3], 0)
        root.update_rectangles((0, 0, 20, 10))
        root._expanded = True
        folderA._expanded = True
        exp = leaf
        act = root.get_tree_at_position((5, 2))
        self.assertEqual(act, exp,
                         "The leaf is the only qualified leaf in the DISPLAYED Tree YOUR RESULT IS " + act._name)

    def test_three_rectangle_intersection_2(self):
        leaf = TMTree("leaf", [], 10)
        leaf2 = TMTree("leaf2", [], 40)
        leaf3 = TMTree("leaf3", [], 50)
        folderA = TMTree("folderA", [leaf, leaf2], 0)
        root = TMTree("root", [folderA, leaf3], 0)
        root.update_rectangles((0, 0, 20, 10))
        root._expanded = True
        folderA._expanded = True
        exp = leaf
        act = root.get_tree_at_position((10, 2))
        self.assertEqual(act, exp,
                         "The leaf is the only qualified leaf in the DISPLAYED Tree YOUR RESULT IS " + act._name)

    def test_three_rectangle_intersection_3(self):
        leaf = TMTree("leaf", [], 10)
        leaf2 = TMTree("leaf2", [], 40)
        leaf3 = TMTree("leaf3", [], 50)
        folderA = TMTree("folderA", [leaf, leaf2], 0)
        root = TMTree("root", [leaf3, folderA], 0)
        root.update_rectangles((0, 0, 10, 18))
        root._expanded = True
        folderA._expanded = True
        exp = leaf3
        act = root.get_tree_at_position((9, 2))
        self.assertEqual(act, exp,
                         "The leaf3 is the only qualified leaf in the DISPLAYED Tree YOUR RESULT IS " + act._name)

    def test_three_rectangle_intersection_4(self):
        leaf = TMTree("leaf", [], 10)
        leaf2 = TMTree("leaf2", [], 40)
        leaf3 = TMTree("leaf3", [], 50)
        folderA = TMTree("folderA", [leaf, leaf2], 0)
        root = TMTree("root", [leaf3, folderA], 0)
        root.update_rectangles((0, 0, 20, 10))
        root._expanded = True
        folderA._expanded = True
        exp = leaf
        act = root.get_tree_at_position((11, 2))
        self.assertEqual(act, exp,
                         "The leaf is the only qualified leaf in the DISPLAYED Tree YOUR RESULT IS " + act._name)



    def test_four_square_intersection(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 50)
        leaf3 = TMTree("leaf3", [], 50)
        leaf4 = TMTree("leaf4", [], 50)
        internal1 = TMTree("internal1", [leaf, leaf2], 0)
        internal2 = TMTree("internal2", [leaf3, leaf4], 0)
        root = TMTree("root", [internal1, internal2], 0)
        rect = (0, 0, 100, 100)
        set_expanded(root)
        root.update_rectangles(rect)
        exp = leaf
        act = root.get_tree_at_position((10, 2))
        self.assertEqual(act, exp,
                         "The leaf is the only qualified leaf in the DISPLAYED Tree YOUR RESULT IS " + act._name)


unittest.main(exit=False)

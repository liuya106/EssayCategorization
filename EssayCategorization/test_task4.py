import unittest
from tm_trees import *
from a2_test_task2 import set_expanded, is_leaf


class a2_test_update_size(unittest.TestCase):
    def test_leaf(self):
        leaf = TMTree("leaf", [], 50)
        leaf.change_size(0.1)
        exp = 55
        act = leaf.update_data_sizes()
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(act))

    def test_folder(self):
        leaf = TMTree("leaf", [], 50)
        folder = TMTree("root", [leaf], 0)
        leaf.data_size = 55
        exp = 55
        act = folder.update_data_sizes()
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(act))

    def test_folder2(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 60)
        root = TMTree("root", [leaf, leaf2], 0)
        leaf.data_size = 60
        leaf2.data_size = 70
        exp = 130
        act = root.update_data_sizes()
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(act))

    def test_folder3(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 60)
        folderA = TMTree("folder", [leaf, leaf2], 0)
        leaf3 = TMTree("leaf3", [], 70)
        leaf4 = TMTree("leaf4", [], 80)
        folderB = TMTree("folder", [leaf3, leaf4], 0)
        root = TMTree("root", [folderA, folderB], 0)
        leaf.data_size = 60
        leaf2.data_size = 70
        exp = 130
        act = folderA.update_data_sizes()
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(act))
        self.assertNotEqual(root.data_size, 280, "You should not change the data size of parent tree")

    def test_folder4(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 60)
        folderA = TMTree("folder", [leaf, leaf2], 0)
        leaf3 = TMTree("leaf3", [], 70)
        leaf4 = TMTree("leaf4", [], 80)
        folderB = TMTree("folder", [leaf3, leaf4], 0)
        root = TMTree("root", [folderA, folderB], 0)
        leaf.data_size = 60
        leaf2.data_size = 70
        exp = 280
        act = root.update_data_sizes()
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(act))
        self.assertEqual(root.data_size, exp, "Expected " + str(exp) + " Your result is " + str(act))
        self.assertEqual(folderA.data_size, 130, "You should also update the data size of folderA")



class a2_test_change_size(unittest.TestCase):
    def test_up(self):
        leaf = TMTree("leaf", [], 50)
        leaf.change_size(0.1)
        leaf.update_data_sizes()
        exp = 55
        act = leaf.data_size
        self.assertEqual(act, exp, "Expected "+str(exp)+" Your result is "+str(act))


    def test_up2(self):
        leaf = TMTree("leaf", [], 50)
        leaf.change_size(0.99)
        leaf.update_data_sizes()
        exp = 100
        act = leaf.data_size
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(act))

    def test_down(self):
        leaf = TMTree("leaf", [], 50)
        leaf.change_size(-0.1)
        leaf.update_data_sizes()
        exp = 45
        act = leaf.data_size
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(act))

    def test_down2(self):
        leaf = TMTree("leaf", [], 50)
        leaf.change_size(-0.99)
        leaf.update_data_sizes()
        exp = 1
        act = leaf.data_size
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(act))

    def test_change_folder(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 60)
        root = TMTree("root", [leaf, leaf2], 0)
        root.change_size(0.01)
        root.update_data_sizes()
        self.assertEqual(root.data_size, 110, "You cannot change the size of a folder")

    def test_change_folder2(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 60)
        root = TMTree("root", [leaf, leaf2], 0)
        leaf.change_size(0.1)
        root.update_data_sizes()
        exp = 55
        act = leaf.data_size
        self.assertEqual(act, 55, "Expected " + str(exp) + " Your result is " + str(act))
        self.assertEqual(root.data_size, 115, "When you change the size of a leaf you should also update its parent")

    def test_change_folder3(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 60)
        root = TMTree("root", [leaf, leaf2], 0)
        leaf.change_size(-0.1)
        root.update_data_sizes()
        exp = 45
        act = leaf.data_size
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(
                             act))
        self.assertEqual(root.data_size, 105,
                         "When you change the size of a leaf you should update its parent also")

    def test_change_folder4(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 60)
        root = TMTree("root", [leaf, leaf2], 0)
        leaf.change_size(-0.1)
        root.update_data_sizes()
        exp = 45
        act = leaf.data_size
        self.assertEqual(act, exp,
                         "Expected " + str(exp) + " Your result is " + str(
                             act))
        self.assertEqual(root.data_size, 105,
                         "When you change the size of a leaf you should update its parent also")

class a2_test_move(unittest.TestCase):
    def test_leaf(self):
        leaf = TMTree("leaf", [], 50)
        dest = TMTree("leaf", [], 60)
        leaf.move(dest)
        self.assertListEqual(leaf._subtrees, [], "You cannot move a leaf to a leaf")

    def test_leaf2(self):
        leaf = TMTree("leaf", [], 60)
        leaf2 = TMTree("leaf2", [], 60)
        dest = TMTree("dest", [leaf2], 0)
        root = TMTree("dest", [dest, leaf], 0)
        leaf.move(dest)
        root.update_data_sizes()
        assert len(dest._subtrees) == 2
        self.assertEqual(dest._subtrees[-1], leaf, "You should add leaf as the last element of dest's subtrees")
        self.assertEqual(leaf._parent_tree, dest, "You should connect leaf to the proper parent tree after you move it")
        self.assertEqual(dest.data_size, 120, "You should also update the data size of dest")

    def test_move_to_folder(self):
        leaf = TMTree("leaf", [], 60)
        folderA = TMTree("folderA", [leaf], 0)
        leaf2 = TMTree("leaf2", [], 60)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        folderA.move(folderB)
        root.update_data_sizes()
        self.assertEqual(folderA.data_size, 60, "Nothing should change")
        self.assertEqual(folderB.data_size, 60, "Nothing should change")
        self.assertEqual(len(folderA._subtrees), 1, "Nothing should change")
        self.assertEqual(len(folderB._subtrees), 1, "Nothing should change")

    def test_move_to_folder2(self):
        leaf = TMTree("leaf", [], 10)
        leaf2 = TMTree("leaf2", [], 20)
        leaf3 = TMTree("leaf3", [], 30)
        folderA = TMTree("folderA", [leaf, leaf2, leaf3], 0)
        leaf4 = TMTree("leaf3", [], 60)
        leaf5 = TMTree("leaf4", [], 60)
        folderB = TMTree("folderB", [leaf4, leaf5], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root.update_rectangles((0,0,100, 100))
        root._expanded = True
        folderA._expanded = True
        folderB._expanded = True
        leaf2.move(folderB)
        root.update_data_sizes()
        root.update_rectangles((0,0,100,100))

        assert len(folderA._subtrees) == 2 and len(folderB._subtrees) == 3
        self.assertEqual(leaf2._parent_tree, folderB, "You should move to the correct parent tree")
        self.assertEqual(folderA.data_size, 40, "You should update folderA's datasize")
        self.assertEqual(folderB.data_size, 140, "You should update folderB's datasize")
        self.assertEqual(folderA.rect, (0,0,100,22), "You should update the rect of folderA")
        self.assertEqual(folderB.rect, (0,22, 100, 78), "You should update the rect of folderB")

    def test_move_to_folder3(self):
        leaf = TMTree("leaf", [], 60)
        folderA = TMTree("folderA", [leaf], 0)
        leaf2 = TMTree("leaf2", [], 60)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        folderA._expanded = True
        folderB._expanded = True
        root._expanded = True
        root.update_rectangles((0,0,100,100))
        leaf.move(folderB)
        root.update_data_sizes()
        root.update_rectangles((0,0,100,100))
        
        assert len(folderB._subtrees) == 2
        self.assertEqual(folderB._subtrees[-1], leaf, "You should add leaf as the last element of folderB")
        self.assertEqual(leaf._parent_tree, folderB, "You should point to the correct parent")
        self.assertEqual(folderB.data_size, 120, "You should update the data size of folderB")
        self.assertEqual(folderA.data_size, 0, "You should update the data size of folderA")
        self.assertEqual(root.data_size, 120, "The root size remain same here since you did make so many change")
        self.assertEqual(folderA.rect, (0,0,100,0), "You should also update the rectangle of folderA")
        self.assertEqual(folderB.rect, (0,0,100,100), "You should also update the rectangle of folderB")





unittest.main(exit=False)

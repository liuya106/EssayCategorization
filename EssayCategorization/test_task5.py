import unittest
from tm_trees import *
from a2_test_task2 import is_leaf, set_expanded
def test_expanded(tree):
    if is_leaf(tree):
        return [tree._expanded == False]
    else:
        temp = []
        temp.append(tree._expanded)
        for sub in tree._subtrees:
            temp.extend(test_expanded(sub))
        return temp


def test_collapse(tree):
    if is_leaf(tree):
        return [tree._expanded == False]
    else:
        temp = []
        temp.append(not tree._expanded)
        for sub in tree._subtrees:
            temp.extend(test_collapse(sub))
        return temp


class a2_task5_test_expanded(unittest.TestCase):
    def test_leaf(self):
        leaf = TMTree("leaf", [], 50)
        leaf.update_rectangles((0,0,100,100))
        leaf.expand()
        self.assertCountEqual([rect[0] for rect in leaf.get_rectangles()], [(0,0,100,100)])
        self.assertEqual(leaf._expanded, False, "You cannot expanded a leaf(A single File)")

    def test_single_folder(self):
        leaf = TMTree("leaf", [], 50)
        folder = TMTree("folder", [leaf], 50)
        folder.expand()
        self.assertEqual(folder._expanded, True,
                         "You can only expanded a folder")

    def test_multiple_folder(self):
        leaf = TMTree("leaf", [], 40)
        folderA = TMTree("folderA", [leaf], 0)
        leaf2 = TMTree("leaf2", [], 40)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root.update_rectangles((0,0,100,100))
        root._expanded = True
        folderA.expand()
        self.assertCountEqual([rect[0]for rect in root.get_rectangles()], [(0,0,100,50), (0,50,100,50)])
        self.assertEqual(folderA._expanded, True, "You should change the expanded of folderA")
        self.assertEqual(root._expanded, True, "You should also change the parent of folderA to be True")
        self.assertEqual(folderB._expanded, False, "You should not change the sibling of folderA")

    def test_multiple_folder2(self):
        leaf = TMTree("leaf", [], 40)
        leaf3 = TMTree("leaf3", [], 20)
        folderC = TMTree("folderC", [leaf, leaf3], 0)
        folderA = TMTree("folderA", [folderC], 0)
        leaf2 = TMTree("leaf2", [], 40)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root.update_rectangles((0,0,100,100))
        root._expanded = True
        folderA._expanded = True
        folderC.expand()
        self.assertCountEqual([rect[0] for rect in root.get_rectangles()], [(0,0,66,60), (66,0,34,60), (0,60,100,40)])
        self.assertEqual(folderC._expanded, True, "You should change the expaned of folderC")
        self.assertEqual(folderB._expanded, False,
                         "You should not change the sibiling of folderA")

    def test_multiple_folder3(self):
        leaf = TMTree("leaf", [], 40)
        folderC = TMTree("folderC", [leaf], 0)
        folderA = TMTree("folderA", [folderC], 0)
        leaf2 = TMTree("leaf2", [], 40)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root._expanded = True
        root.update_rectangles((0,0,100,100))
        folderB.expand()
        root.get_rectangles()
        self.assertCountEqual([rect[0] for rect in root.get_rectangles()], [(0,0,100,50),(0,50,100,50)])
        self.assertEqual(folderB._expanded, True, "You should change the expanded of folderB")
        self.assertEqual(leaf2._expanded, False, "You should not modifided the child of folderB")
        self.assertEqual(folderA._expanded, False,
                         "You should not change the sibiling of folderB")
        self.assertEqual(root._expanded, True,
                         "You should also change the parent of folderB to be True")
        self.assertEqual(folderC._expanded, False,
                         "You should not change the expanded of fodlerC")

    def test_multiple_folder4(self):
        leaf = TMTree("leaf", [], 40)
        folderC = TMTree("folderC", [leaf], 0)
        folderA = TMTree("folderA", [folderC], 0)
        leaf2 = TMTree("leaf2", [], 40)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root._expanded = True
        folderA.expand()
        self.assertEqual(folderC._expanded, False, "You should not change the expaned of folderC")
        self.assertEqual(all(test_collapse(folderC)), True, "You should not change any leaf under folderA")
        self.assertEqual(folderA._expanded, True,
                         "You should change the expanded of folderC's parent")
        self.assertEqual(root._expanded, True,
                         "You should also change the parent of folderA to be True")
        self.assertEqual(folderB._expanded, False,
                         "You should not change the sibiling of folderA")

    def test_multiple_folder5(self):
        leaf = TMTree("leaf", [], 40)
        leaf3 = TMTree("leaf3", [], 20)
        folderC = TMTree("folderC", [leaf, leaf3], 0)
        folderA = TMTree("folderA", [folderC], 0)
        leaf2 = TMTree("leaf2", [], 40)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root._expanded = True
        root.update_rectangles((0,0,100,100))
        folderA.expand()
        self.assertCountEqual([rect[0] for rect in root.get_rectangles()], [(0,0,100,60), (0,60,100,40)])
        self.assertEqual(folderC._expanded, False, "You should not change the expaned of folderC")
        self.assertEqual(all(test_collapse(folderC)), True, "You should not modify node under folderA")
        self.assertEqual(folderA._expanded, True,
                         "You should change the expanded of folderC's parent")
        self.assertEqual(root._expanded, True,
                         "You should also change the parent of folderA to be True")
        self.assertEqual(folderB._expanded, False,
                         "You should not change the sibiling of folderA")


class a2_task5_test_expand_all(unittest.TestCase):
    def test_single_folder(self):
        leaf = TMTree("leaf", [], 50)
        folder = TMTree("folder", [leaf], 50)
        folder.expand_all()
        act = all(test_expanded(folder))
        folder.update_rectangles((0,0,100,100))
        rec = [rect[0] for rect in folder.get_rectangles()]
        self.assertCountEqual(rec, [(0,0,100,100)])
        self.assertEqual(act, True,
                         "You should change every internal node under folder")

    def test_internal_node(self):
        leaf = TMTree("leaf", [], 40)
        folderA = TMTree("folderA", [leaf], 0)
        leaf2 = TMTree("leaf2", [], 40)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root.update_rectangles((0,0,100,100))
        root._expanded = True
        folderA.expand_all()
        act = all(test_expanded(folderA))
        rec = [rect[0] for rect in root.get_rectangles()]
        self.assertCountEqual(rec, [(0,0,100,50),(0,50,100,50)])
        self.assertEqual(act, True, "You should change every internal under folderA")
        self.assertEqual(root._expanded, True, "You should change root's expaned to be True")
        self.assertEqual(folderB._expanded, False, "You should not modified folderB's expanded")

    def test_internal_node2(self):
        leaf = TMTree("leaf", [], 40)
        folderA = TMTree("folderA", [leaf], 0)
        leaf2 = TMTree("leaf2", [], 40)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root._expanded = True
        folderB.expand_all()
        act = all(test_expanded(folderB))
        self.assertEqual(act, True,
                         "You should change the expanded of folderB")
        self.assertEqual(folderA._expanded, False,
                         "You should not modified folderA")

    def test_internal_node3(self):
        leaf = TMTree("leaf", [], 40)
        leaf2 = TMTree("leaf2", [], 40)
        folderC = TMTree("folderC", [leaf, leaf2], 0)
        folderA = TMTree("folderA", [folderC], 0)
        leaf3 = TMTree("leaf3", [], 40)
        leaf4 = TMTree("leaf4", [], 40)
        folderB = TMTree("folderB", [leaf3, leaf4], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root.update_rectangles((0,0,100,100))
        root._expanded = True
        folderA.expand_all()
        rec = [rect[0] for rect in root.get_rectangles()]
        self.assertCountEqual(rec, [(0,0,50,50), (50,0,50,50), (0,50,100,50)])
        self.assertEqual(folderC._expanded, True, "You should change the expaned of folderC")
        self.assertEqual(folderA._expanded, True,
                         "You should change the expanded of folderC's parent")
        self.assertEqual(root._expanded, True,
                         "You should also change the parent of folderA to be True")
        self.assertEqual(folderB._expanded, False,
                         "You should not change the sibiling of folderA")

    def test_internal_node4(self):
        leaf = TMTree("leaf", [], 40)
        folderC = TMTree("folderC", [leaf], 0)
        folderA = TMTree("folderA", [folderC], 0)
        leaf2 = TMTree("leaf2", [], 40)
        leaf3 = TMTree("leaf3", [], 20)
        folderB = TMTree("folderB", [leaf2, leaf3], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root.update_rectangles((0,0,100,100))
        root._expanded = True
        folderA._expanded = True
        folderC.expand_all()
        rec = [rect[0] for rect in root.get_rectangles()]
        self.assertCountEqual(rec, [(0,0,100,40),(0,40,100,60)])
        self.assertEqual(folderC._expanded, True, "You should change the expaned of folderC")
        self.assertEqual(folderA._expanded, True,
                         "You should change the expanded of folderC's parent")
        self.assertEqual(folderB._expanded, False,
                         "You should not change the sibiling of folderA")

    def test_root(self):
        leaf = TMTree("leaf", [], 40)
        leaf2 = TMTree("leaf2", [], 40)
        folderA = TMTree("folderA", [leaf, leaf2], 0)
        leaf3 = TMTree("leaf3", [], 40)
        leaf4 = TMTree("leaf4", [], 40)
        folderB = TMTree("folderB", [leaf3, leaf4], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root.update_rectangles((0,0,100,100))
        root.expand_all()
        act = all(test_expanded(root))
        rec = [rect[0] for rect in root.get_rectangles()]
        self.assertEqual(act, True, "You should change every internal node under root to be True")
        self.assertCountEqual(rec, [(0,0,50,50), (50,0,50,50), (0,50,50,50), (50,50,50,50)])

class a2_task5_test_collapse(unittest.TestCase):
    def test_leaf(self):
        leaf = TMTree("leaf", [], 50)
        leaf.collapse()
        self.assertEqual(leaf._expanded, False, "You should not change the leaf")

    def test_single_folder(self):
        leaf = TMTree("leaf", [], 50)
        folderA = TMTree("folderA", [leaf], 50)
        root = TMTree("root", [folderA], 0)
        root._expanded = True
        folderA.collapse()
        self.assertEqual(folderA._expanded, False, "This has not effect on the folderA")
        self.assertEqual(root._expanded, False, "This has not effect on the root")

    def test_single_folder2(self):
        leaf = TMTree("leaf", [], 50)
        folderA = TMTree("folderA", [leaf], 50)
        root = TMTree("root", [folderA], 0)
        root._expanded = True
        root.collapse()
        self.assertEqual(folderA._expanded, False,
                         "This has not effect on the folderA")
        self.assertEqual(root._expanded, False,
                         "This has not effect on the root")

    def test_folder(self):
        leaf = TMTree("leaf", [], 40)
        folderA = TMTree("folderA", [leaf], 0)
        leaf2 = TMTree("leaf2", [], 40)
        folderB = TMTree("folderB", [leaf2], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root.update_rectangles((0,0,100,100))
        set_expanded(root)
        root.collapse()
        self.assertEqual(root._expanded, False, "You should set _expanded of every thing under root to False")
        rec = [rect[0] for rect in root.get_rectangles()]
        self.assertCountEqual(rec, [(0,0,100,100)])

    def test_multiple_folder(self):
        leaf = TMTree("leaf", [], 40)
        leaf2 = TMTree("leaf2", [], 40)
        folderA = TMTree("folderA", [leaf, leaf2], 0)
        leaf3 = TMTree("leaf3", [], 40)
        leaf4 = TMTree("leaf4", [], 40)
        folderB = TMTree("folderB", [leaf3, leaf4], 0)
        root = TMTree("root", [folderA, folderB], 0)
        root.update_rectangles((0, 0, 100, 100))
        set_expanded(root)
        folderA.collapse()
        rec = [rect[0] for rect in root.get_rectangles()]
        act = all(test_collapse(folderA))
        # self.assertCountEqual(rec, [(0,0,100,50), (0,50,50,50), (50,50,50,50)])
        self.assertEqual(rec, [(0,0,100,100)])
        self.assertEqual(root._expanded, False, "You should not modified root")
        self.assertEqual(act, True, "You should set expanded of every thing under folderA be False")




unittest.main(exit=False)

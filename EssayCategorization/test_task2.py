import unittest
import os
from tm_trees import TMTree, FileSystemTree

def repr_tree(tree:TMTree):
    parent_name = "None" if tree._parent_tree is None else tree._parent_tree._name
    if is_leaf(tree):
        return [(tree._name, tree.data_size, parent_name)]
    else:
        temp = []
        for sub in tree._subtrees:
            temp.extend(repr_tree(sub))
        temp += [(tree._name, tree.data_size, parent_name)]
        return temp


def is_leaf(tree):
    return not tree.is_empty() and tree._subtrees == []


def set_expanded(tree):
    if is_leaf(tree):
        tree._expanded = False
    else:
        tree._expanded = True
        for sub in tree._subtrees:
            set_expanded(sub)


def set_size(tree, size):
    if is_leaf(tree):
        tree.data_size = size
    else:
        for sub in tree._subtrees:
            set_size(sub, size)
        tree.data_size = sum([sub.data_size for sub in tree._subtrees])


class a2_test_task2(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join('example-directory', "workshop")
        self.FileTree = FileSystemTree(self.path)

    def test_single_leaf(self):
        leaf = TMTree("leaf", [], 30)
        rect = (0,0,100,100)
        leaf.update_rectangles(rect)
        self.assertCountEqual(leaf.rect, rect, "The leaf should have the exact rect as given")

    def test_one_level_tree(self):
        leaf = TMTree("leaf", [], 30)
        root = TMTree("root", [leaf], 40)
        rect = (0,0,100,100)
        root.update_rectangles(rect)
        self.assertCountEqual(leaf.rect, rect, "")
        self.assertCountEqual(root.rect, rect,  "Since the tree only contains a leaf so the root's rect should be same with leaf")

    def test_two_leaves(self):
        leaf = TMTree("leaf", [], 30)
        leaf2 = TMTree("leaf", [], 70)
        root = TMTree("root", [leaf, leaf2], 0)
        rect = (0, 0, 1000, 100)
        set_expanded(root)
        root.update_rectangles(rect)
        self.assertCountEqual(leaf.rect, (0,0,300,100), "You should calculate the correct proportion of the leaf")
        self.assertCountEqual(leaf2.rect, (300,0,700,100), "You should calculate the correct proportion of the leaf")
        self.assertCountEqual(root.rect, rect, "The root's rect should be exact same with the given argument")

    def test_two_leaves_round(self):
        leaf = TMTree("leaf", [], 30)
        leaf2 = TMTree("leaf", [], 69)
        root = TMTree("root", [leaf, leaf2], 0)
        rect = (0, 0, 200, 100)
        root.update_rectangles(rect)
        self.assertCountEqual(leaf.rect, (0, 0, 60, 100),
                              "Round down the proportion of the leaf")
        self.assertCountEqual(leaf2.rect, (60, 0, 140, 100),
                              "Round down the proportion of the leaf")
        self.assertCountEqual(root.rect, rect,
                              "The root's rect should be exact same with the given argument")

    def test_two_leaves_round2(self):
        leaf = TMTree("leaf", [], 29)
        leaf2 = TMTree("leaf", [], 70)
        root = TMTree("root", [leaf, leaf2], 0)
        rect = (0, 0, 100, 200)
        root.update_rectangles(rect)
        self.assertCountEqual(leaf.rect, (0, 0, 100, 58),
                              "You should calculate the correct proportion of the leaf")
        self.assertCountEqual(leaf2.rect, (0, 58, 100, 142),
                              "You should calculate the correct proportion of the leaf")
        self.assertCountEqual(root.rect, rect,
                              "The root's rect should be exact same with the given argument")

    def test_different_direction(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 30)
        leaf3 = TMTree("leaf3", [], 70)
        internal = TMTree("internal", [leaf2, leaf3], 0)
        root = TMTree("root", [internal, leaf], 0)
        rect = (0, 0, 210, 160)
        set_expanded(root)
        root.update_rectangles(rect)
        self.assertEqual(root.rect, rect, "Root's size should be same with the given argument")
        self.assertEqual(internal.rect, (0,0,140,160), "internal's width takes the 2/3 of the given argument")
        self.assertEqual(leaf.rect, (140, 0, 70, 160), "leaf's width should take 1/3 of the given argument")
        self.assertEqual(leaf2.rect, (0,0, 140, 48), "leaf 2 (The first leaf of internal)'s height should take 3/10 of INTERNAL'S HEIGHT")
        self.assertEqual(leaf3.rect, (0,48, 140, 112), "leaf3 (The second leaf of internal)'s height should take 7/10 of INTERNAL'S HEIGHT")

    def test_two_qual_height_tree(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 50)
        leaf3 = TMTree("leaf3", [], 50)
        leaf4 = TMTree("leaf4", [], 50)
        internal1 = TMTree("internal1", [leaf, leaf2], 0)
        internal2 = TMTree("internal2", [leaf3, leaf4], 0)
        root = TMTree("root", [internal1, internal2], 0)
        rect = (0,0,100,100)
        set_expanded(root)
        root.update_rectangles(rect)
        self.assertEqual(root.rect, rect, "Root's size should be same with the given argument")
        self.assertEqual(internal1.rect, (0, 0, 100, 50), "internal1's height should take half of the root")
        self.assertEqual(internal2.rect, (0, 50, 100, 50), "internal2's height should take half of the root")
        self.assertEqual(leaf.rect, (0, 0, 50, 50), "leaf(the first leaf of internal1)'s weight should take half of the internal1")
        self.assertEqual(leaf2.rect, (50, 0, 50, 50), "leaf2(the second leaf of internal1)'s weight should take second half of the internal1")
        self.assertEqual(leaf3.rect, (0, 50, 50, 50), "leaf3(the first leaf of internal2)'s weight shoudl take half of the internal2's weight")
        self.assertEqual(leaf4.rect, (50, 50, 50, 50), "leaf4(the second leaf of internal2)'s weight should take half of the internal2's weight")

    def test_complicate(self):
        leafI = TMTree("leaf", [], 20)
        leafJ = TMTree("leaf2", [], 15)
        folderD = TMTree("folderD", [leafI, leafJ], 50)
        leafE = TMTree("leaf3", [], 35)
        folderA = TMTree("folderA", [folderD, leafE], 0)
        leafK= TMTree("leafK", [], 40)
        leafL = TMTree("leafL", [], 10)
        folderF = TMTree("folderF", [leafK, leafL], 0)
        leafG = TMTree("leafG", [], 10)
        folderB = TMTree("folderB", [folderF, leafG], 0)
        leafO = TMTree("leafO", [], 20)
        leafP = TMTree("leafP", [], 20)
        folderM = TMTree("leafM", [leafO, leafP], 40)
        leafN =TMTree("leafN", [], 40)
        folderH = TMTree("folderH", [folderM, leafN], 0)
        folderC = TMTree("folderC", [folderH], 0)
        root = TMTree("root", [folderA, folderB, folderC], 0)
        set_expanded(root)
        rect = (0, 0, 210, 60)
        root.update_rectangles(rect)
        self.assertEqual(root.rect, rect, "Root's rectangle should be same with given argument")
        self.assertEqual(folderA.rect, (0,0,70, 60), "folderA(The first internal node of root)'s width should be 1/3 of the given argument")
        self.assertEqual(folderB.rect, (70, 0, 60, 60), "folderB(The second internal node of root)'s width should be 6/21 of the given argument")
        self.assertEqual(folderC.rect, (130, 0, 80, 60), "folderC(The third internal node of root)'s width should be 8/21 of the given argument")
        self.assertEqual(folderD.rect, (0, 0, 35, 60), "folderD(The first internal node of folderA)'s width should be 1/2 of folderA's width")
        self.assertEqual(leafE.rect, (35, 0, 35, 60), "leafE(The second element of folderA)'s width should take second half of folderA's width")
        self.assertEqual(leafI.rect, (0, 0, 35,34), "leafI(The first leaf of folderD)'s height should be 20/35 of the folderD's height")
        self.assertEqual(leafJ.rect, (0, 34, 35,26), "leafJ(The second leaf of folderD)'s height should be 15/35 of the folderD's height")
        self.assertEqual(folderF.rect, (70, 0, 60, 50), "folderF(The first child of folderB)'s height should be 5/6 of the folderB's height")
        self.assertEqual(leafG.rect, (70, 50, 60, 10), "leafG(The second child of folderB)'s height should be 1/6 of the folderB's hegiht")
        self.assertEqual(leafK.rect, (70, 0, 48, 50), "leafK(The first child of folderF)'s width should be 4/5 of the folderF's width")
        self.assertEqual(leafL.rect, (118,0, 12, 50 ), "leafL(The second child of folderF)'s width should be 1/5 of the folderF's width")
        self.assertEqual(folderH.rect, (130, 0, 80, 60), "folderH(The only child of folderC)'s rect should be same with folderC")
        self.assertEqual(folderM.rect, (130, 0, 40, 60), "folderM(The first child of folderH)'s width should be half of the folderH's width")
        self.assertEqual(leafN.rect, (170, 0, 40, 60), "leafN(The second child of folderH)'s width should be the second half of the folderH")
        self.assertEqual(leafO.rect, (130, 0, 40, 30), "leafO(The first child of folderM)'s height should be the half of the folderM's height")
        self.assertEqual(leafP.rect, (130, 30, 40, 30), "leafP(The second child of folderM)'s height should be the half of the folderM's height")

    def test_get_rectangle_task2(self):
        leaf = TMTree("leaf", [], 30)
        root = TMTree("root", [leaf], 40)
        rect = (0, 0, 100, 100)
        root.update_rectangles(rect)
        set_expanded(root)
        act = root.get_rectangles()
        assert len(act) == 1
        self.assertEqual(act[0][0], rect, "For task 2 you should return every leaf of the DATA tree")

    def test_get_rectangle_task5(self):
        leaf = TMTree("leaf", [], 30)
        root = TMTree("root", [leaf], 40)
        rect = (0, 0, 100, 100)
        root.update_rectangles(rect)
        act = root.get_rectangles()
        assert len(act) == 1
        self.assertEqual(act[0][0], rect, "For task 5 you should return every leaf of the DISPLAYED tree")

    def test_two_leaves_task2(self):
        leaf = TMTree("leaf", [], 30)
        leaf2 = TMTree("leaf", [], 70)
        root = TMTree("root", [leaf, leaf2], 0)
        rect = (0, 0, 1000, 100)
        set_expanded(root)
        root.update_rectangles(rect)
        temp = root.get_rectangles()
        assert len(temp) == 2
        exp = [(0,0,300,100), (300,0,700,100)]
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp, "For task 2 you should return every leaf of the data tree")

    def test_two_leaves_task5(self):
        leaf = TMTree("leaf", [], 30)
        leaf2 = TMTree("leaf", [], 70)
        root = TMTree("root", [leaf, leaf2], 0)
        rect = (0, 0, 1000, 100)
        root.update_rectangles(rect)
        temp = root.get_rectangles()
        assert len(temp) == 1
        exp = [rect]
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp, "For task 5 you should return every leaf of the displayed tree")

    def test_different_direction_task2(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 30)
        leaf3 = TMTree("leaf3", [], 70)
        internal = TMTree("internal", [leaf2, leaf3], 0)
        root = TMTree("root", [internal, leaf], 0)
        rect = (0, 0, 210, 160)
        exp = [(140, 0, 70, 160), (0,0, 140, 48),(0,48, 140, 112)]
        set_expanded(root)
        root.update_rectangles(rect)
        temp = root.get_rectangles()
        assert len(temp) == 3
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp, "For task2 you should return every leaf of the data tree")

    def test_different_direction_task5(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 30)
        leaf3 = TMTree("leaf3", [], 70)
        internal = TMTree("internal", [leaf2, leaf3], 0)
        root = TMTree("root", [internal, leaf], 0)
        rect = (0, 0, 210, 160)
        exp = [(0,0,140,160), (140,0, 70, 160)]
        root._expanded = True
        root.update_rectangles(rect)
        temp = root.get_rectangles()
        assert len(temp) == 2
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp, "For task5 you should return every leaf of the displayed tree")

    def test_two_qual_height_tree_task2(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 50)
        leaf3 = TMTree("leaf3", [], 50)
        leaf4 = TMTree("leaf4", [], 50)
        internal1 = TMTree("internal1", [leaf, leaf2], 0)
        internal2 = TMTree("internal2", [leaf3, leaf4], 0)
        root = TMTree("root", [internal1, internal2], 0)
        rect = (0,0,100,100)
        set_expanded(root)
        root.update_rectangles(rect)
        exp = [(0, 0, 50, 50), (50, 0, 50, 50), (0, 50, 50, 50), (50, 50, 50, 50)]
        temp = root.get_rectangles()
        assert len(temp) == 4
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp, "For task 2 you should return every leaf in the DATA tree")

    def test_two_qual_height_tree_task5(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 50)
        leaf3 = TMTree("leaf3", [], 50)
        leaf4 = TMTree("leaf4", [], 50)
        internal1 = TMTree("internal1", [leaf, leaf2], 0)
        internal2 = TMTree("internal2", [leaf3, leaf4], 0)
        root = TMTree("root", [internal1, internal2], 0)
        rect = (0,0,100,100)
        root._expanded = True
        root.update_rectangles(rect)
        exp = [(0, 0, 100, 50),  (0, 50, 100, 50)]
        temp = root.get_rectangles()
        assert len(temp) == 2
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp, "For task 5 you should only return leaf in the DISPLAY tree")

    def test_two_qual_height_tree_task5_2(self):
        leaf = TMTree("leaf", [], 50)
        leaf2 = TMTree("leaf2", [], 50)
        leaf3 = TMTree("leaf3", [], 50)
        leaf4 = TMTree("leaf4", [], 50)
        internal1 = TMTree("internal1", [leaf, leaf2], 0)
        internal2 = TMTree("internal2", [leaf3, leaf4], 0)
        root = TMTree("root", [internal1, internal2], 0)
        rect = (0,0,100,100)
        root._expanded = True
        internal2._expanded = True
        root.update_rectangles(rect)
        exp = [(0, 0, 100, 50),  (0, 50, 50, 50), (50, 50, 50, 50)]
        temp = root.get_rectangles()
        assert len(temp) == 3
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp, "For task 5 you should only return leaf in the DISPLAY tree")

    def test_complicate_task2(self):
        leafI = TMTree("leaf", [], 20)
        leafJ = TMTree("leaf2", [], 15)
        folderD = TMTree("folderD", [leafI, leafJ], 50)
        leafE = TMTree("leaf3", [], 35)
        folderA = TMTree("folderA", [folderD, leafE], 0)
        leafK= TMTree("leafK", [], 40)
        leafL = TMTree("leafL", [], 10)
        folderF = TMTree("folderF", [leafK, leafL], 0)
        leafG = TMTree("leafG", [], 10)
        folderB = TMTree("folderB", [folderF, leafG], 0)
        leafO = TMTree("leafO", [], 20)
        leafP = TMTree("leafP", [], 20)
        folderM = TMTree("leafM", [leafO, leafP], 40)
        leafN =TMTree("leafN", [], 40)
        folderH = TMTree("folderH", [folderM, leafN], 0)
        folderC = TMTree("folderC", [folderH], 0)
        root = TMTree("root", [folderA, folderB, folderC], 0)
        set_expanded(root)
        rect = (0, 0, 210, 60)
        set_expanded(root)
        root.update_rectangles(rect)
        exp = [(35, 0, 35, 60), (0, 0, 35,34), (0, 34, 35,26), (70, 50, 60, 10), (70, 0, 48, 50), (118,0, 12, 50 ), (170, 0, 40, 60), (130, 0, 40, 30), (130, 30, 40, 30) ]
        temp = root.get_rectangles()
        assert len(temp) == 9
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp,
                              "For task 2 you should return every leaf in the DATA tree")

    def test_complicate_task5(self):
        leafI = TMTree("leaf", [], 20)
        leafJ = TMTree("leaf2", [], 15)
        folderD = TMTree("folderD", [leafI, leafJ], 50)
        leafE = TMTree("leaf3", [], 35)
        folderA = TMTree("folderA", [folderD, leafE], 0)
        leafK = TMTree("leafK", [], 40)
        leafL = TMTree("leafL", [], 10)
        folderF = TMTree("folderF", [leafK, leafL], 0)
        leafG = TMTree("leafG", [], 10)
        folderB = TMTree("folderB", [folderF, leafG], 0)
        leafO = TMTree("leafO", [], 20)
        leafP = TMTree("leafP", [], 20)
        folderM = TMTree("leafM", [leafO, leafP], 40)
        leafN = TMTree("leafN", [], 40)
        folderH = TMTree("folderH", [folderM, leafN], 0)
        folderC = TMTree("folderC", [folderH], 0)
        root = TMTree("root", [folderA, folderB, folderC], 0)
        root._expanded = True
        rect = (0, 0, 210, 60)
        root.update_rectangles(rect)
        exp = [(0, 0, 70, 60), (70, 0, 60, 60), (130, 0, 80, 60)]
        temp = root.get_rectangles()
        assert len(temp) == 3
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp,
                              "For task 5 you should return every leaf in the DISPLAYED tree")

    def test_complicate_task5_2(self):
        leafI = TMTree("leaf", [], 20)
        leafJ = TMTree("leaf2", [], 15)
        folderD = TMTree("folderD", [leafI, leafJ], 50)
        leafE = TMTree("leaf3", [], 35)
        folderA = TMTree("folderA", [folderD, leafE], 0)
        leafK = TMTree("leafK", [], 40)
        leafL = TMTree("leafL", [], 10)
        folderF = TMTree("folderF", [leafK, leafL], 0)
        leafG = TMTree("leafG", [], 10)
        folderB = TMTree("folderB", [folderF, leafG], 0)
        leafO = TMTree("leafO", [], 20)
        leafP = TMTree("leafP", [], 20)
        folderM = TMTree("leafM", [leafO, leafP], 40)
        leafN = TMTree("leafN", [], 40)
        folderH = TMTree("folderH", [folderM, leafN], 0)
        folderC = TMTree("folderC", [folderH], 0)
        root = TMTree("root", [folderA, folderB, folderC], 0)
        root._expanded = True
        folderC._expanded = True
        rect = (0, 0, 210, 60)
        root.update_rectangles(rect)
        exp = [(0, 0, 70, 60), (70, 0, 60, 60), (130, 0, 80, 60)]
        temp = root.get_rectangles()
        assert len(temp) == 3
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp,
                              "For task 5 you should return every leaf in the DISPLAYED tree")

    def test_complicate_task5_3(self):
        leafI = TMTree("leaf", [], 20)
        leafJ = TMTree("leaf2", [], 15)
        folderD = TMTree("folderD", [leafI, leafJ], 50)
        leafE = TMTree("leaf3", [], 35)
        folderA = TMTree("folderA", [folderD, leafE], 0)
        leafK = TMTree("leafK", [], 40)
        leafL = TMTree("leafL", [], 10)
        folderF = TMTree("folderF", [leafK, leafL], 0)
        leafG = TMTree("leafG", [], 10)
        folderB = TMTree("folderB", [folderF, leafG], 0)
        leafO = TMTree("leafO", [], 20)
        leafP = TMTree("leafP", [], 20)
        folderM = TMTree("leafM", [leafO, leafP], 40)
        leafN = TMTree("leafN", [], 40)
        folderH = TMTree("folderH", [folderM, leafN], 0)
        folderC = TMTree("folderC", [folderH], 0)
        root = TMTree("root", [folderA, folderB, folderC], 0)
        root._expanded = True
        folderA._expanded = True
        folderB._expanded = True
        folderC._expanded = True
        rect = (0, 0, 210, 60)
        root.update_rectangles(rect)
        exp = [(0, 0, 35, 60), (35, 0, 35, 60), (70, 0, 60, 50), (70, 50, 60, 10), (130, 0, 80, 60)]
        temp = root.get_rectangles()
        assert len(temp) == 5
        act = [sub[0] for sub in temp]
        self.assertCountEqual(act, exp,
                              "For task 5 you should return every leaf in the DISPLAYED tree")


unittest.main(exit=False)


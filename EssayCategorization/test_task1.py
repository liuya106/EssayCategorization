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


class a2_test_part1_and_part2(unittest.TestCase):
    def setUp(self):
        self.path= os.path.join('example-directory', "workshop")
        self.FileTree = FileSystemTree(self.path)

    def test_init(self):
        act = repr_tree(self.FileTree)
        act.sort(key=lambda x:x[1])
        exp = [('Plan.tex', 2, 'activities'), ('reading.md', 6, 'prep'), ('Cats.pdf', 16, 'images'), ('images', 16, 'prep'), ('Q2.pdf', 20, 'images'), ('prep', 22, 'workshop'), ('Q3.pdf', 49, 'images'), ('draft.pptx', 58, 'workshop'), ('images', 69, 'activities'), ('activities', 71, 'workshop'), ('workshop', 151, "None")]
        self.assertListEqual(act, exp)

    def test_tmtree_setup_no_subtree(self):
        t = TMTree('Easy4.0', [], 50)
        self.assertIsInstance(t.data_size, int,
                              'data_size is not instantiated correctly')
        self.assertIsInstance(t._colour, tuple,
                              '_colour is not instantiated correctly')
        self.assertEqual(t.data_size, 50, 'leaf data size is wrong')

    def test_tmtree_setup_with_subtrees(self):
        subtree1 = TMTree('subtree1', [], 10)
        subtree2 = TMTree('subtree2', [], 20)
        t = TMTree('Easy4.0', [subtree1, subtree2], 100)
        self.assertEqual(t.data_size, 30, 'non-leaf data size is wrong')
        self.assertEqual(subtree1._parent_tree, t, 'parent should be set')
        self.assertEqual(subtree2._parent_tree, t, 'parent should be set')

    def test_tmtree_setup_recursive_data_size(self):
        subtree1 = TMTree('subtree1', [TMTree('subtree11', [], 1000)], 10)
        subtree2 = TMTree('subtree2', [TMTree('subtree21', [], 2000)], 20)
        t = TMTree('Easy4.0', [subtree1, subtree2], 666)
        self.assertEqual(t.data_size, 3000, 'non-leaf data size is wrong')


unittest.main(exit=False)

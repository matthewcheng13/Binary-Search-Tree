from Binary_Search_Tree import Binary_Search_Tree
import unittest

class Binary_Search_Tree_Test(unittest.TestCase):

    def setUp(self):
        self.__tree = Binary_Search_Tree()

    def test_empty_tree_string(self):
        self.assertEqual('[ ]',str(self.__tree))
        self.assertEqual(0,self.__tree.get_height())
    
    # get height/set height

    def test_get_one_element_height(self):
        self.__tree.insert_element(5)
        self.assertEqual(1,self.__tree.get_height())

    def test_get_one_element_height_string(self):
        self.__tree.insert_element('tree')
        self.assertEqual(1,self.__tree.get_height())

    def test_get_two_elements_left_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.assertEqual(2,self.__tree.get_height())

    def test_get_two_elements_right_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.assertEqual(2,self.__tree.get_height())

    def test_get_three_elements_full_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(6)
        self.assertEqual(2,self.__tree.get_height())

    def test_get_three_elements_left_left_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.assertEqual(3,self.__tree.get_height())

    def test_get_three_elements_left_right_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.assertEqual(3,self.__tree.get_height())

    def test_get_three_elements_right_left_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(6)
        self.assertEqual(3,self.__tree.get_height())

    def test_get_three_elements_right_right_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.assertEqual(3,self.__tree.get_height())

    def test_get_seven_elements_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(6)
        self.__tree.insert_element(8)
        self.assertEqual(3,self.__tree.get_height())

    def test_get_height_zero_after_removal(self):
        self.__tree.insert_element(5)
        self.__tree.remove_element(5)
        self.assertEqual(0,self.__tree.get_height())

    def test_get_height_one_after_removal_one_child(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.remove_element(5)
        self.assertEqual(1,self.__tree.get_height())

    def test_get_height_one_after_removal_no_children(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.remove_element(6)
        self.assertEqual(1,self.__tree.get_height())

    def test_get_height_two_after_removal_two_children(self):
        self.__tree.insert_element(6)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.remove_element(6)
        self.assertEqual(2,self.__tree.get_height())

    # insert

    def test_insert_empty_tree(self):
        self.__tree.insert_element(5)
        self.assertEqual('[ 5 ]',str(self.__tree))

    def test_insert_empty_tree_string(self):
        self.__tree.insert_element('Root')
        self.assertEqual('[ Root ]',str(self.__tree))

    def test_insert_single_element_tree_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.assertEqual('[ 4, 5 ]',str(self.__tree))  

    def test_insert_single_element_tree_left_string(self):
        self.__tree.insert_element('Root')
        self.__tree.insert_element('Leaf')
        self.assertEqual('[ Leaf, Root ]',str(self.__tree))

    def test_insert_single_element_tree_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.assertEqual('[ 5, 6 ]',str(self.__tree)) 

    def test_insert_single_element_tree_right_string(self):
        self.__tree.insert_element('Branch')
        self.__tree.insert_element('Leaf')
        self.assertEqual('[ Branch, Leaf ]',str(self.__tree)) 

    def test_insert_two_element_tree_left_full(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(4)
        self.assertEqual('[ 4, 5, 6 ]',str(self.__tree))   

    def test_insert_two_element_tree_right_full(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(6)
        self.assertEqual('[ 4, 5, 6 ]',str(self.__tree)) 

    def test_insert_two_element_tree_left_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.assertEqual('[ 3, 4, 5 ]',str(self.__tree))
    
    def test_insert_two_element_tree_left_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.assertEqual('[ 3, 4, 5 ]',str(self.__tree))

    def test_insert_two_element_tree_right_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(6)
        self.assertEqual('[ 5, 6, 7 ]',str(self.__tree))

    def test_insert_two_element_tree_right_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.assertEqual('[ 5, 6, 7 ]',str(self.__tree))

    def test_insert_three_perfect_tree_left_lower(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(2)
        self.assertEqual('[ 2, 3, 5, 7 ]',str(self.__tree))

    def test_insert_three_perfect_tree_left_higher(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(4)
        self.assertEqual('[ 3, 4, 5, 7 ]',str(self.__tree))

    def test_insert_three_perfect_tree_right_lower(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(6)
        self.assertEqual('[ 3, 5, 6, 7 ]',str(self.__tree))

    def test_insert_three_perfect_tree_right_higher(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.assertEqual('[ 3, 5, 7, 8 ]',str(self.__tree))

    def test_insert_duplicate_root_fail(self):
        self.__tree.insert_element(5)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(5)
        self.assertEqual('[ 5 ]', str(self.__tree))
        self.assertEqual(1,self.__tree.get_height())

    def test_insert_duplicate_root_fail_string(self):
        self.__tree.insert_element('Tree')
        with self.assertRaises(ValueError):
            self.__tree.insert_element('Tree')
        self.assertEqual('[ Tree ]', str(self.__tree))
        self.assertEqual(1,self.__tree.get_height())

    def test_insert_duplicate_deeper_node_fail(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(4)
        self.assertEqual('[ 3, 4, 5 ]',str(self.__tree))
        self.assertEqual(3,self.__tree.get_height())

    def test_insert_duplicate_deeper_leaf_fail(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(3)
        self.assertEqual('[ 3, 4, 5 ]',str(self.__tree))
        self.assertEqual(3,self.__tree.get_height())

    # remove
    def test_remove_leaf_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.remove_element(4)
        self.assertEqual('[ 5 ]',str(self.__tree))

    def test_remove_leaf_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.remove_element(4)
        self.assertEqual('[ 5 ]',str(self.__tree))

    def test_remove_full_node_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.remove_element(3)
        self.assertEqual('[ 2, 4, 5 ]',str(self.__tree))

    def test_remove_single_child_node_left_twice(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.remove_element(3)
        self.assertEqual('[ 2, 5 ]',str(self.__tree))

    def test_remove_single_child_node_left_then_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.remove_element(3)
        self.assertEqual('[ 4, 5 ]',str(self.__tree))

    def test_remove_leaf_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.remove_element(6)
        self.assertEqual('[ 5 ]',str(self.__tree))

    def test_remove_full_node_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(6)
        self.__tree.insert_element(8)
        self.__tree.remove_element(7)
        self.assertEqual('[ 5, 6, 8 ]',str(self.__tree))
    
    def test_remove_single_child_node_right_twice(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(8)
        self.__tree.remove_element(7)
        self.assertEqual('[ 5, 8 ]',str(self.__tree))

    def test_remove_single_child_node_right_then_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(6)
        self.__tree.remove_element(7)
        self.assertEqual('[ 5, 6 ]',str(self.__tree))

    def test_remove_lone_root(self):
        self.__tree.insert_element(5)
        self.__tree.remove_element(5)
        self.assertEqual('[ ]',str(self.__tree))

    def test_remove_lone_root_string(self):
        self.__tree.insert_element('Tree')
        self.__tree.remove_element('Tree')
        self.assertEqual('[ ]',str(self.__tree))

    def test_remove_root_with_subtrees(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(9)
        self.__tree.insert_element(7)
        self.__tree.insert_element(11)
        self.__tree.insert_element(6)
        self.__tree.insert_element(8)
        self.__tree.insert_element(10)
        self.__tree.insert_element(12)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.remove_element(5)
        self.assertEqual('[ 2, 3, 4, 6, 7, 8, 9, 10, 11, 12 ]',str(self.__tree))

    def test_remove_value_error_empty(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(5)
        self.assertEqual('[ ]',str(self.__tree))
        self.assertEqual(0,self.__tree.get_height())

    def test_remove_value_error_empty(self):
        self.__tree.insert_element(5)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(4)
        self.assertEqual('[ 5 ]',str(self.__tree))
        self.assertEqual(1,self.__tree.get_height())

    # in order
    def test_inorder_no_elements(self):
        self.assertEqual('[ ]',self.__tree.in_order())

    def test_inorder_one_elements(self):
        self.__tree.insert_element(5)
        self.assertEqual('[ 5 ]',self.__tree.in_order())

    def test_inorder_two_elements_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.assertEqual('[ 4, 5 ]',self.__tree.in_order())

    def test_inorder_two_elements_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.assertEqual('[ 5, 6 ]',self.__tree.in_order())

    def test_inorder_three_elements_full(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(6)
        self.assertEqual('[ 4, 5, 6 ]',self.__tree.in_order())

    def test_inorder_three_elements_full_string(self):
        self.__tree.insert_element('Root')
        self.__tree.insert_element('Leaf')
        self.__tree.insert_element('Tree')
        self.assertEqual('[ Leaf, Root, Tree ]',self.__tree.in_order())

    def test_inorder_three_elements_left_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.assertEqual('[ 3, 4, 5 ]',self.__tree.in_order())

    def test_inorder_three_elements_left_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.assertEqual('[ 3, 4, 5 ]',self.__tree.in_order())

    def test_inorder_three_elements_right_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(6)
        self.assertEqual('[ 5, 6, 7 ]',self.__tree.in_order())

    def test_inorder_three_elements_right_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.assertEqual('[ 5, 6, 7 ]',self.__tree.in_order())

    # preorder
    def test_preorder_no_elements(self):
        self.assertEqual('[ ]',self.__tree.pre_order())

    def test_preorder_one_elements(self):
        self.__tree.insert_element(5)
        self.assertEqual('[ 5 ]',self.__tree.pre_order())

    def test_preorder_two_elements_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.assertEqual('[ 5, 4 ]',self.__tree.pre_order())

    def test_preorder_two_elements_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.assertEqual('[ 5, 6 ]',self.__tree.pre_order())

    def test_preorder_three_elements_full(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(6)
        self.assertEqual('[ 5, 4, 6 ]',self.__tree.pre_order())

    def test_preorder_three_elements_full_string(self):
        self.__tree.insert_element('Root')
        self.__tree.insert_element('Leaf')
        self.__tree.insert_element('Tree')
        self.assertEqual('[ Root, Leaf, Tree ]',self.__tree.pre_order())

    def test_preorder_three_elements_left_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.assertEqual('[ 5, 4, 3 ]',self.__tree.pre_order())

    def test_preorder_three_elements_left_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.assertEqual('[ 5, 3, 4 ]',self.__tree.pre_order())

    def test_preorder_three_elements_right_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(6)
        self.assertEqual('[ 5, 7, 6 ]',self.__tree.pre_order())

    def test_preorder_three_elements_right_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.assertEqual('[ 5, 6, 7 ]',self.__tree.pre_order())

    # postorder
    def test_postorder_no_elements(self):
        self.assertEqual('[ ]',self.__tree.post_order())

    def test_postorder_one_elements(self):
        self.__tree.insert_element(5)
        self.assertEqual('[ 5 ]',self.__tree.post_order())

    def test_postorder_two_elements_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.assertEqual('[ 4, 5 ]',self.__tree.post_order())

    def test_postorder_two_elements_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.assertEqual('[ 6, 5 ]',self.__tree.post_order())

    def test_postorder_three_elements_full(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(6)
        self.assertEqual('[ 4, 6, 5 ]',self.__tree.post_order())

    def test_postorder_three_elements_full_string(self):
        self.__tree.insert_element('Root')
        self.__tree.insert_element('Leaf')
        self.__tree.insert_element('Tree')
        self.assertEqual('[ Leaf, Tree, Root ]',self.__tree.post_order())

    def test_postorder_three_elements_left_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.assertEqual('[ 3, 4, 5 ]',self.__tree.post_order())

    def test_postorder_three_elements_left_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.assertEqual('[ 4, 3, 5 ]',self.__tree.post_order())

    def test_postorder_three_elements_right_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(6)
        self.assertEqual('[ 6, 7, 5 ]',self.__tree.post_order())

    def test_postorder_three_elements_right_right(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(7)
        self.assertEqual('[ 7, 6, 5 ]',self.__tree.post_order())

if __name__ == "__main__":
    unittest.main()
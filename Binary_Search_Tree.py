class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      # TODO complete Node initialization
      self.height = 1
      self.left_child = None
      self.right_child = None

  def __init__(self):
    self.__root = None
    # TODO complete initialization

  def __set_height(self,node):
    # case of no children always has a height of 1
    if (node.left_child == None) and (node.right_child == None):
      return 1
    # if there is no left child, right's height + 1 must be used
    elif node.left_child == None:
      return node.right_child.height + 1
    # if there is no right child, left's height + 1 must be used
    elif node.right_child == None:
      return node.left_child.height + 1
    # either left child is taller or right child's height is greater than or equal to left child's height
    else:
      if node.left_child.height > node.right_child.height:
        return node.left_child.height + 1
      else:
        return node.right_child.height + 1

  # I was considering using this instead of the current __set_height method, but I decided not to
  # as I was not sure what impact it would have on performance so feedback on this would be helpful
  # despite it not being in my actual implementation
  # def __set_height(self,node):
  #   try:
  #     left = node.left_child.height
  #   except AttributeError:
  #     left = 0
  #   try:
  #     right = node.right_child.height
  #   except AttributeError:
  #     right = 0
  #   if left > right:
  #     return left + 1
  #   else:
  #     return right + 1

  def __rins(self,value,node):
    # base case
    if node == None:
      new_node = Binary_Search_Tree.__BST_Node(value)
      return new_node
    # recursive case
    else:
      if node.value == value:
        raise ValueError
      elif node.value > value:
        node.left_child = self.__rins(value,node.left_child)
        node.height = self.__set_height(node)
      else:
        node.right_child = self.__rins(value,node.right_child)
        node.height = self.__set_height(node)
      return node

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    self.__root = self.__rins(value,self.__root)

  def __rrem(self,value,node):
    # if the node does not exist in the tree
    if node == None:
      raise ValueError
    # base case
    if node.value == value:
      if node.left_child == None:
        return node.right_child
      elif node.right_child == None:
        return node.left_child
      else:
        cur = node.right_child
        while cur.left_child != None:
          cur = cur.left_child
        node.value = cur.value
        node.right_child = self.__rrem(cur.value,node.right_child)
        return node
    # recursive cases
    elif node.value > value:
      node.left_child = self.__rrem(value,node.left_child)
      node.height = self.__set_height(node)
    else:
      node.right_child = self.__rrem(value,node.right_child)
      node.height = self.__set_height(node)
    return node

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    self.__root = self.__rrem(value,self.__root)

  def __rin_order(self,node):
    # performs string concatenation for each node
    # conditionals check if one or both children are missing and
    # returns the values that are present, with the parent's value
    # being in between left and right
    if (node.left_child == None) and (node.right_child == None):
      return str(node.value)
    elif node.left_child == None:
      right = self.__rin_order(node.right_child)
      return str(node.value) + ', ' + right
    elif node.right_child == None:
      left = self.__rin_order(node.left_child)
      return left + ', ' + str(node.value)
    else:
      left = self.__rin_order(node.left_child)
      right = self.__rin_order(node.right_child)
      return left + ', ' + str(node.value) + ', ' + right

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    # left node right
    if self.get_height() == 0:
      return '[ ]'
    else:
      return '[ ' + self.__rin_order(self.__root) + ' ]'

  def __rpre_order(self,node):
    # performs string concatenation for each node
    # conditionals check if one or both children are missing and
    # returns the values that are present, with the parent's value first
    if (node.left_child == None) and (node.right_child == None):
      return str(node.value)
    elif node.left_child == None:
      right = self.__rpre_order(node.right_child)
      return str(node.value) + ', ' + right
    elif node.right_child == None:
      left = self.__rpre_order(node.left_child)
      return str(node.value) + ', ' + left
    else:
      left = self.__rpre_order(node.left_child)
      right = self.__rpre_order(node.right_child)
      return str(node.value) + ', ' + left + ', ' + right

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    # node left right
    if self.get_height() == 0:
      return '[ ]'
    else:
      return '[ ' + self.__rpre_order(self.__root) + ' ]'

  def __rpost_order(self,node):
    # performs string concatenation for each node
    # conditionals check if one or both children are missing and
    # returns the values that are present, with the parent's value last
    if (node.left_child == None) and (node.right_child == None):
      return str(node.value)
    elif node.left_child == None:
      right = self.__rpost_order(node.right_child)
      return right + ', ' + str(node.value)
    elif node.right_child == None:
      left = self.__rpost_order(node.left_child)
      return left + ', ' + str(node.value)
    else:
      left = self.__rpost_order(node.left_child)
      right = self.__rpost_order(node.right_child)
      return left + ', ' + right + ', ' + str(node.value)

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    # left right node
    if self.get_height() == 0:
      return '[ ]'
    else:
      return '[ ' + self.__rpost_order(self.__root) + ' ]'

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation
    if self.__root == None:
      height = 0
    else:
      height = self.__root.height
    return height

  # Similar to before, I was considering using this instead of my current get_height method
  # def get_height(self):
  #   # return an integer that represents the height of the tree.
  #   # assume that an empty tree has height 0 and a tree with one
  #   # node has height 1. This method must operate in constant time.
  #   # TODO replace pass with your implementation
  #   try:
  #     height = self.__root.height
  #   except AttributeError:
  #     height = 1
  #   return height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  t = Binary_Search_Tree()
  t.insert_element(6)
  t.insert_element(5)
  t.insert_element(7)
  t.insert_element(9)
  t.insert_element(8)
  print(str(t))


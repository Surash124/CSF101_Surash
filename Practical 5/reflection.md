## Reflection — Binary Search Tree (BST)

### Discuss What I Learned:
- Learned how a **binary search tree** stores data in sorted hierarchical form.  
- Understood how **recursion** simplifies insertion, deletion, and search logic.  
- Practiced using **inorder traversal** to display sorted data from the BST.  
- Gained better understanding of **tree structures and relationships** between nodes.  
- Learned how to handle **edge cases** during deletion (node with one or two children).  

### Challenges Faced and How I Overcame Them:
- **Challenge:** Deletion logic was confusing for nodes with two children.  
  **Solution:** Used a helper function `_min_value_node()` to find the inorder successor.  
- **Challenge:** Mistakes in recursive calls caused infinite loops initially.  
  **Solution:** Carefully returned updated subtree references in each recursive function.  
- **Challenge:** Visualizing tree structure in console output.  
  **Solution:** Verified results through inorder traversal and printed intermediate steps.  

### Screenshot:
![BST Reflection](../Images/bst.png)

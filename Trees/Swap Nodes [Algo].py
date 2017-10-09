
class BinaryTree:
	def __init__(self, index):
		self.left = None
		self.right = None
		self.index = index

	def insert_left(self, child):
		if self.left is None:
			self.left = child
	def insert_right(self, child):
		if self.right is None:
			self.right = child
	def swap_subtrees(self):
		tmp = self.left
		self.left = self.right	
		self.right = tmp


def get_tree():
	num_nodes = int(input())
	nodes = []
	root = BinaryTree(1)
	nodes.append(root)
	# BFS construction
	for i in range(1, num_nodes+1):
		left, right = [int(e) for e in input().split()]
		left_tree = None
		right_tree = None
		if left != -1:
			left_tree = BinaryTree(left)
			nodes[0].insert_left(left_tree)
			nodes.append(left_tree)

		if right != -1:
			right_tree = BinaryTree(right)
			nodes[0].insert_right(right_tree)
			nodes.append(right_tree)

		nodes.pop(0)
	return root


def swap(tree, cur_level, K):
	# Do recursive DFS and swap subtrees if on a Kth level
	# if tree is None:
	# 	return None
	# if cur_level % K == 0:
	# 	tree.swap_subtrees()
	# swap(tree.left, cur_level+1, K)
	# swap(tree.right, cur_level+1, K)

	# Do an iterative BFS for swapping to avoid exceeding recursion stack size
	nodes = [[tree, 1]]
	cur = nodes[0][0]
	cur_level = 1
	while len(nodes) > 0 and cur != None:
		cur, cur_level = nodes.pop(0)
		# swap the subtrees of all the nodes who are at depth K
		if cur_level % K == 0:
			cur.swap_subtrees()
		if cur.left is not None:
		    nodes.append([cur.left, cur_level + 1])
		if cur.right is not None:
		    nodes.append([cur.right, cur_level + 1])

	return tree

def do_swaps(tree):
	T = int(input())
	for k in range(T):
		# Swap subtrees at every Kth level
		K = int(input())
		new_tree = swap(tree, 1, K)
		display_iterative(new_tree)

def display_iterative(tree):
	# DFS traversal using stack (to avoid recursion)
	nodes = []
	cur = tree
	done = False
	while not done:
		if cur is not None:
			nodes.append(cur)
			cur = cur.left
		else:
			if nodes:
				cur = nodes.pop()
				print("%d " % cur.index, end="")
				cur = cur.right 
			else:
				done = True
	print("")

tree = get_tree()
do_swaps(tree)
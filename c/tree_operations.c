/* Binary Search Tree operations */

#include <stdio.h>
#include <malloc.h>

typedef struct tree * bst;

struct tree {
	int data;
	bst parent;
	bst left;
	bst right;
};


bst insert(bst tree, int data)
{
	if(tree == NULL)
	{
		tree = (bst)malloc(sizeof(struct tree));
		tree->data = data;
		tree->left = tree->right = NULL;
	}
	else if(data <= tree->data)
	{
		tree->left = insert(tree->left, data);
	}
	else if(data > tree->data)
	{
		tree->right = insert(tree->right, data);
	}

	return tree;
}

bst search(bst tree, int item)
{
	if(tree == NULL)
		printf("Empty tree\n");
	else if(item == tree->data)
		printf("Item found\n");
	else if(item <= tree->data)
		tree->left = search(tree->left, item);
	else// if(item > tree->data)
		tree->right = search(tree->right, item);
	
	return tree;
}

void preorder(bst tree)
{
	if(tree == NULL)
		return;
	/* First print the root  */
	printf("%d ", tree->data);
	
	/* Then traverse to the left subtree recursively  */
	preorder(tree->left);
	
	/* Finally traverse to the right subtree */
	preorder(tree->right);
}

void inorder(bst tree)
{
	if(tree == NULL)
		return;
	inorder(tree->left);
	printf("%d ", tree->data);
	inorder(tree->right);
}

void postorder(bst tree)
{
	if(tree == NULL)
		return;
	postorder(tree->left);
	postorder(tree->right);
	printf("%d ", tree->data);
}


int main()
{
	bst tree = NULL;
	int ch=0, item, choice=1;
	while(choice == 1)
	{
		printf("1.\tInsert\n2.\tSearch\n3.\tPreorder\n4.\tInorder\n5.\tPostorder\n\n: ");
		scanf("%d", &ch);
		switch(ch){
			case 1:printf("\nEnter item to be inserted: ");
			       scanf("%d", &item);
			       tree = insert(tree, item);
			       break;

			case 2:printf("\nEnter the element to be entered: ");
			       scanf("%d", &item);
			       tree = search(tree, item);
			       break;

			case 3:preorder(tree);

			case 4:inorder(tree);
			       
			case 5:postorder(tree);

			default:printf("\nWrong choice");
		}
		printf("\nContinue (1/0): ");
		scanf("%d", &choice);
	}
	free(tree);
	return 1;
}

	

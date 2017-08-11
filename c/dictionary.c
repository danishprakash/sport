/* Suppose that we are designing a program to simulate the storage and search in a dictionary. Words appear with different frequ
 * encies, 
 * however, and it may be the case that a frequently us
 * ed word such as "the" appears far from the root while a rarely used word such as 
 * "conscientiousness" appears near the root. We want words that occur frequently in the text to be placed nearer to the root. M
 * oreover, there may 
 * be words in the dictionary for 
 * which there is no definition. Write a program to organize an optimal binary search tree that simulates the storage 
 * and search of words in a dictionary.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node * snp;

struct node{
	char *word;
	char *meaning;
	int freq;
	snp left;
	snp right;
};

snp newNode(char *word, char *meaning, int freq)
{
	snp node = (snp)malloc(sizeof(struct node));
	node->word = malloc(256);
	node->meaning = malloc(256);
	strcpy(node->word, word);
	strcpy(node->meaning, meaning);
	node->freq = freq;
	return node;
}

void insert(snp root, snp newnode)
{
	if(strcmp(root->word, newnode->word)  == 0)
	{
		root->freq += 1;
		return;
	}
	else if(root->freq >= newnode->freq)
	{
		if(root->left == NULL)
		{	
			root->left = newnode;
			root->left->freq += 1;
		}
		else
		{
			insert(root->left, newnode);
		}
	}
	else if(root->freq < newnode->freq)
	{
		if(root->right == NULL)
		{
			root->right = newnode;
			root->right->freq += 1;
		}
		else
			insert(root->right, newnode);
	}
}

void lookup(snp root, char *word)
{
	if(strcmp(root->word, word) == 0)
	{
		printf("\nFound element, freq: %d", root->freq);
		return;
	}
	else if(root == NULL)
		return;
	else if(root->left != NULL)
		lookup(root->left, word);
	else if (root->right != NULL)
		lookup(root->right, word);
}


int main()
{
	snp root, node;
	root = NULL;
	int ch=-1;
	char *word = malloc(256);
	char *meaning = malloc(256);
	while(ch != 0)
	{
		printf("\n1. Insert\n2. Lookup\n");
		scanf("%d", &ch);
		switch(ch){
			case 1: 
				printf("Enter word\t");
				scanf("%s", word);
				printf("\nEnter meaning\t");
				scanf("%s", meaning);
				if(root == NULL)
				{
					node = newNode(word, meaning, 0);
					root = node;
					root->freq += 1;
				}
				else
				{
					node = newNode(word, meaning, 0);
					insert(root, node);
				}
				break;
			case 0:
				break;
			case 2:
				printf("\nEnter word to be searched\t");
				scanf("%s", word);
				lookup(root, word);
				break;
			default: 
				printf("\nEnter a valid choice");
				break;
		}
	}
					
	return 1;
}


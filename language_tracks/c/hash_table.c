/* Hash Table implementation in C */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int element_count = 0;
struct hash *hash_table = NULL;

struct node {
	int key, age;
	char name[100];
	struct node *next;
};

struct hash {
	struct node *head;
	int count;
};

struct node * createNode(int key, char *name, int age)
{
	struct node *newnode;
	newnode = (struct node*)malloc(sizeof(struct node));
	newnode->age = age;
	newnode->key = key;
	strcpy(newnode->name, name);
	newnode->next = NULL;
	return newnode;
}

void insert(int key, char *name, int age)
{
	int hash_value = key % element_count;
	struct node *newnode = createNode(key, name, age);
	//printf("%d %d %d\n", key, element_count, hash_value);

	if(!hash_table[hash_value].head)
	{
		hash_table[hash_value].head = newnode;
		hash_table[hash_value].count = 1;
		return;
	}

	newnode->next = hash_table[hash_value].head;
	hash_table[hash_value].head = newnode;
	hash_table[hash_value].count += 1;
	return;
}

void search(int key)
{
	int hash_value = key % element_count, flag = 0;
	struct node * node = hash_table[hash_value].head;

	if(!node)
	{
		printf("Search element not available in hash table\n");
		return;
	}

	while(node != NULL) {
		if(node->key == key)
		{
			printf("Element found %s\n", node->name);
			flag = 1;
			break;
		}
		node = node->next;
	}
	if (!flag)
		printf("Element not found\n");
	return;
}

void delete(int key)
{
	int hash_value = key % element_count, flag = 0;

	struct node *temp, *node;
	node = hash_table[hash_value].head;

	if(!node)
	{
		printf("Element not present in the hash table\n");
		return;
	}
	temp = node;
	while(node != NULL) {
		if(node->key == key)
		{
			flag = 1;
			if(hash_table[hash_value].head == node)
				hash_table[hash_value].head = node->next;
			else
				temp->next = node->next;
			hash_table[hash_value].count--;
			free(node);
			break;
		}
		temp = node;
		node = node->next;
	}

	if(!flag)
		printf("Element not present in the hash table\n");
	else
		printf("Element deleted\n");
	return;
}

void display()
{
	struct node *node;
	int i;
	for(i = 0; i < element_count; i++)
	{
		if(hash_table[i].count == 0)
			continue;
		node = hash_table[i].head;
		if(!node)
			continue;
		printf("Elements at index %d of hash table\n", i+1);
		while(node != NULL) {
			printf("%-12d", node->key);
			printf("%-15s", node->name);
			printf("%d\n", node->age);
			node = node->next;
		}
	}
	return;
}



int main()
{
	int n, ch, key, age;
	char name[100];
	printf("Enter no. of elements\n");
	scanf("%d", &n);
	element_count = n;
	hash_table = (struct hash *)calloc(n, sizeof(struct hash));

	while(1) {
		printf("1. Insert\n2. Search\n3. Delete\n4. Display table\n5. Exit\n\n");
		scanf("%d", &ch);
		switch(ch) {
			case 1: printf("Enter key value\n");
				scanf("%d", &key);
				printf("Name\n");
				scanf("%s", name);
//				name[strlen(name)-1] = '\0';
				printf("Age\n");
				scanf("%d", &age);
				insert(key, name, age);
				break;

			case 2: printf("Enter key of element to be searched\n");
				scanf("%d", &key);
				search(key);
				break;

			case 3: printf("Enter key of element to be deleted\n");
				scanf("%d", &key);
				delete(key);
				break;
				
			case 4: display();
				break;

			case 5: exit(0);

			default: printf("Wrong choice\n");

		}
	}
	return 0;
}

		

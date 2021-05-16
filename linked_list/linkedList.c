#include <stdio.h>
#include <stdlib.h>
typedef struct Node Node;
struct Node {
	int data;
	Node* next;
};

void printNode(Node* n) {
	while(n != NULL) {
		printf(" % d \n ", n->data);
		n = n->next;
	}
}

Node* searchItem(Node* item, int x) {
	if (item == NULL) return (NULL);

	if (item->data == x)
	       	return (item); 
	else
		return (searchItem(item->next, x));
}

void addItem(Node** item, int x) {
	Node* p;

	p = malloc(sizeof(Node));
	p->data = x;
	p->next = *item;
	*item = p;
}	

Node* predecessor_node(Node* list, int x) {
	if ((list == NULL) || (list->next == NULL)) {
	       printf("Error: predecessor is NULL.\n");
       	       return (NULL);
	}
	if ((list->next)->data == x) 
		return (list);
	else 
		return (predecessor_node(list->next, x));
}

void delete_item(Node** list, int x) {
	Node* p;
	Node* pred;
	Node* searchItem(), *predecessor_node();

	p = searchItem(*list, x);
	if(p!=NULL) {
		pred = predecessor_node(*list, x);
		if (pred==NULL)
			*list = p->next;
		else 
			pred->next = p->next;
		free(p);
	}
} 



int main() {
	 Node* head = NULL;
	 Node* second = NULL;
	 Node* third = NULL;

	head = (struct Node*)malloc(sizeof(struct Node));
	second = (struct Node*)malloc(sizeof(struct Node));
	third = (struct Node*)malloc(sizeof(struct Node));

	head->data = 1;
	head->next = second;
	second->data = 2;
	second->next = third;
	third->data = 3;
	third->next = NULL;
	
	printNode(head);

	Node** temp = &head;
	
	addItem(temp, 5);	
	printNode(head);

	delete_item(temp, 2);
	printNode(head);
}

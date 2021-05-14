#include <stdio.h>
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
}

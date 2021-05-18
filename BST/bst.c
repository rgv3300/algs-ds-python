#include<stdio.h>
#include<stdlib.h>
typedef struct tree tree;

struct tree {
	int data;
	tree* left;
	tree* right;
	tree* parent;
};



int main() {
	tree* a;
	a = (tree*)malloc(sizeof(tree));
	a->data = 2;
	a->left = (tree*)malloc(sizeof(tree));
	a->left->data = 1;
	a->left->right = NULL;
	a->left->left = NULL;
	a->right = (tree*)malloc(sizeof(tree));
	a->right->data = 3;
	a->right->right = NULL;
	a->right->left = NULL;
	
	printf("   %i\n",a->data);
	printf("%i        %i\n",a->left->data,a->right->data);
}

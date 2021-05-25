#include<stdio.h>
#include<string.h>
#define SIZE 10000
#include<stdlib.h>
unsigned long hash_func(char* str) {
	unsigned long i = 0;
	for (int j = 0; str[j]; j++)
		i += str[j];
	return i % 10000;
}

typedef struct hash_table hash_table;
typedef struct hash_item hash_item;
typedef struct linked_list linked_list;

struct linked_list {
	hash_item* item;
	linked_list* next;
};

struct hash_item {
	char* key;
	char* value;
};

struct hash_table {
	hash_item** item;
	linked_list** overflow_buckets;
	int size;
	int count;
};

hash_item* create_hash_item(char* key, char* value) {
	hash_item* item = (hash_item*)malloc(sizeof(hash_item));
	item->key = (char*)malloc(sizeof(key) + 1);
	item->value = (char*)malloc(sizeof(value) + 1);

	strcpy(item->key, key);
	strcpy(item->value, value);
	
	return item;
}

linked_list** create_overflow_bucket(hash_table* table) {
	linked_list** bucket = (linked_list**)calloc(table->size,sizeof(linked_list*)); //create overflow linked list for every hashtable slot
	for(int i = 0; i < table->size; i++)  
		bucket[i] = NULL;
	return bucket;
}

hash_table* create_hash_table(int size) {
	hash_table* table = (hash_table*)malloc(sizeof(hash_table));
	table->size = size;
	table->count= 0;
	table->item = (hash_item**)calloc(table->size, sizeof(hash_item*));
	for(int i = 0; i < table->size; i++) 
		table->item[i] = NULL;
		table->overflow_buckets = create_overflow_bucket(table);	//comeback to check if overflow bucket is made for every item 10000 times
	return table;
}

void free_item(hash_item* item) {
	free(item->key);
	free(item->value);
	free(item);
}

void free_list(linked_list* list) {
	linked_list* temp = list;
	while(list) {
		temp = list;
		list = list->next;
		free(temp->item->key);
		free(temp->item->value);
		free(temp->item);
		free(temp);
	}
}

void free_overflow_bucket(hash_table* table) {
	linked_list** bucket = table->overflow_buckets;
	for(int i = 0; i<table->size; i++)
		free_list(bucket[i]);
	free(bucket);
}

void free_table(hash_table* table) {
	for (int i = 0; i < table->size; i++) {
		hash_item* item = table->item[i];
		if (item!=NULL)
			free_item(item);
	}
	free_overflow_bucket(table);
	free(table->item);
	free(table);
}

linked_list* list_allocate() {
	linked_list* list = (linked_list*)malloc(sizeof(linked_list));
	return list;
}

linked_list* list_insert(linked_list* list, hash_item* item) {
	if(!list) {
		linked_list* head = list_allocate();
		head->item = item;
		head->next = NULL;
		list = head;
		return list;
	}
	else if (list->next == NULL) {
		linked_list* node = list_allocate();
		node->item = item;
		node->next = NULL;
		list->next = node;
		return list;
	}
	linked_list* temp = list;
	while(temp->next->next) {
		temp = temp->next;
	}
	linked_list* node = list_allocate();
	node->item= item;
	node->next = NULL;
	temp->next = node;

	return list;
}

void collision_handler(hash_table* table, unsigned long index, hash_item* item) {
	linked_list* head = table->overflow_buckets[index];

	if(head==NULL) {
		head = list_allocate();
		head->item = item;
		table->overflow_buckets[index] = head;
		return;
	}
	else {
		table->overflow_buckets[index] = list_insert(head, item);
		return;
	}
}

void hash_insert(hash_table* table, char* key, char* value) {
	hash_item* item = create_hash_item(key, value);
	
	int index = hash_func(key);

	hash_item* curr_item = table->item[index];

	if (curr_item == NULL) {
		if (table->count == table->size) {
			printf("Error: Hash table is full\n");
			free_item(item);
			return;
		}
		
		table->item[index] = item;
		table->count++;
	}
	else {
		if (strcmp(curr_item->key, key) == 0) {
			strcpy(table->item[index]->value, value);
		}
		else {
			collision_handler(table,index,item);
			return;
		}
	}
}

char* hash_search(hash_table* table, char* key) {
	int index = hash_func(key);
	
	hash_item* item = table->item[index];
	
	linked_list* head = table->overflow_buckets[index];

	if (item != NULL) {
		if (strcmp(item->key, key) == 0)
			return item->value;
		if(head == NULL)
			return NULL;
		item = head->item;
		head = head->next;
	}

	return NULL;
}

void print_search(hash_table* table, char* key) {
	char* val;
	if((val = hash_search(table, key)) == NULL) {
		printf("Key:%s does not exist\n", key);
		return;
	}
	else {
		printf("Key:%s, Value:%s\n",key,val);
	}
}

void print_table(hash_table* table) {
	printf("\nHash table\n--------------------\n");
	for(int i =0; i < table->size; i++) {
		if(table->item[i]) {
			printf("index:%d, key:%s, value:%s\n",i,table->item[i]->key, table->item[i]->value);
		}
	}
	printf("----------------------\n\n");
}

hash_item* remove_list(linked_list* list) {
	if(!list)
		return NULL;
	if(!list->next)
		return NULL;
	linked_list* node = list->next;
	linked_list* temp = list;
	temp->next = NULL;
	list = node;
	hash_item* it = NULL;
	memcpy(temp->item,it,sizeof(hash_item));
	free(temp->item->key);
	free(temp->item->value);
	free(temp->item);
	free(temp);
	return it;
}

void hash_delete(hash_table* table, char* key) {
	int index = hash_func(key);
	hash_item* item = table->item[index];
	linked_list* head = table->overflow_buckets[index];

	if(item == NULL) {
		return;
	}
	else {
		if (head == NULL && strcmp(item->key, key) == 0) {
			table->item[index] = NULL;
			free_item(item);
			table->count--;
			return;
		}
		else if (head != NULL) {
			if(strcmp(item->key,key) == 0) {

				free_item(item);
				linked_list* node = head;
				head = head->next;
				node->next = NULL;
				table->item[index] = create_hash_item(node->item->key, node->item->value);
				free_list(node);
				table->overflow_buckets[index] = head;
				return;
			}

			linked_list* curr = head;
			linked_list* prev = NULL;

			while(curr) {
				if(strcmp(curr->item->key, key) == 0) {
					if(prev == NULL) {

						free_list(head);
						table->overflow_buckets[index] = NULL;
						return;
					}
					else {
						prev->next = curr->next;
						curr->next = NULL;
						free_list(curr);
						table->overflow_buckets[index] = head;
						return;
					}
				}
				curr = curr->next;
				prev = curr;
			}
		}
	}
}

int main() {
	hash_table* ht = create_hash_table(SIZE);
	
	hash_insert(ht, "1", "first address");
	hash_insert(ht, "2", "second address");

	print_search(ht, "1");
	print_search(ht,"2");
	print_search(ht, "3");
	print_table(ht);
	free_table(ht);
	return 0;
}


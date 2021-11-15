#include <stdio.h>
#include <stdlib.h>

struct ListNode {
	int val;
	struct ListNode *next;
}; 

struct ListNode* generate_list(int arr[], int size) {
	struct ListNode *head = (struct ListNode*)malloc(sizeof(struct ListNode));
	head->val = arr[0];
	
	struct ListNode *node, *prev; 
	node = head->next;
	prev = head;
	
	for (int i = 1; i < size; i++) {
		node = (struct ListNode*)malloc(sizeof(struct ListNode));
		node->val = arr[i];
		prev->next = node;
		prev = node;
		node = node->next;
	}

	return head;
}

void print_list(struct ListNode *head) {
	if (head == NULL) {
		printf("Empty\n");
		return;
	}

	struct ListNode *node = head;
	printf("%d -> ", node->val);
	node = head->next;
	while(node != NULL) {
		printf("%d -> ", node->val);
		node = node->next;
	}

	printf("NULL\n");
}

int main() {
	int arr[] = {1, 2, 3, 4, 5};
	struct ListNode *head = generate_list(arr, 5);

	print_list(head);
	return 0;
}
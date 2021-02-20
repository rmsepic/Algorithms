// For practicing and understanding threading in c
#include <stdio.h>
#include <pthread.h>

void foo(void *t) {
	printf("Thread ID: %d\n", (int)t);
}

int main() {
	pthread_t id1, id2;
	pthread_create(&id1, NULL, (void*)foo, &id1);
	pthread_create(&id2, NULL, (void*)foo, &id2);
	printf("Thread %d\n", (int)id1);
}
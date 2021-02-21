// For practicing and understanding threading in c
#include <stdio.h>
#include <pthread.h>

void foo(void *t) {
	printf("Thread ID: %u\n", (unsigned)t);
	printf("pthread self: %u\n", (unsigned)pthread_self());
}

int main() {
	pthread_t id1, id2;
	pthread_create(&id1, NULL, (void*)foo, &id1);
	printf("Thread1 %u\n", (unsigned)id1);
	pthread_create(&id2, NULL, (void*)foo, &id2);
	printf("Thread2 %d\n", (int)id2);
	
}
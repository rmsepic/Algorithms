#include <stdio.h>
#include <pthread.h>
#include <dispatch/dispatch.h>
#include <dispatch/object.h>
#include <dispatch/time.h>

#define N 3

dispatch_semaphore_t sem;
dispatch_semaphore_t sem2;
dispatch_semaphore_t sem3;


void foo() {
	printf("foo\n");
	dispatch_semaphore_wait(sem, DISPATCH_TIME_FOREVER);
	printf("foo 2\n");
}

void bar() {
	printf("bar\n");
	dispatch_semaphore_wait(sem2, DISPATCH_TIME_FOREVER);
	printf("bar 2\n");
}

void fooBar() {
	dispatch_semaphore_signal(sem3);
	printf("fooBar\n");
	dispatch_semaphore_wait(sem3, DISPATCH_TIME_FOREVER);
	printf("fooBar 2\n");
}

int main() {
	pthread_t id, t_id2, t_id3;
	sem = dispatch_semaphore_create(0);
	sem2 = dispatch_semaphore_create(1);
	sem3 = dispatch_semaphore_create(0);

	pthread_create(&id, NULL, (void*)foo, NULL);
	pthread_create(&t_id2, NULL, (void*)bar, NULL);
	pthread_create(&t_id3, NULL, (void*)fooBar, NULL);
	pthread_join(id, NULL);
}
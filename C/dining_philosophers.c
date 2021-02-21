/*
 * Using the arbitrator solution
 */

#include <stdio.h>
#include <pthread.h>
#include <dispatch/dispatch.h>
#include <dispatch/object.h>
#include <dispatch/time.h>
#include <stdbool.h>

#define N 5 // Number of philosophers
#define LEFT (*num - 1) % N
#define RIGHT (*num + 1) % N

bool eating[N] = {false, false, false, false, false};
const char *phil[N] = {"Plato", "Kant", "Sartre", "Kierkegaard", "Descartes"};

dispatch_semaphore_t mutex;
dispatch_semaphore_t sems[N];

void take_left_fork(int* num) {
	printf("%s took a left fork\n", phil[*num]);
}

void take_right_fork(int* num) {
	printf("%s took a right fork\n", phil[*num]);
}

void eat(int* num) {
	printf("%s is eating\n", phil[*num]);
}

void put_left_fork(int* num) {
	printf("%s is done with left fork\n", phil[*num]);
}

void put_right_fork(int *num) {
	printf("%s is done with right fork\n", phil[*num]);
}

void philosopher(int* num) {
	while(1) {
		dispatch_semaphore_wait(mutex, DISPATCH_TIME_FOREVER);
		printf("Thread %u: %s is hungry. Num = %d\n", (unsigned)pthread_self(), phil[*num], *num);
		
		if (eating[LEFT] == false && eating[RIGHT] == false) {
			take_right_fork(num);
			take_left_fork(num);
			eating[*num] = true;
			eat(num);
			dispatch_semaphore_signal(sems[*num]);
		}

		dispatch_semaphore_signal(mutex);
		dispatch_semaphore_wait(sems[*num], DISPATCH_TIME_FOREVER);

		dispatch_semaphore_wait(mutex, DISPATCH_TIME_FOREVER);
		put_right_fork(num);
		put_left_fork(num);
		eating[*num] = false;
		dispatch_semaphore_signal(mutex);
		dispatch_semaphore_wait(sems[*num], DISPATCH_TIME_FOREVER);
	}
}

int main() {
	int phil_nums[N];

	for (int i = 0; i < N; i++) {
		phil_nums[i] = i;
	}

	pthread_t id[N];

	mutex = dispatch_semaphore_create(1);
	for (int i = 0; i < N; i++) {
		sems[i] = dispatch_semaphore_create(0);
	}

	for (int i = 0; i < N; i++) {
		pthread_create(&id[i], NULL, (void*)philosopher, (void*)&phil_nums[i]);
		printf("Thread %u: %s is dining\n", (unsigned)id[i], phil[i]);
	}

	for (int i = 0; i < N; i++) {
		pthread_join(id[i], NULL);
	}
}
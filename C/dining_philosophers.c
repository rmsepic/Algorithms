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
		// mutex serves as the "waiter" or arbitrator. Prevents two philosphers from picking up 
		// or putting down forks at the same time
		// Does not halt the program for the first dining philosopher because the sem 
		// was initalized to 1
		dispatch_semaphore_wait(mutex, DISPATCH_TIME_FOREVER);
		printf("Thread %u: %s is hungry\n", (unsigned)pthread_self(), phil[*num]);
		
		// Try to eat
		if (eating[LEFT] == false && eating[RIGHT] == false) {
			take_right_fork(num);
			take_left_fork(num);
			eating[*num] = true;
			eat(num);
			dispatch_semaphore_signal(sems[*num]);
		}

		// If the philosopher cannot eat, then they free up the waiter to deal with someone else
		dispatch_semaphore_signal(mutex);

		// If the philosopher ate then they will pass through this because the semaphore will be 1
		dispatch_semaphore_wait(sems[*num], DISPATCH_TIME_FOREVER);

		// This portion of the function involves the putting down
		// The waiter only deals with philosophers one at a time when they are handling the utencils
		dispatch_semaphore_wait(mutex, DISPATCH_TIME_FOREVER);
		
		put_right_fork(num);
		put_left_fork(num);
		eating[*num] = false;

		// Free up the waiter
		dispatch_semaphore_signal(mutex);
	}
}

int main() {
	// Initialize array, assigned numbers to each philosopher
	// Prevents overwriting memory
	int phil_nums[N];
	for (int i = 0; i < N; i++) {
		phil_nums[i] = i;
	}

	pthread_t id[N];

	// Set this semaphore to 1
	// When the first philosopher calls wait the thread does not wait for him
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
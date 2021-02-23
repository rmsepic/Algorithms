// Resource hierarchy solution
// Original one by Dijkstra

#include <assert.h>
#include <dispatch/dispatch.h>
#include <dispatch/object.h>
#include <dispatch/time.h>
#include <pthread.h>
#include <stdbool.h>
#include <stdio.h>

#define N 5
#define LEFT (*num + 4) % N
#define RIGHT *num //(*num + 1) % N

//struct Forks {
//	int resource;
//	bool in_use;
//}

// This is to make sure that the threads are not modifying the same resource 
// at the same time
//struct Forks forks[N];

//				0		1		2		3		4
bool forks[N] = {false, false, false, false, false};
char fork_name[N] = {		 'A',    'B',       'C', 		   'D', 		  'E'};
const char *phil[N] = {"Plato", "Kant", "Sartre", "Kierkegaard", "Descartes"};
dispatch_semaphore_t sems[N];


void take_left_fork(int* num) {
	if (forks[LEFT] == true){
		dispatch_semaphore_wait(sems[*num], DISPATCH_TIME_FOREVER);
	} 

	assert(forks[LEFT] == false);
	forks[LEFT] = true;
	printf("%s took left fork %c (%d)\n", phil[*num], fork_name[LEFT], LEFT);
}

void take_right_fork(int* num) {
	if (forks[RIGHT] == true){
		dispatch_semaphore_wait(sems[*num], DISPATCH_TIME_FOREVER);
	} 

	assert(forks[RIGHT] == false);
	forks[RIGHT] = true;
	printf("%s took right fork %c (%d)\n", phil[*num], fork_name[RIGHT], RIGHT);
}

void eating() {
	while(1) {
	}
}

void put_left_fork(int* num) {
	printf("%s is done with left fork\n", phil[*num]);
}

void put_right_fork(int *num) {
	printf("%s is done with right fork\n", phil[*num]);
}

void philosopher(int *num) {
	while(1) {
		if (LEFT > *num) {
			take_right_fork(num);
			take_left_fork(num);
		} else {
			take_left_fork(num);
			take_right_fork(num);
		}
	}
}

int main() {
	// Initialize array, assigned numbers to each philosopher
	// Prevents overwriting memory
	int phil_num[N];
	for (int i = 0; i < N; i++) {
		phil_num[i] = i;
	}

	// Initalize semaphores
	for (int i = 0; i < N; i++) {
		sems[i] = dispatch_semaphore_create(0);
	}
	pthread_t id[N];

	for (int i = 0; i < N; i++) {
		pthread_create(&id[i], NULL, (void*) philosopher, (void*)&phil_num[i]);
	}

	for (int i = 0; i < N; i++) {
		pthread_join(id[i], NULL);
	}
}
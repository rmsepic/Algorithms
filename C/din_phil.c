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
#define RIGHT *num // 'Right' for the fork, which is the same as the phil's number
#define RIGHT_PHIL (*num + 1) % N // This is the philosopher sitting to the right

//				0		1		2		3		4
bool forks[N] = {false, false, false, false, false};
char fork_name[N] = {		  'A',    'B',       'C', 		   'D', 		  'E'};
const char *phil[N] = {"Plato", "Kant", "Sartre", "Kierkegaard", "Descartes"};
dispatch_semaphore_t sems[N];
dispatch_semaphore_t fork_sems[N];

void take_left_fork(int* num) {
	dispatch_semaphore_wait(fork_sems[LEFT], DISPATCH_TIME_FOREVER);
	while (forks[LEFT] == true){
		dispatch_semaphore_wait(sems[*num], DISPATCH_TIME_FOREVER);
	} 

	assert(forks[LEFT] == false);
	forks[LEFT] = true;
}

void take_right_fork(int* num) {
	dispatch_semaphore_wait(fork_sems[RIGHT], DISPATCH_TIME_FOREVER);
	while (forks[RIGHT] == true){
		dispatch_semaphore_wait(sems[*num], DISPATCH_TIME_FOREVER);
	} 

	assert(forks[RIGHT] == false);
	forks[RIGHT] = true;
}

void eating(int* num) {	
	printf("%s is eating\n", phil[*num]);
}

void put_left_fork(int* num) {
	forks[LEFT] = false;
	dispatch_semaphore_signal(fork_sems[LEFT]);
}

void put_right_fork(int *num) {
	forks[RIGHT] = false;
	dispatch_semaphore_signal(fork_sems[RIGHT]);
}

void unlock_sems(int* num, int side) {
	// If this is 0 then that means that it is already waiting
	if (dispatch_semaphore_wait(sems[side], DISPATCH_TIME_NOW) != 0) {
		dispatch_semaphore_signal(sems[side]);
	} 
}

void philosopher(int *num) {
	while(1) {
		// This first if statement is for Plato
		// Since he is the first philosopher 
		// he has to take the 'last' fork number 4
		if (LEFT > *num) {
			take_right_fork(num);
			take_left_fork(num);
		} else {
			take_left_fork(num);
			take_right_fork(num);
		}

		// After the philosopher has obtained both forks they can eat
		eating(num);
		put_right_fork(num);
		put_left_fork(num);
		unlock_sems(num, LEFT);
		unlock_sems(num, RIGHT_PHIL);
	}
}

int main() {
	// Initialize array, assigned numbers to each philosopher
	// Prevents overwriting memory
	int phil_num[N];
	for (int i = 0; i < N; i++) {
		phil_num[i] = i;
	}

	for (int i = 0; i < N; i++) {
		sems[i] = dispatch_semaphore_create(0);
		fork_sems[i] = dispatch_semaphore_create(1);
	}
	pthread_t id[N];

	for (int i = 0; i < N; i++) {
		pthread_create(&id[i], NULL, (void*) philosopher, (void*)&phil_num[i]);
	}

	for (int i = 0; i < N; i++) {
		pthread_join(id[i], NULL);
	}
}
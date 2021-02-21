#include <stdio.h>
#include <pthread.h>
#include <dispatch/dispatch.h>
//#include <dispatch/sempahore.h>
#include <dispatch/object.h>
#include <stdbool.h>

#define N 5 // Number of philosophers

bool eating[N] = {false, false, false, false, false};
char *phil[N] = {"Plato", "Kant", "Sartre", "Kierkegaard", "Descartes"};

dispatch_semaphore_t mutex;
dispatch_semaphore_t sems[N];

void take_left_fork() {

}

void take_right_fork() {

}

void eat() {

}

void put_left_fork() {

}

void put_right_fork() {

}

void philosopher(int* num) {
	while(1) {
		//dispatch_semaphore_wait(&sem);

	}
}

int main() {
	pthread_t id[N];

	mutex = dispatch_semaphore_create(1);
	for (int i = 0; i < N; i++) {
		sems[i] = dispatch_semaphore_create(0);
	}

	for (int i = 0; i < N; i++) {
		pthread_create(&id[0], NULL, (void*)philosopher, &i);
	}
}
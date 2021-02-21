#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdbool.h>

#define N 5 // Number of philosophers

bool eating = {false, false, false, false, false};
char *phil = {"Plato", "Konfuzius", "Socrates", "Voltaire", "Descartes"};

sem_t sem;
sem_t sems[N];

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
		sem_wait(&sem);

	}
}

int main() {
	pthread_t id[N];

	sem_init(&sem, 0, 1);
	for (int i = 0; i < N; i++) {
		sem_init(&s[i], 0, 0);
	}

	for (int i = 0; i < N; i++) {
		pthread_create(&id[0], NULL, (void*)philosopher, &i);
	}
}
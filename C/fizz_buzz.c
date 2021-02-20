#include <stdio.h> 
#include <stdlib.h> 
#include <pthread.h> 

void printNumber(int x) {
	printf("%d, ", x);
}

void printFizz() {
	printf("fizz, ");
}

void printBuzz() {
	printf("buzz, ");
}

void printFizzBuzz() {
	printf("fizzbuzz, ");
}

typedef struct {
    int n;
    int curr;
    pthread_mutex_t lock;
    pthread_cond_t cond;
} FizzBuzz;

FizzBuzz* fizzBuzzCreate(int n) {
    FizzBuzz* obj = (FizzBuzz*) malloc(sizeof(FizzBuzz));
    obj->n = n;
    obj->curr = 1;
    pthread_mutex_init(&obj->lock, NULL);   
    pthread_cond_init(&obj->cond, NULL);

    return obj;
}

// printFizz() outputs "fizz".
void fizz(FizzBuzz* obj) {
	while(1) {
		pthread_mutex_lock(&obj->lock);
		//printf("In fizz");

		if (obj->n < obj->curr) {
			pthread_mutex_unlock(&obj->lock);
			return;
		}
		//printf("curr %d\n", obj->curr);
		if (obj->curr % 3 == 0 && obj->curr % 5 != 0) {
			printFizz();
			obj->curr++;
			pthread_cond_broadcast(&obj->cond);
		} else {
			pthread_cond_wait(&obj->cond, &obj->lock);
		}

		pthread_mutex_unlock(&obj->lock);
	}
}

// printBuzz() outputs "buzz".
void buzz(FizzBuzz* obj) {
	while(1) {
		pthread_mutex_lock(&obj->lock);

		if (obj->n < obj->curr) {
			pthread_mutex_unlock(&obj->lock);
			return;
		}

		//printf("In buzz %d\n", obj->curr);
		if (obj->curr % 3 != 0 && obj->curr % 5 == 0){
			printBuzz();
			obj->curr++;
			pthread_cond_broadcast(&obj->cond);
		} else {
			pthread_cond_wait(&obj->cond, &obj->lock);
		}

		pthread_mutex_unlock(&obj->lock);	
	}
}

// printFizzBuzz() outputs "fizzbuzz".
void fizzbuzz(FizzBuzz* obj) {
    while(1) {
		pthread_mutex_lock(&obj->lock);

		if (obj->n < obj->curr) {
			pthread_mutex_unlock(&obj->lock);
			return;
		}

		//printf("In fizzbuzz %d\n", obj->curr);
		if (obj->curr % 3 == 0 && obj->curr % 5 == 0){
			printFizzBuzz();
			obj->curr++;
			pthread_cond_broadcast(&obj->cond);
		} else {
			pthread_cond_wait(&obj->cond, &obj->lock);
		}

		pthread_mutex_unlock(&obj->lock);
	}
}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.
void number(FizzBuzz* obj) {
	while(1) {
		pthread_mutex_lock(&obj->lock);

		if (obj->n < obj->curr) {
			pthread_mutex_unlock(&obj->lock);
			return;
		}

		//printf("In number %d\n", obj->curr);
		if (obj->curr % 3 != 0 && obj->curr % 5 != 0){
			printNumber(obj->curr);
			obj->curr++;
			pthread_cond_broadcast(&obj->cond);
		} else {
			pthread_cond_wait(&obj->cond, &obj->lock);
		}

		pthread_mutex_unlock(&obj->lock);
	}
}

void fizzBuzzFree(FizzBuzz* obj) {
    
}

int main() {
	FizzBuzz *fb = fizzBuzzCreate(15);
	pthread_t id[4];
	
	pthread_create(&id[0], NULL, (void*)fizz, fb);
	pthread_create(&id[1], NULL, (void*)buzz, fb);
	pthread_create(&id[2], NULL, (void*)fizzbuzz, fb);
	pthread_create(&id[3], NULL, (void*)number, fb);

	//printf("Thread %d\n", (int)id[0]);

	pthread_join(id[0], NULL);
	pthread_join(id[1], NULL);
	pthread_join(id[2], NULL);
	pthread_join(id[3], NULL);
}
#ifndef HELPERS_H // include guard
#define HELPERS_H

#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void printVector(vector<T> v) {
	cout << '{';
	for (auto &itr: v) {
		cout << itr << ',';
	}

	cout << '}' << endl;
}

void printVectorChar(vector<char> v);

#endif 
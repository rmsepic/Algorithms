#include "helpers.h"

template <typename T>
void printVector(vector<T> v) {
	cout << '{';
	for (auto &itr: v) {
		cout << itr << ',';
	}

	cout << '}' << endl;
}

void printVectorChar(vector<char> v) {
	cout << '{';

	while (v.size() != 0) {
		cout << v.back() << ',';
		v.pop_back();
	}
	
	cout << '}' << endl;
}
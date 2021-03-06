#ifndef HELPERS_H // include guard
#define HELPERS_H

#include <iostream>
#include <map>
#include <vector>

using namespace std;

void printMap(map<int,int> m);

template <typename T>
void printVector(vector<vector<T>> v) {
	for (auto &i : v) {
		for (auto &j : i) {
			cout << j  << " ";
		}
		cout << endl;
	}
}

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
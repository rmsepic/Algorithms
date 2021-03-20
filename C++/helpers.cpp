#include "helpers.h"

void printVectorChar(vector<char> v) {
	cout << '{';

	while (v.size() != 0) {
		cout << v.back() << ',';
		v.pop_back();
	}
	
	cout << '}' << endl;
}
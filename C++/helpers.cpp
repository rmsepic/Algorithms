#include "helpers.h"

void printVectorChar(vector<char> v) {
	cout << '{';

	while (v.size() != 0) {
		cout << v.back() << ',';
		v.pop_back();
	}
	
	cout << '}' << endl;
}

void printMap(map<int,int> m) {
	for(auto it = m.cbegin(); it != m.cend(); it++) {
    	cout << it->first << " " << it->second << endl;;
	}

	cout << endl;
}
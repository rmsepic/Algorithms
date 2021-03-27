#include <iostream>
#include <string>
#include <map>

#include <math.h>

using namespace std;

string intToRoman(int num) {
	// Initalize map
	map<int, string> m;
	m[1] = 'I';
	m[5] = 'V';
	m[10] = 'X';
	m[50] = 'L';
	m[100] = 'C';
	m[500] = 'D';
	m[1000] = 'M';

	// Convert num to a string
	string str = to_string(num);
	string s;	// Answer string

	for (int i = 0; i < str.size(); i++){
		int num = (str[i] - '0');	// Represents the digit x000
		int figure = pow(10, str.size() - i - 1); // The order of the numbers
		int x = 0, y = 0, z = 0;

		if (figure == 1000) {
			// Only go up to 3 
			z = 1000;
		} else if (figure == 100) {
			x = 1000;
			y = 500;
			z = 100;
		} else if (figure == 10) {
			x = 100;
			y = 50;
			z = 10;
		} else if (figure == 1) {
			x = 10;
			y = 5;
			z = 1;
		}

		while (num > 0) {
			if (num == 9) {
				s += m[z];
				s += m[x];
				num -= 9;
			} else if (num >= 5) {
				s += m[y];
				num -= 5;
			} else if (num == 4) {
				s += m[z];
				s += m[y];
				num -= 4;
			} else {
				s += m[z];
				num -= 1;
			}
		}
	}

	return ans;
}

int main() {
	// 1 <= num <= 3999
	int num = 1994;
	string ans = intToRoman(num);

	cout << ans << endl;

	return 0;
}
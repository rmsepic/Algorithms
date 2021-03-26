#include <iostream>
#include <string>
#include <map>

#include <math.h>

using namespace std;

string intToRoman(int num) {
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
	string ans;

	for (int i = 0; i < str.size(); i++){
		int num = (str[i] - '0');
		int figure = pow(10, str.size() - i - 1);
		string s;

		if (figure == 1000) {

		} else if (figure == 100) {

		} else if (figure == 10) {

		} else if (figure == 1) {
			while (num > 0) {
				if (num == 9) {
					s += m[1];
					s += m[10];
					num -= 9;
				} else if (num >= 5) {
					s += m[5];
					num -= 5;
				} else if (num == 4) {
					s += m[1];
					s += m[5];
					num -= 4;
				} else {
					s += m[1];
					num -= 1;
				}
			}

			ans += s;
		}
	}

	return ans;
}

int main() {
	// 1 <= num <= 3999
	int num = 4;
	string ans = intToRoman(num);

	cout << ans << endl;

	return 0;
}
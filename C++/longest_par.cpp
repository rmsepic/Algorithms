#include <iostream>
#include <string>
#include <vector>

#include "helpers.h"

using namespace std;

int longestValidParentheses(string s) {
	unsigned int max_ = 0;

	// Loop through the string 
	for (int i = 0; i < s.length(); i++) {
		// The valid parentheses cannot start with this character
		// So go to next
		if (s[i] == ')') {
			continue;
		}

		// Valid pars need to begin with '('
		vector<char> vec;
		vec.push_back('(');
		//printVectorChar(vec);
		unsigned int temp_max = 0;
		
		// Loop through the string from i -> end of string
		for (int j = i + 1; j < s.length(); j++) {
			//cout << j << " " << s[j] << endl;
			if (s[j] == '(') {
				vec.push_back('(');
			} else if (s[j] == ')') {
				if (vec.size() > 0 && vec.front() == '(') {
					temp_max += 2;
					vec.pop_back();
				} else {
					// Extra ')' so it is no longer valid
					// Go to the next iteration
					break;
				}

				// Found an invalid parenthese
				// Make sure the vector is empty
				// If not then there are '(' that are unmatched
				if (vec.size() == 0) {
					max_ = max(max_, temp_max);
				} 
			}

			printVectorChar(vec);
		}
		vec.clear();
	}

	return max_;
}

int main() {
	string str = ")()())()()(";
	int ans = longestValidParentheses(str);
	cout << ans << endl;
}
#include <iostream>
#include <vector>
#include <map>

#include "helpers.h"

using namespace std;

int trapWater(vector<int> &height) {
	if (height.size() <= 2) {
		return 0;
	}

	int ans = 0;
	int left = 0, right = 2;
	map<int, int> m;

	while (left < height.size() - 1) {
		while(height[right] <= height[right - 1]) {
			right++;

			if (right >= height.size()) {
				break;
			}
		}

		int vol = min(height[left], height[right]) * (right - left - 1);
		cout << "vol " << vol << " Left " << left << " Right " << right << endl;
		for (int i = left + 1; i < right - 1; i++) {
			vol -= height[i];
		}

		if (m.count(left) > 0) {
			int x = max(m[left], vol);
			m.insert(pair<int,int>(left, x));
		} else {
			m.insert(pair<int,int>(left, vol));
		}

		printMap(m);

		ans += vol;
		left++;
		right = left + 2;
	}


	return ans;
}

int main() {
	//vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
	vector<int> height = {4,1,2,1,3,2};
	int ans = trapWater(height);
	cout << "Answer: " << ans << endl;

	return 0;
}
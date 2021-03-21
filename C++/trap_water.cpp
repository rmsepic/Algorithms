#include <iostream>
#include <vector>
#include <map>

#include "helpers.h"

using namespace std;
/*
 * Loop through the vector
 * For each index in the vector (except for the last one)
 * Calculate the total volume it holds
 * Given an array [i, j, k]
 * Store in a map {i: V1, j: V2}
 * Volume is calculated by V = min(i,k) * (k - i) where k >= i
 */
int trapWater(vector<int> &height) {
	//map<int, int> m;
	unsigned int total_volume = 0;
	unsigned int left = 0, right = 1;
	vector<int> vols;
	bool flag = true;

	while (left < height.size() - 1) {
		cout << height[left] << endl;
		right = left + 1;
		while (height[right] < height[left]) {
			if (right < height.size()) {
				right++;
			} else {
				// Go back to the first loop
				flag = false;
				break;
			}
		}

		if (flag == true) {
			int vol = right - left - 1;
			vols.push_back(vol);
		}

		left++;
		flag = true;
	}

	printVector(vols);

	for (int i = 0; i < vols.size(); i++) {
		total_volume += vols[i];
	}

	return total_volume;
}

int main() {
	//vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
	vector<int> height = {4,2,0,3,2,5};
	int ans = trapWater(height);
	cout << "Answer: " << ans << endl;
}
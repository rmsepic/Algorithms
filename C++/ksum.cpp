#include <iostream>
#include <map>

#include "helpers.h"

using namespace std;


vector<vector<int>> twoSum(vector<int>& nums, int target, int start) {
	vector<vector<int>> next;
	map<int, int> ht;

	for (auto i = start; i < nums.size(); i++){

		if (!next.empty() && next.back()[1] == nums[i]) {
			continue;
		} else {
			int rem = target - nums[i];

			if (ht.count(rem) > 0) {
				next.push_back({rem, nums[i]});
			}

			ht.insert(pair<int, int>(nums[i], i));
		}
	}


	return next;
}

vector<vector<int>> kSum(vector<int>& nums, int target, int start, int k) {
	vector<vector<int>> next;

	// Only need two more numbers 
	if (k == 2) {
		return twoSum(nums, target, start);
	}

	for (int i = start; i < nums.size(); i++) {
		if (i - 1 >= start && nums[i] == nums[i - 1]) {
			continue;
		} else {

			vector<vector<int>> set = kSum(nums, target - nums[i], i + 1, k - 1);
			for (auto &x : set) {
				// Update the answer
				vector<int> temp = x;
				temp.push_back({nums[i]});
				next.push_back(temp);
			}
		}
	}

	return next;
}

vector<vector<int>> fourSum(vector<int>& nums, int target) {
	sort(begin(nums), end(nums));
	printVector(nums);
	return kSum(nums, target, 0, 4);
}



int main() {
	vector<int> nums = {0,4,-5,2,-2,4,2,-1,4};
	//{0,1,5,0,1,5,5,-4};
	// {0,4,-5,2,-2,4,2,-1,4};
	int target = 12;
	//11; 
	//12;

	vector<vector<int>> ans = fourSum(nums, target);
	
	for (auto &i : ans) {
		for (auto &j : i) {
			cout << j  << " ";
		}
		cout << endl;
	}

}
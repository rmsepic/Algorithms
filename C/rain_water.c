#include <stdio.h>
#include <stdlib.h>

int min(int x, int y) {
	if (x < y) {
		return x;
	} else {
		return y;
	}
}

int max(int x, int y) {
	if (x > y) {
		return x;
	} else {
		return y;
	}
}

int rain_water_brute_force(int *arr, int size) {
	int ans = 0;
	for (int i = 0; i < size; i++) {
		int area = 0;
		for (int j = i + 1; j < size; j++) {
			if (arr[j] > area) {
				ans += (j - i - 1) * (min(arr[j], arr[i]) - area);
				area = min(arr[j], arr[i]);
			}
		}
	}

	return ans;
}

int rain_water_dp(int *arr, int size) {
	if (size < 2) {
		return 0;
	}

	int ans = 0;
	int *left_max = (int*)malloc(sizeof(int) * size);
	int *right_max = (int*)malloc(sizeof(int) * size);

	left_max[0] = arr[0];
	right_max[size - 1] = arr[size - 1];

	for (int i = 1; i < size; i++) {
		left_max[i] = max(arr[i], left_max[i - 1]);
	}

	for (int j = size - 2; j >=0; j--) {
		right_max[j] = max(arr[j], right_max[j + 1]);
	}

	for (int k = 1; k < size - 1; k++) {
		ans += min(left_max[k], right_max[k]) - arr[k];
	}

	free(left_max);
	free(right_max);

	return ans;
}

int rain_water_pointers(int *arr, int size) {
	int left = 0;
	int right = size - 1;
	int left_max = 0, right_max = 0;
	int ans = 0;
	
	while (left < right) {
		if (arr[left] < arr[right]) {
			if (arr[left] >= left_max) {
				left_max = arr[left];
			} else {
				ans += left_max - arr[left];
			}

			left++;
		} else {
			if (arr[right] >= right_max) {
				right_max = arr[right];
			} else {
				ans += right_max - arr[right];
			}

			--right;
		}
	}

	return ans;
}

# define SIZE 12
int main(int argc, char **argv) {
	int height[SIZE] = {0,1,0,2,1,0,1,3,2,1,2,1};
	// {2,0,3,4};
	//{4,2,3};
	// {4,2,0,3,2,5};
	// {5,4,3,0,2,4};
	// {0,1,0,2,1,0,1,3,2,1,2,1};
	int ans = rain_water_pointers(height, SIZE);

	//int ans = rain_water(*argv[0], *argv[1]);

	printf("Ans: %d\n", ans);
	return 0;
}
#include <stdio.h>

struct Bar {
	int height;
	int index;
};

int min(int x, int y) {
	if (x < y) {
		return x;
	} else {
		return y;
	}
}

int rain_water(int *arr, int size) {
	if (size < 1) {
		return 0;
	}

	int ans = 0;
	struct Bar left, prev;
	

	for (int i = 1; i < size; i++) {
		// Found a container
		if (arr[i - 1] < arr[i]) {
			int area = arr[i];

			// Looking for right side of container
			for (int j = i - 2; j >= 0; j--) {
				if (j == 0) {
					if (arr[j] >= arr[i]) {
						int vol = min(arr[j], arr[i]) * (i - j - 1);
						ans += vol - area;
					}
				} else if (arr[j] > arr[i - 1]) {
					int vol = min(arr[j], arr[i]) * (i - j - 1);
					ans += vol - area;
				}

				area += arr[j];
			}
		}
	}

	return ans;
}

# define SIZE 6
int main(int argc, char **argv) {
	int height[SIZE] = {5,4,3,0,2,4};
	// {2,0,3,4};
	//{4,2,3};
	// {4,2,0,3,2,5};
	// {5,4,3,0,2,4};
	// {0,1,0,2,1,0,1,3,2,1,2,1};
	int ans = rain_water(height, SIZE);

	//int ans = rain_water(*argv[0], *argv[1]);

	printf("Ans: %d\n", ans);
	return 0;
}
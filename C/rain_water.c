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
	if (size < 2) {
		return 0;
	}

	int ans = 0;
	struct Bar left, greatest;
	

	for (int j = 0; j < size - 1; j++) {
		left.height = arr[j];
		left.index = j;
		greatest.height = arr[j + 1];
		greatest.index = j;
		int area = greatest.height;

		for (int i = 2; i < size; i++) {
			// Found a right and will need to recalc left
			if (arr[i] >= left.height) {
				int vol = min(left.height, arr[i]) * (i - left.index - 1);
				
				if (vol - area > 0) {
					ans += vol - area;
				}
				
				area = 0;
				j = i;
				continue;
			} else if (arr[i] >= greatest.height) {
				greatest.height = arr[i];
				greatest.index = i;
			}

			area += arr[i];
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
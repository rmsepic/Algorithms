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
	struct Bar left;
	

	for (int i = 0; i < size; i++) {
		left.height = arr[i];
		left.index = i;
		
		for (int j = i + 1; j < size; j++) {
			// Found a right side bar, so the container can now hold water
			if (arr[j] >= left.height) {
				int vol = min(left.height, arr[j]) * (j - left.index - 1);
				printf("i: %d   j: %d    vol: %d\n", i, j, vol);
				//printf("i: %d/%d    j: %d/%d    vol: %d\n", i, arr[i], j, arr[j], vol);
				//printf("arr[j]: %d    left.height: %d    vol: %d\n", arr[j], left.height, vol);
				for (int k = i + 1; k < j; k++) {
					vol -= arr[k];
					printf("arr[k]: %d    ", arr[k]);
				}

				ans += vol;
				printf("ans: %d\n\n", ans);
				i = j - 1;
				break;
			}
		}
	}

	return ans;
}

# define SIZE 3
int main(int argc, char **argv) {
	int height[SIZE] = {4,2,3};
	// {4,2,0,3,2,5};
	// {5,4,3,0,2,4};
	// {0,1,0,2,1,0,1,3,2,1,2,1};
	int ans = rain_water(height, SIZE);

	//int ans = rain_water(*argv[0], *argv[1]);

	printf("Ans: %d\n", ans);
	return 0;
}
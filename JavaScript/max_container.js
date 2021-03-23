function max_container(height) {
	let left = 0;
	let right = height.length - 1;
	let water = 0;

	while (left < right) {
		let current_height = Math.min(height[left], height[right]);
		// Update water if it increased
		water = Math.max(water, (right - left) * current_height);

		while (height[left] <= current_height && left < right) {
			left++;
		}

		while(height[right] <= current_height && left < right) {
			right--;
		}
	}

	return water;
};

console.log(max_container([1,8,6,2,5,4,8,3,7]));





var longestValidParentheses = function(s) {
	if (s.length == 0) {
		return 0;
	}  

	let dp = Array(s.length);
	dp.fill(0);
	let stack = [];
	for (let i = 0; i < s.length; i++) {
		if (s[i] == '(') {
			stack.push(i);
		// s[i] == ')'
		} else if (stack.length > 0) {
			dp[i] += dp[i - 1] + 2;
			let idx = stack.pop();
			if (idx > 0) {
				dp[i] += dp[idx - 1];
			}
		}
		console.log(dp);
	}

	return Math.max(...dp);
};

console.log(longestValidParentheses("()(())"));

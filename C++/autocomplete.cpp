#include <iostream>
#include <string>
#include <list>

using namespace std;

list<list<string>> autoSuggestion(const unsigned int len, list<string> repo, string userReq) {
	// First sort the list
	int size = repo.size();
	repo.sort();

	// Answer goes in this list
	list<list<string>> ans;	

	// Holds the current string being searched
	string curr_q;	
	curr_q += userReq[0];

	for (int i = 1; i < userReq.length(); i++) {
		curr_q += userReq[i];	
		list<string> sug;
		for (list<string>::iterator itr = repo.begin(); itr != repo.end() && sug.size() < 3; itr++) {
			if (itr->rfind(curr_q, 0) == 0) {
				sug.push_front(itr->c_str());
			}
		}

		if (sug.size() > 0) {
			ans.push_front(sug);
		}
	}

	return ans;
}

int main() {
	list<string> repo = {"taxes", "taxis", "tex", "tax tools", "tax software"};
	const unsigned int len = repo.size();
	string userReq = "tax ";
	list<list<string>> ans = autoSuggestion(len, repo, userReq);
	cout << ans.size() << endl;
	for (auto i : ans) {
		for (auto j : i) {
			cout << j << endl;
		}
	}
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Largest Sum Contiguous Array
// Kadane's Algorithm : Time Complexity O(n) and Space Complexity O(1)

// Approach 1 : Does not work with all negative numbers in array.

// int main() {
// 	vector<int> a={-2,-3,4,-1,-2,1,5,-3};
// 	int max_end_here=0;
// 	int max_so_far=0;
// 	for(int x : a)
// 	{
// 		max_end_here=max_end_here+x;
// 		if(max_end_here<0)
// 			max_end_here=0;
// 		if(max_so_far<max_end_here)
// 			max_so_far=max_end_here;
// 	}
// 	cout<<max_so_far;
// 	return 0;
// }

// Approach 2 : Works for both cases.

int main()
{
	// vector<int> a={-1,-2,-3,-5,-6};
	vector<int> a={-2,-3,4,-1,-2,1,5,-3};

	int max_so_far=a[0],curr_max=a[0];

	for(int x : a)
	{
		curr_max=max(x,curr_max+x);
		max_so_far=max(curr_max,max_so_far);
	}
	cout<<max_so_far;

	return 0;
}

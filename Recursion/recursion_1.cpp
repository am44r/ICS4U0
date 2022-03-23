/**
 * @name: Recursion 1
 * @author: Amaar Sana
 * @Description: Given a non-negative integer n, create a double 
				 countdown-pattern in the console.
 * @studentNumber: 917364
*/
 
/**
  * @param [in]n non-negative integer that user passes through
  * @param count a deafult parameter used as an increment
  * @return a double countdown starting from `n` to `0`
*/ 

#include <bits/stdc++.h>

using namespace std;

int doubleCountdown(int n, int count=0)
{
    if (n == count)
    {
        return 1;
    }
	cout << n - count << endl;
	doubleCountdown(n, count+1);
		
	
	cout << count << endl;
	return 0;
}

int main() 
{
	// Test cases
	doubleCountdown(5);
	//doubleCountdown(6);
	//doubleCountdown(4);
}

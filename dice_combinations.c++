#include <bits/stdc++.h>

using namespace std;


// #define MOD pow(10, 9) + 7

int main(){
    long long n;
    cin >> n;
    long long MOD = pow(10, 9) + 7;

    long long dp[n + 1];
    dp[0] = 1;

    for(int i = 1; i < n + 1; i++){
        dp[i] = 0;
        for(int j = 1; j < 7; j++){
            if(i >= j){
                dp[i] = (dp[i] + dp[i-j]) % MOD;
            }
        }
    }

    cout << dp[n] <<endl;
}
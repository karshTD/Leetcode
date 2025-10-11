#include <vector>
using namespace std;

class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> trustCount(n + 1, 0);
        vector<bool> trustsSomeone(n + 1, false);
        
        for (const auto& t : trust) {
            trustsSomeone[t[0]] = true;
            trustCount[t[1]]++;
        }
        
        for (int i = 1; i <= n; i++) {
            if (!trustsSomeone[i] && trustCount[i] == n - 1) {
                return i;
            }
        }
        
        return -1;
    }
};
#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int max_len = 0;
    int n = strlen(s);
    
    for (int i = 0; i < n; i++) {
        int seen[256] = {0};
        int current_len = 0;
        
        for (int j = i; j < n; j++) {
            if (seen[s[j]] == 0) {
                seen[s[j]] = 1;
                current_len++;
                if (current_len > max_len) {
                    max_len = current_len;
                }
            } else {
                break;
            }
        }
    }
    
    return max_len;
}
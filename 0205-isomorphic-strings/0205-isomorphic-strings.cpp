class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if ( s.length() != t.length()){
            return false;
        }

        unordered_map<char, char> mapst;
        unordered_map<char , char> mapts;


        for(int i = 0; i < s.length(); i ++){
            char c1 = s[i];
            char c2 = t[i];
        

        if(mapst.count(c1)){
            if ( mapst[c1] != c2) { return false ; }
        }

        if(mapts.count(c2)){
            if (mapts[c2] != c1){ return false; }
        }

        mapst[c1] = c2;
        mapts[c2] = c1;



    }

    return true; 
    }
};
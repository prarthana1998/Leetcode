class Solution {
public:
    int countLatticePoints(vector<vector<int>>& circles) {

        set<pair<int, int>> unique_pair;

        for(auto &circle : circles)
        {
            int a = circle[0];
            int b = circle[1];
            int r = circle[2];

            int r_squared = r*r;
        
        for(int x = -r; x <= r; x++)
        {
            for(int y = -r; y<=r ; y++)
            {
                if((x*x)+(y*y) <= r_squared)
                unique_pair.insert({a+x, b+y});
            }
        }
        }
        return unique_pair.size();
    }
};
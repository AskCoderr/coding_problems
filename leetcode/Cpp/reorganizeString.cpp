// ALGORITHM IDEA

// -- make a priority queue
// -- start filling initially in the primary layer (layer where there is a gap of
//    index 1 in account of repetitiveness) of the result array by the highest priority alphabet
// -- when there is a change in the highest priority alphabet start filling the secondary layer (the
//    empty slots left by the primary layer) until either the initial primary alphabet becomes
//    higher priority again in which case you have to go back to the primary layer or a new alphabet emerges
//    in which case you will have to keep filling the secondary layer until finished then go back to the primary
// -- in case the secondary is still to be finished by the end, there is no valid solution

// ALGORITHM
//
//  make a priority queue {data}
//  set variables primAlph = data.pop(), primIndex = 0, secIndex = None, mapp = vector()
//  while loop:
//      currAlph = data.pop()
//      if primAlph == currAlph
//          adjust secIndex if None
//          adjust primIndex
//          put currAlph in mapp[primIndex]
//      else
//          if secIndex == None
//              adjust primAlpha
//              adjust primIndex
//              put currAlph in mapp[primIndex]
//          else
//              put currAlph in mapp[secIndex]
//              adjust secIndex
//              if secondary layer satisfied
//                  secIndex = None
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <utility>

using std::vector, std::string, std::unordered_map;

class Solution
{
private:
    struct Container
    {
        string main;
        vector<std::pair<char, int>> stor;
        unordered_map<char, int> map;

        Container(string str)
        {
            main = str;
            strToMap();
            mapToVec();
            std::sort(stor.begin(), stor.end(), [](auto &a, auto &b)
                      { return a.second < b.second; });
        }

        void strToMap()
        {
            for (char i : main)
            {
                map[i]++;
            }
        }

        void mapToVec()
        {
            for (const auto &i : map)
            {
                stor.push_back(i);
            }
        }

    public:
        char pop()
        {
            /*
            if last element value = 1
                del pair
            else
                decrement value
                while last elem value less than prev element value
                    shift pair left
            */

            char temp = stor.back().first;
            if (stor.back().second == 1)
            {
                stor.pop_back();
            }
            else
            {
                stor.back().second--;
                int index = stor.size() - 1;
                while (index != 0 && stor[index].second < stor[index - 1].second)
                {
                    std::swap(stor[index], stor[index - 1]);
                    index--;
                }
            }
            return temp;
        }
    };

public:
    string reorganizeString(string s)
    {
        Container data(s);
        char primAlph = data.pop();
        int primIndex = 0;
        int secIndex = -1;
        unordered_map<int, char> mapp = {{0, primAlph}};

        for (int i = 0; i < s.size() - 1; i++)
        {
            char currAlph = data.pop();
            if (primAlph == currAlph)
            {
                if (secIndex == -1)
                {
                    secIndex = primIndex + 1;
                }
                primIndex += 2;
                mapp[primIndex] = currAlph;
            }
            else
            {
                if (secIndex == -1)
                {
                    primAlph = currAlph;
                    primIndex++;
                    mapp[primIndex] = currAlph;
                }
                else
                {
                    mapp[secIndex] = currAlph;
                    secIndex += 2;
                    if (secIndex == primIndex + 1)
                    {
                        secIndex = -1;
                    }
                }
            }
        }

        string result = "";
        for (int i = 0; i < s.size(); i++)
        {
            if (mapp.count(i))
            {
                result.push_back(mapp[i]);
            }
            else
            {
                return "";
            }
        }
        return result;
    }
};

int main()
{
    Solution sol;
    string s = sol.reorganizeString("aaabbcde");
    std::cout << s << std::endl;
    return 0;
}

// https://leetcode.com/problems/reorganize-string/description/
// /*
// -----IDEA-----
// - convert the edge list into a adjacency list
// - take a initial node
// - the slow pointer and the fast pointer should visit all possible routes
// - if a slow pointer meets its corresponding fast pointer, we retrieve the
// nodes in the cycle from the fast pointer's history till we reach that
// common node again to get all the nodes in the cycle

// -----1st breakdown-----
// -   get size of edges {n}
// -   inititalize dictionary {graph} with unique_ptr for n nodes (takes
// order of insertion as well, as the second element in the pair in value)
// -   for i in enumerate(edges)
// -       add the data into graph
// -   set slow_pointer and fast_pointer variables
// -   instantiate two instances of recrs function
// (slow and fast(fast stores history)) that goes through all the nodes
// -   while loop
// -       yield fast twice (update fast ptr)
// -       yield slow once (update slow ptr)
// -       if they equal
// -           trace back through fast history until you find the equal
// node to get all the nodes in the cycle
// -           find out the latest node in the input from the data in graph
// */

// #include <vector>
// #include <generator>
// #include <unordered_map>

// using namespace std;

// class Solution
// {
// public:
//     vector<int> findRedundantConnection(vector<vector<int>> &edges)
//     {
//         unordered_map<int, vector<pair<int, int>>> graph;
//         int order = 0;
//         for (const auto &i: edges) {
//             if (graph.count(i[0])) {
//                 graph[i[0]].push_back({i[1], order});
//                 graph[i[1]].push_back({i[0], order});
//                 order++;
//             } else {
//                 graph[i[0]] = {{i[1], order}};
//                 graph[i[1]] = {{i[0], order}};
//                 order++;
//             }
//         }
//         slowPointer = edges[0][0];
//         fastPointer = edges[0][0];
//         vector<int> history = {fastPointer};
//         auto fastTraverse = fast(history, graph);
//         auto slowTraverse = slow(graph);
//         auto fastTraveller = fastTraverse.begin();
//         auto slowTraveller = slowTraverse.begin();
//         slowTraveller++;
//         while (true) {
//             fastTraveller++;
//             fastTraveller++;
//             slowTraveller++;
            
//             if (*fastTraveller == *slowTraveller) {
//             /*
//             i = history[history.size()-1]
//             int latestInput;
//             while (history[i] != *fastTraveller) {
//                 compare nodes at index and index-1 of history in graph and see how latest is the input
//                 reduce i
//             }
//             */
//                 int i = history.size()-2;
//                 int latestInput = howLatest(graph[history[i]], history[i+1]);
//                 while (history[i] != *fastTraveller) {
//                     int temp = howLatest(graph[history[i]], history[i-1]);
//                     if (latestInput < temp) {
//                         latestInput = temp;
//                     }
//                     i--;
//                 }
//             }
//             return edges[order];
//         }
//     }

// private:
//     int slowPointer;
//     int fastPointer;
//     generator<int> fast(vector<int>& history, unordered_map<int, vector<pair<int, int>>>& graph)
//     {   
//         for (const pair<int, int> j: graph[fastPointer]) {
//             history.push_back(j.first);
//             co_yield j.first;
//             fastPointer = j.first;
//             fast(history, graph);
//             fastPointer = j.first;
//             history.pop_back();
//         }
//     }

//     generator<int> slow(unordered_map<int, vector<pair<int, int>>>& graph){
//         for (const pair<int, int> k: graph[slowPointer]) {
//             co_yield k.first;
//             slowPointer = k.first;
//             slow(graph);
//             slowPointer = k.first;
//         }
//     }

//     int howLatest(vector<pair<int, int>>& vec, int num) {

//    }
// };

// // initial leaf node exception

/*
- make adjacency list
- 
*/

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        
    }
};
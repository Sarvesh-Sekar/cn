 #include<stdio.h>
 #include<stdbool.h>
 #include<limits.h>
 #defineN10//Maxnumberofnodes
 int find_min_distance(intdist[],boolvisited[], intnodes){
 intmin=INT_MAX,min_index;
 for(intv=0;v<nodes;v++){
 if(visited[v]==false&&dist[v]<=min){
 min=dist[v];
 min_index=v;
 }
 }
 returnmin_index;
 }
 voidlink_state(intgraph[N][N], intsrc, intnodes){
int dist[N];
 bool visited[N];
 for (int i = 0; i < nodes; i++) {
 dist[i] = INT_MAX;
 visited[i] = false;
 }
 dist[src] = 0;
 for (int count = 0; count < nodes- 1; count++) {
 int u = find_min_distance(dist, visited, nodes);
 visited[u] = true;
 for (int v = 0; v < nodes; v++) {
 if (!visited[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) {
 dist[v] = dist[u] + graph[u][v];
 }
 }
 }
 printf("\nLink State Routing Table for Node %d:\n", src);
 for (int i = 0; i < nodes; i++) {
 if (dist[i] == INT_MAX)
 printf("Node %d: INF\n", i);
 else
 printf("Node %d: %d\n", i, dist[i]);
 }
 }
 int main() {
 int graph[N][N], nodes, i, j, src;
 printf("Enter the number of nodes: ");
 scanf("%d", &nodes);
 printf("Enter the graph matrix (enter 9999 for infinity):\n");
 for (i = 0; i < nodes; i++) {
 for (j = 0; j < nodes; j++) {
 scanf("%d", &graph[i][j]);
 if (i == j)
 graph[i][j] = 0;
 if (graph[i][j] == 9999)
 graph[i][j] = INT_MAX;
 }
 }
 printf("Enter the source node: ");
scanf("%d",&src);
 link_state(graph,src,nodes);
 return 0;
 }
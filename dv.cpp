#include <stdio.h>
 #include <limits.h>
 #define N 10 // Max number of nodes
 void distance_vector(int cost[N][N], int nodes) {
 int distance[N][N], i, j, k;
 for (i = 0; i < nodes; i++) {
 for (j = 0; j < nodes; j++) {
 distance[i][j] = cost[i][j];
 }
 }
 for (k = 0; k < nodes; k++) {
 for (i = 0; i < nodes; i++) {
 for (j = 0; j < nodes; j++) {
 if (distance[i][j] > distance[i][k] + distance[k][j])
 distance[i][j] = distance[i][k] + distance[k][j];
 }
 }
 }
 printf("\nDistance Vector Routing Table:\n");
 for (i = 0; i < nodes; i++) {
 printf("Router %d: ", i);
 for (j = 0; j < nodes; j++) {
 if (distance[i][j] == INT_MAX)
 printf("INF ");
 else
 printf("%d ", distance[i][j]);
 }
 printf("\n");
 }
 }
 int main() {
 int cost[N][N], nodes, i, j;
 printf("Enter the number of nodes: ");
 scanf("%d", &nodes);
 printf("Enter the cost matrix (enter 9999 for infinity):\n");
 for (i = 0; i < nodes; i++) {
 for (j = 0; j < nodes; j++) {
 scanf("%d", &cost[i][j]);
 if (i == j)
 cost[i][j] = 0;
 if (cost[i][j] == 9999)
cost[i][j]=INT_MAX;
 }
 }
 distance_vector(cost,nodes);
 return 0;
 }
#include <bits/stdc++.h>
using namespace std;

const int N = 100000;

double X[N], Y[N];

double getDistance(double x1, double y1, double x2, double y2){
    double dist = (abs(x2 - x1) * abs(x2 - x1)) + (abs(y2 - y1) * abs(y2 - y1));
    return sqrt(dist);
}

int main() {
    int n;
    cin>>n;
    double px, py;
    cin>>px>>py;
    for(int i = 0; i <= n; i++){
        cin>>X[i]>>Y[i];
    }
   
    double curr_x = px, curr_y = py;
   
    int flag = 0;
   
    double dist;
   
    for(int i = 0; i <= n; i++){
        dist = getDistance(curr_x, curr_y, X[i], Y[i]);
       // cout<<i<<" ";
       // cout<<dist<<endl;
        if(dist <= 10){
            flag = 1;
            cout<<i<<endl;
            printf("%.2f", dist);
            break;
        }
        double x_diff = X[i] - curr_x;
        double y_diff = Y[i] - curr_y;
        double x_change = 20 * x_diff;
        x_change /= dist;
        double y_change = 20 * y_diff;
        y_change /= dist;
        curr_x = curr_x + x_change;
        curr_y = curr_y + y_change;
        //cout<<"NEW --> "<<curr_x<<" "<<curr_y<<endl;
    }
   
    if(flag == 0){
        cout<<-1<<endl;
        printf("%.2f", dist);
    }
     
    return 0;
}
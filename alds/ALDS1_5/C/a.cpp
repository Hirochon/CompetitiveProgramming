#include <iostream>
#include <cmath>
using namespace std;

void koch(int d, double p1[], double p2[]) {
    double rp1[4], rs[4], ru[4], rt[4], rp2[4];
    double xy[4];

    if (d == 0) {
        return;
    }

    rp1[0] = p1[0];
    rp1[1] = p1[1];
    rp2[0] = p2[0];
    rp2[1] = p2[1];

    xy[0] = p2[0] - p1[0];
    xy[1] = p2[1] - p1[1];
    rs[0] = p1[0] + (xy[0] / 3);
    rs[1] = p1[1] + (xy[1] / 3);
    rt[0] = p2[0] - (xy[0] / 3);
    rt[1] = p2[1] - (xy[1] / 3);
    
    double x = rt[0] - rs[0];
    double y = rt[1] - rs[1];
    ru[0] = x * cos(M_PI / 3) - y * sin(M_PI / 3) + rs[0];
    ru[1] = x * sin(M_PI / 3) + y * cos(M_PI / 3) + rs[1];

    koch(d-1, rp1, rs);

    printf("%.8f %.8f\n", rs[0], rs[1]);

    koch(d-1, rs, ru);
    
    printf("%.8f %.8f\n", ru[0], ru[1]);
    
    koch(d-1, ru, rt);
    
    printf("%.8f %.8f\n", rt[0], rt[1]);
    
    koch(d-1, rt, rp2);
}

int main() {
    int n;
    double p1[4] = {0, 0};
    double p2[4] = {100, 0};

    scanf("%d", &n);
    printf("%.8f %.8f\n", p1[0], p1[1]);
    koch(n, p1, p2);
    printf("%.8f %.8f\n", p2[0], p2[1]);
    return 0;
}
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <random>

using namespace std;

mt19937 gen;
uniform_real_distribution<double> uniform(0.0, 1.0);

double S(int j, double *x, int N, double a){
    
    int j_next = (j+1) % N;
    int j_prev = (j-1) % N;

    return (a*x[j]*x[j])/2.0 + x[j]*(x[j]-x[j_next]-x[j_prev])/a;
}

void update(double *x, int N, double a,
        //std::uniform_real_distribution<double> epsil(mt19937),
        //mt19937 gen,
        double epsilon,
        int *acc_counter){
    
    uniform_real_distribution<double> eps(-epsilon, epsilon);   // This is slow

    double old_x, old_Sj, dS;
    int j;
    for (j = 0; j<N; j++){
        old_x = x[j];
        old_Sj = S(j, x, N, a);
        x[j] += eps(gen) ;
        dS = S(j, x, N, a) - old_Sj;

        if(exp(-dS) < uniform(gen)){    // Metropolis
            x[j] = old_x;
        } else {
            *acc_counter += 1;
        }
    }
}

double compute_G(double *x, int n, int N){
    double g = 0;
    for (int i=0; i<N; i++){
        g += x[i] * x[(i+n)%N];
    }

    return g/N;
}

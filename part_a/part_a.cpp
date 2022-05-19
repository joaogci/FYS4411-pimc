
#include "pimc_funcs.h"

int main(int argc, char* argv[]){

    int N = 20;
    int N_corr = 20;
    int N_cf = 1e6;
    double a = 0.5;
    double epsilon = 1.6;

    double x[N];
    double corr[N];

    double *G[N_cf];
    for (int i=0; i<N_cf; i++){
        G[i] = new double [N];
    }

    mt19937 generator;
    normal_distribution <double> distribution(0.0, 1.0);
    uniform_real_distribution <double> epsil(-epsilon, epsilon);

    // Initialize the starting positions as random normally distributet numbers
    for (int i; i<N; i++){
        x[i] = distribution(generator);
    }

    // Main calculations

    // Thermalize
    int acc_counter = 0;    // Acceptance counter, can be omitted
    for (int i=0; i<10*N_corr; i++){
        //eps = epsil(generator);
        //update(x, N, a, &epsil, generator, &acc_counter);     
        update(x, N, a, epsilon, &acc_counter);     
    }

    // Main loop
    for (int i=0; i<N_cf; i++){
        for (int j=0; j<N_corr; j++){
            update(x, N, a, epsilon, &acc_counter);
        }

        for (int n=0; n<N; n++){
            G[i][n] = compute_G(x, n, N);
        }
    }

    // Compute average correlation
    double avg_G;
    for (int n=0; n<N; n++){
        avg_G = 0.0;
        for (int i=0; i<N_cf; i++){
            avg_G += G[i][n];
        }
        avg_G /= N_cf;
        corr[n] = avg_G;
    }

    cout << "Obtained first exited energy lvl: " << log(corr[0] / corr[1]) / a << endl;
    cout << "Expected first exited energy lvl: 1.0" << endl;

    return 0;
}

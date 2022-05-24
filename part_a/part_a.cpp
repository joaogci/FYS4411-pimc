
#include "pimc_funcs.h"

int main(int argc, char* argv[]){

    int N = 20;
    int N_corr = 20;
    int N_cf = 1e6;
    int nbins = 10;
    double a = 0.5;
    double epsilon = 1.4;   // 1.6

    double x[N];
    double corr[nbins][N];
    int acc_counter;

    double *G[N_cf];
    for (int i=0; i<N_cf; i++){
        G[i] = new double [N];
    }

    /*
    cout << log10(N_cf) << endl;
    printf("Integer: %d\n", (int)log10(N_cf));
    exit(1);
    */

    unsigned int seed = (unsigned int) time(NULL);

    mt19937 generator (seed);
    normal_distribution <double> distribution(0.0, 1.0);
    uniform_real_distribution <double> epsil(-epsilon, epsilon);

    // Do the entire thing nbins times
    for (int bin=0; bin<nbins; bin++){

        // Initialize the starting positions as random normally distributet numbers
        x[0] = 0.0;
        //x[N-1] = 0.0;
        for (int i=1; i<N-1; i++){    // Fixed initial and final pos
        //for (int i=0; i<N; i++){      // Random initial and final pos
            x[i] = distribution(generator);
            //x[i] = 0.0;
        }

        // Main calculations

        // Thermalize
        acc_counter = 0;    // Acceptance counter, can be omitted
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
            corr[bin][n] = avg_G;
        }

    }   // End bins loop

    cout << "Obtained first exited energy lvl: " << endl;

    ofstream ofile;
    string filename = "delta_E_" + to_string((int)log10(N_cf)) + ".txt";
    ofile.open(filename);

    double G_Ratio, delta_E;
    for (int bin=0; bin<nbins; bin++){

        for (int n=0; n<N-1; n++){
            G_Ratio = corr[bin][n] / corr[bin][(n+1)%N];
            delta_E = log(G_Ratio) / a;
            //cout << delta_E << endl;
            ofile << delta_E << ", ";
        }
        // Last element done manually to ensure proper formating
        G_Ratio = corr[bin][N-1] / corr[bin][0];
        delta_E = log(G_Ratio) / a;
        ofile << delta_E << endl;
    }
    ofile.close();

    //log(corr[0] / corr[1]) / a << endl;
    //cout << "Expected first exited energy lvl: 1.0" << endl;

    cout << "Accepted " << acc_counter << "/" << N*(10*N_corr + N_cf*N_corr) << " changes." << endl;
    cout << "Acceptance probability: " << (double) acc_counter / (double)(N*(10*N_corr + N_cf*N_corr)) << endl;

    // Free G arrays
    for (int i=0; i<N_cf; i++){
        delete[] G[i];
    }

    return 0;
}

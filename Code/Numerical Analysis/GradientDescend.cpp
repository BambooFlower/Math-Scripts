// Example of Gradient Descent

#include <stdio.h>
#include <stdlib.h>

double dfx(double x) {
    return 4*(x*x*x) - 9*(x*x);
}

double abs_val(double x) {
    return x > 0 ? x : -x;
}

double gradient_descent(double dx, double error, double gamma, unsigned int max_iters) {
    double c_error = error + 1;
    unsigned int iters = 0;
    double p_error;
    while (error < c_error && iters < max_iters) {
        p_error = dx;
        dx -= dfx(p_error) * gamma;
	    c_error = abs_val(p_error-dx);
        printf("\nc_error %f\n", c_error);
        iters++;
    }
    return dx;
}

int main() {
    double dx = 6;
    double error = 1e-6;
    double gamma = 0.01;
    unsigned int max_iters = 10000;
    printf("The local minimum is: %f\n", gradient_descent(dx, error, gamma, max_iters));
    return 0;
}
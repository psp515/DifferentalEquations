#include <iostream>
using namespace std;

double ** make_matrix(int v_n, double h, double a, double b){
    double ** matrix = 0;
    matrix = new double*[v_n];

    for(int i = 0; i < v_n; i++)
    {
        matrix[i] = new double[2*v_n];

        for(int j = 0; j < 2*v_n; j++)
            matrix[i][j] = 0;
    }

    matrix[0][0] = 1;
    matrix[0][1] = 2;

    matrix[v_n-1][v_n-1] = 2*h*h*h+2*h*b+2*h-2*b-2;
    matrix[v_n-1][v_n-2] = h*h+2*b+2;

    for(int i =1; i < v_n-1; i++)
    {
        matrix[i][i-1] = 2*(a+i*h)+2-h;
        matrix[i][i] = 4*(a+i*h)+4;
        matrix[i][i+1] = 2*(a+i*h)+2+h;
    }


    return matrix;
}

double* make_x(int v_n, double h, double b)
{
    double * x = new double[v_n];

    x[0]=0;
    x[v_n-1] = 4*h*(b+1) +h*h + h*h*h*4;

    for(int i = 1; i < v_n-1; i++)
        x[i] = 2*h*h;

    return x;
}


void print_matrix(double** matrix, int v_n)
{
    for(int i =0; i < v_n; i++)
    {
        std::cout << ' ';
        for(int j = 0; j < v_n; j++)
        {
            std::cout << matrix[i][j] <<' ';
        }
        std::cout << "\n";
    }
}

void print_arr(double* array, int v_n)
{
    for(int i =0; i < v_n; i++)
        std::cout<< i+1 << ". " << array[i] << endl;
}


double ** reverse_matrix(int n, double ** matrix)
{
    int i, j, k;
    double d;


    double ** a = 0;
    a = new double*[200];

    for(i = 0; i < 200; i++)
    {
        a[i] = new double[2*200];

        for(j = 0; j < 2*200; j++)
            a[i][j] = 0;
    }


    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            a[i][j] = matrix[i-1][j-1];
        }
    }

    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= 2 * n; j++)
        {
            if (j == (i + n))
            {
                a[i][j] = 1;
            }
        }
    }
    for (i = n; i > 1; i--)
    {
        if (a[i-1][1] < a[i][1])
        {
            for(j = 1; j <= n * 2; j++)
            {
                d = a[i][j];
                a[i][j] = a[i-1][j];
                a[i-1][j] = d;
            }
        }
    }
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n * 2; j++)
        {
            if (j != i)
            {
                d = a[j][i] / a[i][i];
                for (k = 1; k <= n * 2; k++)
                {
                    a[j][k] = a[j][k] - (a[i][k] * d);
                }
            }
        }
    }
    for (i = 1; i <= n; i++)
    {
        d=a[i][i];
        for (j = 1; j <= n * 2; j++)
        {
            a[i][j] = a[i][j] / d;
        }
    }


    double ** inversed_matrix = 0;
    inversed_matrix = new double*[n];

    for(i = 0; i < n; i++)
    {
        inversed_matrix[i] = new double[n];

        for(j = 0; j < n; j++)
            inversed_matrix[i][j] = 0;
    }

    for (i = 1; i <= n; i++)
    {
        for (j = n + 1; j <= n * 2; j++)
        {
            inversed_matrix[i-1][j-n-1] = a[i][j];
        }
    }

    return inversed_matrix;
}

void solve_equation(int n, int a, int b)
{
    double h = (double)(b-a)/n;
    int v_n = n+1;

    double** matrix = make_matrix(v_n,h,a,b);
    double* x = make_x(v_n, h, b);

    //print_matrix(matrix,v_n);

    double** inversed_matrix = reverse_matrix(v_n, matrix);
    //print_matrix(inversed_matrix, v_n);

    double* ans = new double [v_n];

    for(int i = 0; i < v_n; i++)
        ans[i]=0;

    for(int i = 0; i < v_n; i++)
        for(int k = 0; k < v_n; k++)
        {
            ans[i] += inversed_matrix[i][k] * x[k];
        }

    print_arr(ans,v_n);
}

int main() {

    std::cout << "Start" << std::endl;
    std::cout << "-------------------" << std::endl;
    std::cout << "n = 10" << std::endl;
    solve_equation(10,0,1);
    std::cout << "-------------------" << std::endl;
    std::cout << "n = 50" << std::endl;
    solve_equation(50,0,1);

    return 0;
}



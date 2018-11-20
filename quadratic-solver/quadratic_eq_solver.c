#include <stdio.h>
#include <math.h>

// this is a declaration of solve_d (to announce that it exists)
float solve_d(float a, float b, float c);
float solve_x(float a, float b, float c, int sign);


int solve(float a, float b, float c)
{
    float d, x1, x2;

    d = solve_d(a, b, c);

    printf("D = %5.2f\n", d);
    if (d < 0) // if diskriminant is negative
    {
        printf("Nope, quadratic equation has no solution (d = %5.2f)\n", d);
        return 0;
    }

    if (d == 0) // if diskriminant is zero
    {
        x1 = solve_x(a, b, d, 0);
        printf("The one and only solution is: %5.2f\n", x1);
        return 0;
    }

    else
    {
        x1 = solve_x(a, b, d, 0);
        x2 = solve_x(a, b, d, 1);
        printf("First solution: %5.2f | Second solution: %5.2f\n", x1, x2);
        return 0;
    }
}

float solve_x(float a, float b, float d, int sign) // sign == 1 --> plus
{
    float x;

    if (sign) // use +
    {
        x = (-b + sqrt(d) ) / (2*a);
        return x;
    }

    else
    {
        x = (-b - sqrt(d) ) / (2*a);
        return x;
    }
}


float solve_d(float a, float b, float c)
{
    float d;
//    d = b * b -4.0 * a * c;
    d = powf(b, 2) -4.0*a*c;
    return d;
}



int main(void)
{
    // declare & define variables
    float a = 1;
    float b = 3;
    float c = -4;
    /* the result: x1 = -4 | x2 = 1 */

    // print as integers
    printf("Variable a is: %f\n", a);
    printf("Variable b is: %f\n", b);
    printf("Variable c is: %f\n", c);

    // print the whole equation with their respective signs
    printf("\n\nEquation: (%+5.2f)x^2 (%+5.2f)x %+5.2f\n",a,b,c);

    // solve
    solve(a,b,c);

    return 0;
}

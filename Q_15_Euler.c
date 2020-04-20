#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// function declaration

float f(float t ,float y);
float exact_sol(float t);

int main()
{
	float t, t0 = 0 ,tf = 2 ,y0 = 0.5 , y ,h =0.2 ,err_bound , err;
    
    t = t0;
    y = y0;

    while (t <= tf + h)
    {
       err = (exact_sol(t) - y);

       // from the formula of error bound calculated 
       err_bound = (exp(t) - 1) * 0.1 * (0.5 * exp(2) - 2);

       printf(" Error at the mesh point t = %f is %f \n",t ,err );
       printf(" Error Bound at the mesh point t = %f is %f \n\n",t ,err_bound );

       y = y + h * f(t , y);

       t = t + h ;

    }
	return 0;
}

// definition of dy/dt(t,y)
float f(float t ,float y)
{
	return (y - t * t + 1);
}

float exact_sol(float t)
{
	return ((t + 1) * (t + 1) - 0.5 * exp(t));
}

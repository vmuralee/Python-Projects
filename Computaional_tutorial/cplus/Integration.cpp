#include<iostream>
#include "Trapezoidal_rule.h"

using namespace std;

double func(double x){

  return x*x;
}


double rectangle_rule(double a, double b, int n, double (*func)(double))
{
  double rectangle_sum;
  double fa, fb, x, step;
  int j;
  step=(b-a)/((double) n);
  rectangle_sum=0.;
  for (j = 0; j <= n; j++){
    x = (j+0.5)*step+a; // midpoint of a given rectangle
    rectangle_sum+=(*func)(x); // add value of function.
  }
  rectangle_sum *= step; // multiply with step length.
  return rectangle_sum;
}
double trapezoidal_rule(double a, double b, int n, double (*func)(double))
{
  double trapez_sum=0;
  double fa, fb, x, step;
  int j;
  step=(b-a)/((double) n);
  fa=(*func)(a)/2. ;
  fb=(*func)(b)/2. ;
  
  for (j=1; j <= n-1; j++){
    x=j*step+a;
    trapez_sum+=(*func)(x);
  }
  trapez_sum=(trapez_sum+fb+fa)*step;
  return trapez_sum;
}
int main(){
  //cout<<trapezoidal_rule(0,1,10,func)<<endl;
  //cout<<rectangle_rule(0,1,100,func)<<endl;
  Trapezoid_Integration* obj = new Trapezoid_Integration(0,1,20);
  obj->set_value(0,1,10);
  obj->TrapeIntegrate(func);
  obj->print_value();
  
}

#include <iostream>

using namespace std;

class Trapezoid_Integration{
 private:
  double xlow,xup;
  int n;

 public:
  Trapezoid_Integration(double xl, double xu, int N){
    xl = xlow;
    xu = xup;
    N = n;
   
    
    cout<<"Trapezoidal object is created"<<endl;
  }
  //~Trapezoid_Integration();
  void TrapeIntegrate(double (*func)(double)){
    double trapez_sum=0;
    double fa, fb, x, step;
    int j;
    step=(xup-xlow)/((double) n);
    fa=(*func)(xlow)/2. ;
    fb=(*func)(xup)/2. ;
  
    for (j=1; j <= n-1; j++){
      x=j*step+xlow;
      trapez_sum+=(*func)(x);
    }
    
    trapez_sum=(trapez_sum+fb+fa)*step;
    cout<<trapez_sum<<endl;
  }
  void set_value(double a, double b, int N){
    xlow =a;
    xup = b;
    n = N;
  }
  void print_value(){
    cout<<"The Integration done from "<<xlow<<" to "<<xup<<" using "<<n<<" interation";
  }
};

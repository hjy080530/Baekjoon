#include <iostream>
using namespace std;
int main() {
  long long int n,a,b;
  cin>>n;
  for(int i=1;i<=n;i++){
    cin>>a>>b;
    cout<<"Case #"<<i<<": "<<a+b<<endl;
  }

  return 0;
}

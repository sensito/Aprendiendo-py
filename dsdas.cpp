#include<iostream>
#include<time.h>
#include <math.h>
using namespace std;
void swap(int *xp, int *yp){
int temp = *xp;
*xp = *yp;
*yp = temp;
}

void bubbleSort(int arr[], int n){
  int i, j;
  bool swapped;
  for (i = 0; i < n; i++){

    swapped = false;
    for (j = 0; j < n-i; j++){
      if (arr[j] > arr[j+1]){
        swap(&arr[j], &arr[j+1]);
        swapped = true;
      }
    }
    // IF no two elements were swapped by inner loop, then break
    if (swapped == false) break;
  }
}

void insert(int arr[]) {

  for(int c = 0; c < 5; c++){
    std::cout << "Valor a ingresar" << '\n';
    std::cin >> arr[c];
  }
}
void max(int arr[]) {
  int maximo = 0;
  for (size_t i = 0; i < 5; i++) {
    if (maximo < arr[i]) {
      maximo = arr[i];
    }
  }
  std::cout << "El valor maximo es: " <<maximo << '\n';
}
void min(int arr[]) {
  int minimo = 1000000;
  for (size_t i = 0; i < 5; i++) {
    if (minimo > arr[i]) {
      minimo = arr[i];
    }
  }
std::cout << "El valor minimo es: " <<minimo << '\n';
}

void prom(int arr[]) {
  float prome = 1.1;
  for (int i = 0; i < 5; i++) {
    prome += arr[i];
  }
  prome -= 1.1;
  prome = prome / 5;
  std::cout << "El promedio es: " <<prome << '\n';
}
void imprime(int arr[]) {
  for (int i = 0; i < 5; i++) {
    std::cout << arr[i] << '\n';
  }
}

int main(int argc, char const *argv[]) {
  int n;
  srand(time(NULL));
  int arr[5];
  insert(arr);
  max(arr);
  min(arr);
  prom(arr);
  clock_t tiempo_inicio, tiempo_final;
  double segundos;
  tiempo_inicio = clock();
  bubbleSort(arr, 4);
  tiempo_final = clock();
  segundos = (double)(tiempo_final - tiempo_inicio) / CLOCKS_PER_SEC; /*según que estes midiendo el tiempo en segundos es demasiado grande*/
  printf("Segundos: %f",segundos);
  imprime(arr);
  return 0;
}

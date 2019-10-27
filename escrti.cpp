#include<iostream>
#include<time.h>
#include <math.h>
using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
void bubbleSort(int arr[], int n)
{
   int i, j;
   bool swapped;
   for (i = 0; i < n-1; i++)
   {
     swapped = false;
     for (j = 0; j < n-i-1; j++)
     {
        if (arr[j] > arr[j+1])
        {
           swap(&arr[j], &arr[j+1]);
           swapped = true;
        }
     }

     // IF no two elements were swapped by inner loop, then break
     if (swapped == false)
        break;
   }
}

void insert(int arr[], int n) {
   int c;
   for(c = 1; c <= n; c++)
{
    arr[c] = 1 + rand() % (n - 1);
}
}

int main(int argc, char const *argv[]) {
    int n;
    srand(time(NULL));
    std::cout << "tamano de array para acomodar" << '\n';
    std::cin >> n;
    int arr[n];
    insert(arr, n);
    clock_t tiempo_inicio, tiempo_final;
    double segundos;
    tiempo_inicio = clock();
    bubbleSort(arr, n);
    tiempo_final = clock();
    segundos = (double)(tiempo_final - tiempo_inicio) / CLOCKS_PER_SEC; /*según que estes midiendo el tiempo en segundos es demasiado grande*/
    printf("Segundos: %f",segundos);
    return 0;
  return 0;
}

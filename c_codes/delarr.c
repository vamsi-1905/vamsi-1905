#include <stdio.h>

int deleteElement(int arr[], int size, int index) {
    if (index < 0 || index >= size) return size;
    for (int i = index; i < size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    return size - 1;
}

int main() {
    int arr[100], size, index;
    scanf("%d", &size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    scanf("%d", &index);
    size = deleteElement(arr, size, index);
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

}

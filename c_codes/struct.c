#include<stdio.h>
#include<string.h>
int main(void){
    struct bookdirectory{
  char title[100];
  char author[100];
  int price;
};
int k;
printf("How many books do u want to enter in the directory??");
scanf("%d",&k);

struct bookdirectory books[k];

for(int i=1;i<=k;i++){
printf("Enter book name\n");
scanf("%s",books[i].title);
printf("Enter author name\n");
scanf("%s",books[i].author);
printf("Enter book price\n");
scanf("%d",&books[i].price);
}
printf("Books in the Directory:\n");
    for (int i = 0; i < k; i++) {
        printf("Book %d: %s by %s, Price: %d\n", i + 1, books[i].title, books[i].author, books[i].price);
    }

}
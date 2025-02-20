
    import java.util.Scanner;
class Multiply{
    public static void main(String[] args){
        int i = 1;
        int multiply=0;
        Scanner sc= new Scanner(System.in);
        System.out.println("What is n?");
        int n = sc.nextInt();
         do{
            multiply=n*i;
            System.out.println("Table of " +n+ " "+ multiply);
            i++;
         }
         while(i<=10);
              sc.close();
            }

        }


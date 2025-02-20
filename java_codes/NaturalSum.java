import java.util.Scanner;
class NaturalSum{
    public static void main(String[] args){
        int sum=0;
        Scanner sc= new Scanner(System.in);
        System.out.println("What is n?");
        int n = sc.nextInt();
            sum+=(n*(n+1))/2;
              System.out.println("Sum of natural numbers uptil n = " + sum);
              sc.close();
            }

        }


        
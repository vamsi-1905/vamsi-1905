import java.util.Scanner;
class DigitSum{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter number:");
        int a = sc.nextInt();
        int s =0;
        for(;a>0;s=s+a%10,a=a/10);
        System.out.println("The sum is:"+s);
        sc.close();
    }
}



import java.util.Scanner;
class Temp{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the first number:");
        int a = sc.nextInt();
        System.out.println("Enter the second number:");
        int b = sc.nextInt();
        int tmp=1;
        tmp = a;
        a = b;
        b = tmp;
        System.out.println("a is equal to:"+ a);
        System.out.println("b is equal to:"+ b);
        sc.close();

}
}
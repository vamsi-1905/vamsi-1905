import java.util.Scanner;
class Calculator{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the first number:");
        int a = sc.nextInt();
        System.out.println("Enter the second number:");
        int b = sc.nextInt();
        System.out.println("Enter function to execute from 1 to 4:");
        int function = sc.nextInt();
        int add = a + b;
        int multiply = a * b;
        int divide = a/b;
        int subtract = a - b;
        sc.close();
        switch(function){
        case 1:
        System.out.println("Sum is equal to:"+ add);
        break;
        case 2:
        System.out.println("Product is equal to:"+ multiply);
        break;
        case 3:
        System.out.println("Division is equal to:"+ divide);
        break;
        case 4:
        System.out.println("Subtraction is equal to:"+ subtract);
        break;
        default: 
        System.out.println("Invalid function. Please choose a number between 1 and 4.");

    }
}
}
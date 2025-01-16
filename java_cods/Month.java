import java.util.Scanner;

class Month {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the year to be checked:");
        int year = sc.nextInt();
        int tmp = 0; // Initialize tmp outside for accessibility
        
        // Fixed parentheses in leap year condition
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            System.out.println("It is a leap year");
            tmp = 1; // Set tmp to 1 if it's a leap year
        } else {
            System.out.println("Not a leap year");
        }

        System.out.println("Enter the month to be checked:");
        int a = sc.nextInt();
        
        // Fixed condition for months with 31 days
        if (a == 1 || a == 3 || a == 5 || a == 7 || a == 8 || a == 10 || a == 12) {
            System.out.println("The month contains 31 days");
        }
        
        // Fixed condition to compare tmp using ==
        if (tmp == 1 && a == 2) {
            System.out.println("The month contains 29 days");
        } else if (a == 2) {
            System.out.println("The month contains 28 days");
        }
        
        // Fixed condition for months with 30 days
        if (a == 4 || a == 6 || a == 9 || a == 11) {
            System.out.println("The month contains 30 days");
        }
        
        sc.close(); // Close the scanner
    }
}

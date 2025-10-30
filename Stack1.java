
import java.util.Scanner;

class Stack {
    int s[];
    int top;
    int Max;

    Stack(int m) {
        Max = m;
        top = -1;
        s = new int[Max];
    }

    void push(int a) {
        if (top >= Max - 1) {
            System.out.println("Stack is full");
        } else {
            s[++top] = a;
            System.out.println(a + " pushed into stack");
        }
    }

    int pop() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return -1;
        } else {
            return s[top--];
        }
    }

    boolean isEmpty() {
        return top == -1;
    }

    int peek()
    {
        return s[top];
    }

   void display() {
    if (top == -1) {
        System.out.println("Stack is empty");
    } else {
        System.out.print("Stack: ");
        for (int i = top; i >= 0; i--) {
            System.out.print(s[i] + " ");
        }
        System.out.println();
    }
}


    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter length of stack");
        int m = sc.nextInt();

        Stack stack = new Stack(m);

        int choice;
        do {
            System.out.println("Choose an operation:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Check if stack is empty");
            System.out.println("4. peek ");
            System.out.println("5. display");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    if (stack.top < stack.Max - 1) {
                        System.out.print("Enter element to push: ");
                        int a = sc.nextInt();
                        stack.push(a);
                    } else {
                        System.out.println("Stack is full");
                    }
                    break;

                case 2:
                    int popped = stack.pop();
                    if (popped != -1) {
                        System.out.println("Popped element: " + popped);
                    }
                    break;

                case 3:
                    System.out.println("Stack is empty: " + stack.isEmpty());
                    break;

                case 4:

                    System.out.println("Top element:"+ stack.peek());
                    break;
                case 5:
                     stack.display();
                     break;

                     case 6:

                     System.out.println("Exiting...");
                     break;

                default:
                    System.out.println("Invalid choice. Try again.");
            }
        } while (choice != 6);

        sc.close();
    }
}



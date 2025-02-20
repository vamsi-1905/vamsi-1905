import java.util.Scanner;

public class Stack {
    static int top = -1;
    static int max;
    static char[] s;

    Stack(int size) {
        max = size;
        s = new char[max];
    }
    
    void push(char a) {
        if (top >= max - 1) {
            System.out.println("Stack is full.");
        } else {
            s[++top] = a;
        }
    }
    
    char pop() {
        if (top == -1) {
            return '0';
        } else {
            return s[top--];
        }
    }
    
    boolean isempty() {
        return top == -1;
    }

    static int prec(char ch) {
        switch (ch) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '^':
                return 3;
            default:
                return -1;
        }
    }

    public static String convertInfixToPostfix(String exp) {
        StringBuilder result = new StringBuilder();
        Stack stack = new Stack(100);
        
        for (int i = 0; i < exp.length(); ++i) {
            char c = exp.charAt(i);
            
            if (Character.isLetterOrDigit(c)) {
                result.append(c);
            }
            else if (c == '(') {
                stack.push(c);
            }
            else if (c == ')') {
                while (!stack.isempty() && stack.s[stack.top] != '(') {
                    result.append(stack.pop());
                }
                if (!stack.isempty()) {
                    stack.pop(); 
                }
            }
            else {
                while (!stack.isempty() && prec(c) <= prec(stack.s[stack.top])) {
                    result.append(stack.pop());
                }
                stack.push(c);
            }
        }
        
        while (!stack.isempty()) {
            if (stack.s[stack.top] == '(') {
                return "Invalid Expression";
            }
            result.append(stack.pop());
        }
        
        return result.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter an infix expression: ");
        String exp = sc.nextLine();
        System.out.println("Postfix expression: " + convertInfixToPostfix(exp));
        sc.close();
    }
}
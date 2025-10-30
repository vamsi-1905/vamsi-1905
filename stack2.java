import java.util.Scanner;

class stack2{
    int s[];
    int top;
    int max;

    stack2(int m)
    {
      max = m;
      top = -1;
      s=new int[max];
    }
    
    void push(int a)
    {
        if(top >= max-1)
        {
            System.out.println("Overflow condition");
        }
        else{
            top++;
            s[top]=a;

        }
    }
     
     int pop()
     {
        int val=0;
        if(top==-1)
        {
            System.out.println("stack is empty");
        }
        else{
            
               val = s[top];
            top--;
            
        }
        return val;
    }
    public int peek()
    {
        if(top==-1)
        {
          {
            System.out.println("stack is empty");
            return -1;
        }    
        }
        else{
           
        }
        return s[top];
    }
    public boolean is_empty()
    {
        if(top==-1)
        {
            return true;
        }
        else{
            return false;
        }
    
    }
    
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int m;
        System.out.println("Enter size of stack");
        m = sc.nextInt();
        stack2 s = new stack2(m);

        int choice;
        do {
            System.out.println("Choose an operation:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Check if stack is empty");
            System.out.println("4. peek ");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    if (s.top < s.max - 1) {
                        System.out.print("Enter element to push: ");
                        int a = sc.nextInt();
                        s.push(a);
                    } else {
                        System.out.println("Stack is full");
                    }
                    break;

                case 2:
                    int popped = s.pop();
                    if (popped != -1) {
                        System.out.println("Popped element: " + popped);
                    }
                    break;

                case 3:
                    System.out.println("Stack is empty: " + s.is_empty());
                    break;

                case 4:

                    System.out.println("Top element:"+ s.peek());
                    break;
                case 5:
               
                     System.out.println("Exiting...");
                     break;

                default:
                    System.out.println("Invalid choice. Try again.");
            }
        } while (choice != 5);

        sc.close();
    }
    }



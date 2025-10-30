import java.util.Scanner;

public class CircularQueue {
    static int front = -1, rear = -1, max;
    static int[] queue;

    CircularQueue(int size) {
        max = size;
        queue = new int[max];
    }
    
    static boolean isFull() {
        return (front == 0 && rear == max - 1) || (front == rear + 1);
    }
    
    static boolean isEmpty() {
        return front == -1;
    }
    
    static void enQueue(int data) {
        if (isFull()) {
            System.out.println("Queue is full");
            return;
        }
        
        if (front == -1) {
            front = 0;
            rear = 0;
        } else if (rear == max - 1 && front != 0) {
            rear = 0;
        } else {
            rear = rear + 1;
        }
        
        queue[rear] = data;
    }
    
    static int deQueue() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return -1;
        }
        
        int data = queue[front];
        
        if (front == rear) {
            front = -1;
            rear = -1;
        } else if (front == max - 1) {
            front = 0;
        } else {
            front = front + 1;
        }
        
        return data;
    }
    
    static void display() {
        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return;
        }
        
        System.out.println("Elements in Circular Queue are:");
        if (rear >= front) {
            for (int i = front; i <= rear; i++) {
                System.out.print(queue[i] + " ");
            }
        } else {
            for (int i = front; i < max; i++) {
                System.out.print(queue[i] + " ");
            }
            for (int i = 0; i <= rear; i++) {
                System.out.print(queue[i] + " ");
            }
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice, value;
        
        System.out.print("Enter queue size: ");
        int size = scanner.nextInt();
        
        CircularQueue queue = new CircularQueue(size);
        
        while (true) {
            System.out.println("\n--- Circular Queue Menu ---");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            System.out.print("Enter choice: ");
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("Enter value to enqueue: ");
                    value = scanner.nextInt();
                    enQueue(value);
                    break;
                case 2:
                    value = deQueue();
                    if (value != -1) {
                        System.out.println("Dequeued: " + value);
                    }
                    break;
                case 3:
                    display();
                    break;
                case 4:
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}
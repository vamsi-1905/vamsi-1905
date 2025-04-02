import java.util.Scanner;

public class DoubleEndedQueue {
    static int front = -1, rear = 0, max;
    static int[] deque;

    DoubleEndedQueue(int size) {
        max = size;
        deque = new int[max];
    }
    
    static boolean isFull() {
        return ((front == 0 && rear == max - 1) || front == rear + 1);
    }
    
    static boolean isEmpty() {
        return (front == -1);
    }
    
    static void insertFront(int key) {
        if (isFull()) {
            System.out.println("Overflow");
            return;
        }
        
        if (front == -1) {
            front = 0;
            rear = 0;
        } else if (front == 0) {
            front = max - 1;
        } else {
            front = front - 1;
        }
        
        deque[front] = key;
    }
    
    static void insertRear(int key) {
        if (isFull()) {
            System.out.println("Overflow");
            return;
        }
        
        if (front == -1) {
            front = 0;
            rear = 0;
        } else if (rear == max - 1) {
            rear = 0;
        } else {
            rear = rear + 1;
        }
        
        deque[rear] = key;
    }
    
    static void deleteFront() {
        if (isEmpty()) {
            System.out.println("Queue Underflow");
            return;
        }
        
        if (front == rear) {
            front = -1;
            rear = -1;
        } else if (front == max - 1) {
            front = 0;
        } else {
            front = front + 1;
        }
    }
    
    static void deleteRear() {
        if (isEmpty()) {
            System.out.println("Queue Underflow");
            return;
        }
        
        if (front == rear) {
            front = -1;
            rear = -1;
        } else if (rear == 0) {
            rear = max - 1;
        } else {
            rear = rear - 1;
        }
    }
    
    static int getFront() {
        if (isEmpty()) {
            System.out.println("Underflow");
            return -1;
        }
        return deque[front];
    }
    
    static int getRear() {
        if (isEmpty() || rear < 0) {
            System.out.println("Underflow");
            return -1;
        }
        return deque[rear];
    }
    
    static void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return;
        }
        
        System.out.println("Elements in Deque are:");
        if (rear >= front) {
            for (int i = front; i <= rear; i++) {
                System.out.print(deque[i] + " ");
            }
        } else {
            for (int i = front; i < max; i++) {
                System.out.print(deque[i] + " ");
            }
            for (int i = 0; i <= rear; i++) {
                System.out.print(deque[i] + " ");
            }
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice, value;
        
        System.out.print("Enter deque size: ");
        int size = scanner.nextInt();
        
        DoubleEndedQueue deque = new DoubleEndedQueue(size);
        
        while (true) {
            System.out.println("\n--- Deque Menu ---");
            System.out.println("1. Insert at Front");
            System.out.println("2. Insert at Rear");
            System.out.println("3. Delete from Front");
            System.out.println("4. Delete from Rear");
            System.out.println("5. Get Front");
            System.out.println("6. Get Rear");
            System.out.println("7. Display");
            System.out.println("8. Exit");
            System.out.print("Enter choice: ");
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("Enter value to insert at front: ");
                    value = scanner.nextInt();
                    insertFront(value);
                    break;
                case 2:
                    System.out.print("Enter value to insert at rear: ");
                    value = scanner.nextInt();
                    insertRear(value);
                    break;
                case 3:
                    deleteFront();
                    System.out.println("Deleted from front");
                    break;
                case 4:
                    deleteRear();
                    System.out.println("Deleted from rear");
                    break;
                case 5:
                    value = getFront();
                    if (value != -1) {
                        System.out.println("Front element: " + value);
                    }
                    break;
                case 6:
                    value = getRear();
                    if (value != -1) {
                        System.out.println("Rear element: " + value);
                    }
                    break;
                case 7:
                    display();
                    break;
                case 8:
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}

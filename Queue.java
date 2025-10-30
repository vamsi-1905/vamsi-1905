import java.util.Scanner;

class Queue{

int array_of_Queue[];
int front;
int rear;
int Max;

Queue(int m) {
        Max = m;
        front = -1;
        rear =-1;
         array_of_Queue = new int[Max];
    }

void enQueue_Data_Structure(int element) {  
  
    if (isFull()) {  
      System.out.println("Queue_Data_Structure is full");  
    }  
    else {  
      if (front == -1) {  
        front = 0;  
      }  
      rear++;  
      array_of_Queue[rear] = element;  
      System.out.println("Inserted " + element);  
    }  
  } 
  
  int deQueue_Data_Structure() {  
    
    int element;  
  
    if (isEmpty()) {  
      System.out.println("Queue_Data_Structure is empty");  
      return (-1);  
    }  
    else {  
      element = array_of_Queue[front];  
  
      if (front == rear) {  
        front = -1;  
        rear = -1;  
      }  
      else {  
        front++;  
      }  
      System.out.println( element + " Deleted");  
      return (element);  
    }  
  }

void Display(){
  if (isEmpty()) {  
      System.out.println("Queue_Data_Structure is empty");  
    }  
else{
  for(int i = front; i<=rear;i++)
  {
    System.out.println("Queue is:"+array_of_Queue[i]);
  }
}
}
boolean isEmpty() {

        if(rear==-1)
        {
        return true;
    }
    else{
      return false;
    }
}

boolean isFull(){
  if(rear==Max-1)
  {
    return true;
  }
  else{
    return false;
  }
}
   public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter length of queue");
        int m = sc.nextInt();

        Queue Queue = new Queue(m);

        int choice;
        do {
            System.out.println("Choose an operation:");
            System.out.println("1.Enqueue");
            System.out.println("2.Dequeue");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    if (Queue.front < Queue.Max - 1) {
                        System.out.print("Enter element to push: ");
                        int a = sc.nextInt();
                       Queue.enQueue_Data_Structure(a);
                    } else {
                        System.out.println("Queue is full");
                    }
                    break;

                case 2:
                    int Dequeued = Queue.deQueue_Data_Structure();
                    if (Queue.front!=-1&&Queue.rear!=-1) {
                        Queue.deQueue_Data_Structure();
                    }
                    break;
  
                case 3:
                   Queue.Display();
                    break;

                     case 4:

                     System.out.println("Exiting...");
                     break;

                default:
                    System.out.println("Invalid choice. Try again.");
            }
        } while ( choice !=4);

        sc.close();
    }
}



import java.util.Scanner;

class Node{
    Node next;
    int data;

        Node(int data)
        {
            this.data=data;
            this.next=null;
        }
    }


public class stackll {

    Node head;

    stackll()
    {
        this.head=null;
    }

    boolean is_empty()
    {
        if(head==null)
        {
            return true;
        }
        else{
            return false;
        }
    }

    void push(int a)
    {

         Node newNode = new Node(a);
        newNode.next=head;
        head= newNode;
        

    }

    int pop()
    {
        if(head==null)
        {
            System.out.println("Stack is empty");
            return -1;
        }
        else{
             Node temp = head;
            head = head.next;
            return temp.data;           
        }
    }

    int peek()
    {
        if(head==null)
        {
            System.out.println("Stack is empty");
            return -1;
        }
        else{
             return head.data;
        }
    }

     public static void main(String args[]) {
   

    stackll st = new stackll();

        
        st.push(11);
        st.push(22);
        st.push(33);
        st.push(44);

        
        System.out.println("Top element is " + st.peek());

        st.pop();
        st.pop();

      
        System.out.println("Top element is " + st.peek());
}
}


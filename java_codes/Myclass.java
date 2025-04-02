final class Mycl {  
    final int Max_speed = 120;  
    final static double PI = 3.14;

    void displayValues() {
        
        System.out.println("Max speed: " + Max_speed);
        System.out.println("Pi: " + PI);
    }
}

class Myclass extends Mycl{
System.out.println("1000");
}
    public static void main(String args[]) {
        Myclass MyCl = new Myclass();  
        MyCl.displayValues(); 
    }


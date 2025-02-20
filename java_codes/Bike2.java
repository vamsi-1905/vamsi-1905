class Vehicle
{
    void run()
    {
        System.out.println("Vehicle is running!!");
    }

    }
class Bike2 extends Vehicle{
     public static void main(String args[]){
        Bike2 obj = new Bike2();
        obj.run();
    }
    
    void run(){
        System.out.println("bomboclatt");
    }
   
}

//write program to calc your sgpa based on grades obtained for that subject. you need to enter credits of each subject
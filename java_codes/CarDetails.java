public class CarDetails{
    
        String Powertrain;
        int Torque;
        int Seats;
        CarDetails(){
            Powertrain = "Manual";
            Torque = 300;
            Seats=7;
        }

        CarDetails(String Powertrain)
        {
            this.Powertrain=Powertrain;
            this.Seats=10;
            this.Torque=2500;

        }
        CarDetails(String Powertrain,int Seats,int Torque)
        {
            this.Powertrain = Powertrain;
            this.Seats=Seats;
            this.Torque=Torque;

        }
         public static void main(String args[]){
         CarDetails s1 = new CarDetails();
         System.out.println(s1.Powertrain +" "+s1.Seats + " " + s1.Torque);
         CarDetails s2 = new CarDetails("Automatic");
         System.out.println(s2.Powertrain + " " + s2.Seats + " "+s2.Torque);
         CarDetails s3 = new CarDetails("Electric",4,400);
         System.out.println(s3.Powertrain + " " + s3.Seats + " " + s3.Torque);

    }
}
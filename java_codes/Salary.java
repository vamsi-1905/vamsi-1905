
 public class Salary{
    double monthlySalary;
    double bonus;
    double SalaryRecieved;
    Salary()
    {
        monthlySalary=50000;
        bonus=10000;
        SalaryRecieved=monthlySalary+bonus;
    }
    Salary(double monthlySalary)
    {
        this.monthlySalary=monthlySalary;
        this.bonus=10000;
        this.SalaryRecieved=monthlySalary+bonus;
    }
     Salary(double monthlySalary,double bonus)
    {
        this.monthlySalary=monthlySalary;
        this.bonus=bonus;
        this.SalaryRecieved=monthlySalary+bonus;
    }
    public static void main(String args[]){
         Salary s1 = new Salary();
         System.out.println(s1.monthlySalary +" "+s1.bonus + " " + s1.SalaryRecieved);
          Salary s2 = new Salary(70000);
         System.out.println(s2.monthlySalary +" "+s2.bonus + " " + s2.SalaryRecieved);
          Salary s3 = new Salary(70000,20000);
         System.out.println(s3.monthlySalary +" "+s3.bonus + " " + s3.SalaryRecieved);

 }
 }
class Faculty {
    String name;
    String department;
    Float salary;

    
    Faculty(String name, String department, Float salary) {
        this.name = name;
        this.department = department;
        this.salary = salary;
    }

    
    void display() {
        System.out.println("Name: " + name + ", Department: " + department + ", Salary: " + salary);
    }
}


class PermanentFaculty extends Faculty {
    float salaryPercentage;

  
    PermanentFaculty(String name, String department, Float salary, Float salaryPercentage) {
        super(name, department, salary);
        this.salaryPercentage = salaryPercentage;
    }


    void calculateSalary() {
        float totalSalary = salary + (salary * salaryPercentage / 100);
        System.out.println("Total Salary: " + totalSalary);
        display();
    }
}


class VisitingFaculty extends Faculty {
    float noOfClasses;
    float payPerClass;

    
    VisitingFaculty(String name, String department, float noOfClasses, float payPerClass) {
        super(name, department, 0f); 
        this.noOfClasses = noOfClasses;
        this.payPerClass = payPerClass;
    }

    
    void calculateSalary() {
        float totalSalary = noOfClasses * payPerClass;
        System.out.println("Total Salary: " + totalSalary);
        display();
    }
}


public class FacultyDemo {
    public static void main(String args[]) {
        PermanentFaculty pf = new PermanentFaculty("Dr. Smith", "CS", 50000f, 10f);
        VisitingFaculty vf = new VisitingFaculty("Dr. John", "AI", 20, 500);

        pf.calculateSalary();
        vf.calculateSalary();
    }
}

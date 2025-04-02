import java.util.Scanner;

class Mobile {
    String companyName, modelName;
    double price;
    int storage;

    void get_details() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Company Name: ");
        companyName = sc.nextLine();
        System.out.print("Enter Model Name: ");
        modelName = sc.nextLine();
        System.out.print("Enter Price: ");
        price = sc.nextDouble();
        System.out.print("Enter Storage (GB): ");
        storage = sc.nextInt();
    }

    void discount() {
        if (price > 10000) {
            price -= price * 0.05;
        }
    }

    void display_details() {
        System.out.println("Company: " + companyName);
        System.out.println("Model: " + modelName);
        System.out.println("Price after discount: " + price);
        System.out.println("Storage: " + storage + "GB");
    }

    public static void main(String[] args) {
        Mobile phone = new Mobile();
        phone.get_details();
        phone.discount();
        phone.display_details();
    }
}
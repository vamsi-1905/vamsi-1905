import java.util.Scanner;
class IPyramid{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        System.out.println("What is n?");
        int n = sc.nextInt();
        for(int i = n; i>0;i--)
        {
            for(int j = 0 ; j<i;j++)
            {
                System.out.print("#");
            }
            System.out.println(" ");
        }
        sc.close();
    }
}
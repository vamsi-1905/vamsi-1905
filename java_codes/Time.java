import java.util.Scanner;
public class Time {
    public static void main(String[] args){
Scanner sc = new Scanner(System.in);
System.out.println("Enter hours in 24 hour format");
int h = sc.nextInt();
System.out.println("Enter minutes in 24 hour format");
int m = sc.nextInt();
System.out.println("Enter seconds in 24 hour format");
int s = sc.nextInt();
if(s==59)
{
    s=0;
    m = m+1;
}
else{
    s = s+1;
}
if(m==60){
    h = h+1;
    m =0;
    }
    if(h==24)
    {
        h=0;
    }

    System.out.printf("Updated Time: %02d:%02d:%02d\n", h, m, s);
    sc.close();
}
}

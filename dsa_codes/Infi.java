import java.util.Scanner;
import java.util.Stack;

class Infi{
	static int precedence(char ch) {
	switch(ch) {
	case '+':
	case '-':
		return 1;
	case '/':
	case '*':
		return 2;
	case'^':
		return 3;
	default:
		return -1;
	}
}

static String convert(String Infix)
{
	Stack<Character> stack = new Stack<>();
	String postfix = "";

	for(int i =0;i<Infix.length();i++)
	{
		char c = Infix.charAt(i);
		
		if(Character.isLetterOrDigit(c))
		{
			postfix+=c;
		}
		else if(c == '(')
		{
			stack.push(c);
		}
		else if (c == ')')
		{
			while(!stack.isEmpty()&& precedence(c)<=precedence(stack.peek()))
			{
				postfix+=stack.pop();
			}
			stack.push(c);
			
		}
		while(!stack.isEmpty())
		{
			postfix+=stack.pop();
		}
		return postfix;
		
	}
	
} 

public class InfitoPostfi {

	Scanner sc = new Scanner(System.in);

	System.out.println("Enter Infix Expression");
	
	String Infix = sc.nextLine();
    System.out.println("Postfix expression: " + Infix.convert(Infix));
     

 }
}

abstract class Animal
{
    abstract void eat();
    public void out(){
   System.out.println("Meow Meow");
}
}
class Dog extends Animal
{
    public void makesound(){
        System.out.println("Bark Bark");
    }
}
class Main{
    public static void main(String args[]){
        Dog d1 = new Dog();
        d1.makeSound();
        d1.eat();

    }
}
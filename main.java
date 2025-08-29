

public class main{
    public static void main(String[] args) {
        Car lexus = new Car(4, 4);
        System.out.println(lexus.doors);
    }
}
class Car{
    int wheels;
    int doors;
    public Car(int wheels, int doors){
        this.wheels = wheels;
        this.doors = doors;
    }

}
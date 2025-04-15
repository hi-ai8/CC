import javax.jws.WebService;

@WebService
public interface CalculatorService {
    int add(int a, int b);

    int multiply(int a, int b);

    int largestOfTwo(int a, int b);

    int largestOfThree(int a, int b, int c);

    int square(int a);

    int cube(int a);

    int addThree(int a, int b, int c);
}
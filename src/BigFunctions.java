
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class BigFunctions {

    public static long factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }

    public static int[] sortArray(int[] array) {
        Arrays.sort(array);
        return array;
    }

    public static List<String> filterByLength(List<String> list, int minLength) {
        return list.stream()
                .filter(s -> s.length() >= minLength)
                .collect(Collectors.toList());
    }

    public static String concatenateStrings(String a, String b) {
        return a + b;
    }

    public static int findMax(int[] array) {
        return Arrays.stream(array).max().orElseThrow();
    }
}

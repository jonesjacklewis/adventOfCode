import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
// hashmap
import java.util.HashMap;

public class Day1 {
    public static void main(String[] args) {
        // Read input.txt in current directory
        String filename = "input.txt";
        String content = "";
        try {
            content = Files.readString(Paths.get(filename));
            int[][] numbers = convertStringToTwoArrays(content);

            int[] point1 = numbers[0];
            int[] point2 = numbers[1];

            if(point1.length != point2.length) {
                System.out.println("Invalid input");
                return;
            }

            // sort the points
            Arrays.sort(point1);
            Arrays.sort(point2);

            int partOneResult = partOne(point1, point2);

            System.out.printf("Total Difference: %d\n", partOneResult);

            int partTwoResult = partTwo(point1, point2);

            System.out.printf("Similarity Score: %d\n", partTwoResult);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int[][] convertStringToTwoArrays(String content) {
        String[] lines = content.split("\n");
        int[][] result = new int[2][lines.length];
        for (int i = 0; i < lines.length; i++) {
            String[] parts = lines[i].split("   ");
            result[0][i] = Integer.parseInt(parts[0]);
            result[1][i] = Integer.parseInt(parts[1]);
        }
        return result;
    }

    private static int partOne(int[] arr1, int[] arr2) {
        int[] differences = new int[arr1.length];

        for(int i = 0; i < arr1.length; i++) {
            int n1 = arr1[i];
            int n2 = arr2[i];

            int difference = Math.abs(n1 - n2);

            differences[i] = difference;
        }

        int total = 0;

        for(int i = 0; i < differences.length; i++) {
            total += differences[i];
        }

        return total;
    }

    private static int partTwo(int[] arr1, int[] arr2) {
        int similarityScore = 0;
        HashMap<Integer, Integer> scoreLookup = new HashMap<>();

        for(int num: arr1) {
            if(scoreLookup.containsKey(num)) {
                similarityScore += scoreLookup.get(num);
            } else {
                int increase_by = num * countOccurences(arr2, num);
                scoreLookup.put(num, increase_by);
                similarityScore += increase_by;
            }
        }

        return similarityScore;
    }

    private static int countOccurences(int[] arr, int value) {
        int count = 0;

        for(int num: arr) {
            if(num == value) {
                count++;
            }
        }

        return count;
    }
}
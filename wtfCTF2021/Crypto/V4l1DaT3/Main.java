import java.util.Scanner;

public class Main{

     public static void main(String []args){
        System.out.println("Hello World");
        validate flag = new validate();
        System.out.println("Enter flag : ");
        Scanner input = new Scanner("System.in");
        String inputFlag = "k33pC@pm@n4Tp1dCCC";//input.nextLine();
        
        if(flag.valid(inputFlag)==1)
        {
            System.out.println("Correct!");
        }
        else
        {
            System.out.println("Incorrect");
        }
     }
}

class validate{
    int valid(String str) {

        char[] input = str.toCharArray();
        int i, j, flag = 1;
        String str1 = "CmpFny4T@1d";
        if(input.length!=18) return 0;
        
        
        char letters[] = str1.toCharArray();
        System.out.println(letters);
        System.out.println(input);
        
        for (i = 4; i < 18; i++) { //Less than 18, greater than 4, 14 times
            for (j = 0; j < letters.length; j++) { //Less than 10, 10 times
                flag = 1;
                System.out.println("input = " + input[i]);
                System.out.println("letters = " + letters[j]);
                if (input[i] == letters[j]) {
                    flag = 0;
                    break;
                }
            }
            if (flag == 1) {
                break;
            }
        }
        
        System.out.println("Flag is = " + flag);
        
        if (flag == 1) {
            return 0;
        }
        
        if (input[0] != 'k') return 0;
        if (input[1] != '3') return 0;
        if (input[2] != '3') return 0;
        if (input[3] != 'p') return 0; //k33pCmpFny4T@1dCCC

        System.out.println("Here0");

        if (input[4] != input[15]) return 0; //k33p{C}mpFny4T@1dC{C}C
        if (input[5] != input[8]) return 0; //k33pC{m}pFn{y}4T@1dCCC
        if (input[6] != input[12]) return 0; //k33pCm{p}Fmy4T{@}1dCCC
        
        System.out.println("Here1");

        if ((input[7] - input[4]) != 42) return 0; //k33p{C}mp{F}my4Tp1dCCC
        if ((input[7] + 1) != input[9]) return 0; //k33pCmp{m}m{y}4Tp1dCCC
        if ((input[9] % input[8]) != 46) return 0; //k33pCmpm{m}{n}4Tp1dCCC
        if ((input[11] - input[8] + input[2]) != 'c') return 0;
        System.out.println("Here2");
        if ((input[14] - input[6]) != (input[17] + 2)) return 0;
        if ((input[9] % input[5]) * 2 != (input[13] + 40)) return 0;
        if ((input[4] % input[13]) != 15) return 0;
        if ((input[14] % input[13]) != (input[12] - 32)) return 0;
        if (((input[7] % input[6]) + 89) != input[10]) return 0;
        if ((input[16] % input[15]) != 17) {
            System.out.println((input[16] % input[15]));
            return 0;
        }
        int x = 0;
        int y = 132;
        for (i = 4; i < 18; i++) {
            x = x ^ input[i];
            y = y + input[i];
        }
        if (x != 72) return 0;
        if (y != 1250) return 0;

        return 1;
    }
}
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
public class One {
	public static void main (String args[]) throws IOException{
		ArrayList<Integer> linky = new ArrayList<Integer>();
		
		  File input = new File("Day1Inpput.txt"); Scanner scan = new Scanner(input);
		  while(scan.hasNext()) { linky.add(scan.nextInt()); } scan.close();
		/*
		 * linky.add(199); linky.add(200); linky.add(208); linky.add(210);
		 * linky.add(200); linky.add(207); linky.add(240); linky.add(269);
		 * linky.add(260); linky.add(263);
		 */
		int sum = 0;
		for (int i =0; i< linky.size(); i++) {
			if (i == linky.size()-1) {
				break;
			}
			else {
				if (linky.get(i) < linky.get(i+1)) {
					sum++;
				}
			}
		}
		System.out.println(sum);	
	}
	

}

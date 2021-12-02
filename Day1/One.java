import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
public class One {
	
	public ArrayList<Integer> convertToWin(ArrayList<Integer> list) {
		ArrayList<Integer> sumList = new ArrayList<Integer>();
		for(int i =0; i < list.size(); i++) {
			if ((i == list.size()-1) || (i==list.size()-2)){
				break;
			}
			else {
				sumList.add(list.get(i) + list.get(i+1) + list.get(i+2));
			}
		}
		return sumList;
	}
	
	public int taskOne(ArrayList<Integer> list) {
		int sum = 0;
		for (int i = 0; i < list.size(); i++) {
			if (i == list.size()-1) {
				break;
			}
			else {
				if (list.get(i) < list.get(i+1)) {
					sum++;
				}
			}
		}
		return sum;
	}
	public static void main (String args[]) throws IOException{
		ArrayList<Integer> linky = new ArrayList<Integer>();
		One dayOne = new One();
		
		
		  File input = new File("Day1Inpput.txt"); Scanner scan = new Scanner(input);
		  while(scan.hasNext()) { linky.add(scan.nextInt()); } scan.close();
		  System.out.println(dayOne.taskOne(linky));
		
		/*
		 * linky.add(199); linky.add(200); linky.add(208); linky.add(210);
		 * linky.add(200); linky.add(207); linky.add(240); linky.add(269);
		 * linky.add(260); linky.add(263);
		 */
		 
		ArrayList<Integer> linky2 = dayOne.convertToWin(linky);
		System.out.println(dayOne.taskOne(linky2));
	}
	

}

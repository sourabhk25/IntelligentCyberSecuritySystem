import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;


public class KDD 
{
	public static void main(String []args) throws IOException
	{
		String myfile = args[0];
		String myfile2 = args[1];
		System.out.println("hiii "+myfile+" "+myfile2);
		File inputFile = new File(myfile);
		BufferedReader br;
		BufferedWriter br2;
		br = new BufferedReader(new FileReader(inputFile));
		File outFile ;
		outFile = new File(myfile2);
		br2 = new BufferedWriter(new FileWriter(outFile));
		HashMap<String,Integer> TAB = new HashMap<String,Integer>();
		HashMap<String,Integer> TAB2 = new HashMap<String,Integer>();
		HashMap<String,Integer> TAB3 = new HashMap<String,Integer>();
		HashMap<String,Integer> TAB4 = new HashMap<String,Integer>();
		HashMap<String,Integer> TAB5 = new HashMap<String,Integer>();
		String s;

		int c=0,c2=0,c3=0,c4=0,c5=0;
		while((s = br.readLine())!=null)
		{
			
			br2.append("\n");
			String arr1[] = s.split(",");
			for(int i=0;i<arr1.length;i++)
			{
				
				
				if(i==3)
				{
					Integer x =TAB2.get(arr1[i]);
					if(x==null)
					{
						TAB2.put(arr1[i], c2);
						c2++;
					}
				//	br2.appendln(TAB);
					
						
					br2.append(","+TAB2.get(arr1[i]));
				}
				else if(i==4)
				{
					Integer x =TAB3.get(arr1[i]);
					if(x==null)
					{
						TAB3.put(arr1[i], c3);
						c3++;
					}
				//	br2.appendln(TAB);
					
						
					br2.append(","+TAB3.get(arr1[i]));
				}
				else if(i==6)
				{
					Integer x =TAB.get(arr1[i]);
					if(x==null)
					{
						TAB.put(arr1[i], c);
						c++;
					}
				//	br2.appendln(TAB);
					
						
					br2.append(","+TAB.get(arr1[i]));
				}
				else if(i==8)
				{
					Integer x =TAB5.get(arr1[i]);
					if(x==null)
					{
						TAB5.put(arr1[i], c5);
						c5++;
					}
				//	br2.appendln(TAB);
					
						
					br2.append(","+TAB5.get(arr1[i]));
				}
				else if(i==27)
				{
					Integer x =TAB4.get(arr1[i]);
					if(x==null)
					{
						TAB4.put(arr1[i], c4);
						c4++;
					}
				//	br2.appendln(TAB);
					
						
					br2.append(","+TAB4.get(arr1[i]));
				}
				else
				{
					if(i!=0)
					br2.append(","+arr1[i]);
					else
						br2.append(arr1[i]);
				}
			}
		}
		
		br.close();br2.close();
	}

}

package displayTest;

import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class displayTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ResultSet rs;
		try {	
    		Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/jtest","root","prashant");
    		Statement stmt=conn.createStatement(); 
    		System.out.println("Connected and executed ");
    		int yy=2017;
    		String str;
    		for(int mm=1;mm<=8;mm++)
    		{
    			for(int dd=1;dd<=23;dd++)
    			{
    				str="insert into tempTesaData(Date) values('"+Integer.toString(yy)+"-"+Integer.toString(mm)+"-"+Integer.toString(dd)+"') ";
    				System.out.println(str);
    				stmt.executeUpdate(str);
    			}
  	 		}
			
        }
        catch(Exception e)
        {
        	e.printStackTrace();
        }
        

	}

}

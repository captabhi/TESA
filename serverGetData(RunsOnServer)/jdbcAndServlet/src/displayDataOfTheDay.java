

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class displayDataOfTheDay
 */
@WebServlet("/displayDataOfTheDay")
public class displayDataOfTheDay extends HttpServlet {
	private static final long serialVersionUID = 1L;
	public ResultSet getResult(String date) throws Exception
	{
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/jtest","root","prashant");
		String str="select * from tempTesaData where Date='"+date+"'";
		Statement stm=conn.createStatement();
		ResultSet rs=stm.executeQuery(str);
		System.out.println("Query successful");
		
		return rs;
		
		
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getWriter().append("Served at: ").append(request.getContextPath());
		ResultSet myResult;
		PrintWriter out=response.getWriter();
		response.setContentType("text/html");
		String yyString=request.getParameter("yearID");
		request.getSession().removeAttribute(yyString);

		String mmString=request.getParameter("monthID");
		request.getSession().removeAttribute(mmString);

		String ddString=request.getParameter("dateID");
		request.getSession().removeAttribute(ddString);
		int dd,yy,mm;
		System.out.println(ddString);
		System.out.println(mmString);
		System.out.println(yyString);
		
		dd=Integer.parseInt(ddString);
		mm=Integer.parseInt(mmString);
		yy=Integer.parseInt(yyString);
		String Date=Integer.toString(yy+2001)+"-"+Integer.toString(mm+1)+"-"+Integer.toString(dd+1);
		out.write("<html><h1>Date: "+Date+"</h1><head><style>table, th, td {\n" + 
				"    border: 1px solid black;\n" + 
				"    border-collapse: collapse;\n" + 
				"}\n" + 
				"th, td {\n" + 
				"    padding: 5px;\n" + 
				"}\n" + 
				"th {\n" + 
				"    text-align: left;\n" + 
				"}\n" + 
				"</style></head>");
		
		try {
		myResult=getResult(Date);
		//System.out.println("This is query");

		out.write("<body><table style=\"width:100%\">");
		out.write("<tr><th>Time</th><th>Vac1</th><th>Vac2</th><th>Vac3</th>");
		out.write("<th>Vpv1</th><th>Vpv2</th>");
		out.write("<th>Iac1</th><th>Iac2</th><th>Iac3</th>");
		out.write("<th>Ipv1</th><th>Ipv2</th>");
		out.write("<th>Pnow</th><th>Etoday</th><th>Eall</th>");
		out.write("<th>Fault_code</th>");

		while(myResult.next())
		{
			/*
			System.out.println("This is query");
			System.out.print(myResult.getString("Time")+" ");
			System.out.print(myResult.getString("Vac1")+" "+myResult.getString("Vac2")+" "+myResult.getString("Vac3")+" ");
			System.out.print(myResult.getString("Vpv1")+" "+myResult.getString("Vpv2")+" ");
			System.out.print(myResult.getString("Iac1")+" "+myResult.getString("Iac2")+" "+myResult.getString("Iac3")+" ");
			System.out.print(myResult.getString("Ipv1")+" "+myResult.getString("Ipv2")+" ");
			System.out.print(myResult.getString("Pnow")+" "+myResult.getString("Etoday")+" "+myResult.getString("Eall")+" ");
			System.out.println(myResult.getString("Fault_code"));
			*/
			
			out.write("<tr><td>"+myResult.getString("Time")+"</td><td>"+myResult.getString("Vac1")+"</td><td>"+myResult.getString("Vac2")+"</td><td>"+myResult.getString("Vac3")+"</td>");
			out.write("<td>"+myResult.getString("Vpv1")+"</td><td>"+myResult.getString("Vpv2")+"</td>");
			out.write("<td>"+myResult.getString("Iac1")+"</td><td>"+myResult.getString("Iac2")+"</td><td>"+myResult.getString("Iac3")+"</td>");
			out.write("<td>"+myResult.getString("Ipv1")+"</td><td>"+myResult.getString("Ipv2")+"</td>");
			out.write("<td>"+myResult.getString("Pnow")+"</td><td>"+myResult.getString("Etoday")+"</td><td>"+myResult.getString("Eall")+"</td>");
			out.write("<td>"+myResult.getString("Fault_code")+"</td>");
		}
		out.write("</table></body></html>");
		
		}
		catch(Exception e)
		{
			
			e.printStackTrace();
		}
				
	}

}

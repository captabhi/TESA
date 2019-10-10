


import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.net.ssl.*;
import javax.net.*;
import java.util.UUID;
import java.io.*;
import java.net.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.*;



/**
 * Servlet implementation class dateQuery
 */
@WebServlet("/dateQuery")
public class dateQuery extends HttpServlet {
	
	public ResultSet getResult() throws Exception
	{
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/jtest","root","prashant");
		String str="select distinct Date from tempTesaData order by Date desc";
		Statement stm=conn.createStatement();
		ResultSet rs=stm.executeQuery(str);
		
		return rs;
		
		
	}
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		System.out.println(request.getContextPath());
		response.setContentType("text/html");
		PrintWriter out=response.getWriter();
		out.write("<html>");
		out.write("<h1>Years of Data Available</h1><body>Select Any Year<br><table style=\\\"width:80%\\\">");
		
		String[] temp;
		
		int yearMonthDate[][][]=new int[100][12][31];
		
		try {
			ResultSet rs=getResult();
			while(rs.next())
			{	
				temp=rs.getString("Date").split("-");
				yearMonthDate[Integer.parseInt(temp[0])%2000-1][Integer.parseInt(temp[1])-1][Integer.parseInt(temp[2])-1]=10;
				
			}
			
		}
		catch(Exception e)
		{
			e.printStackTrace();
			
			
		}
		
		//Way to create hyperlink
		//<p><a href="https://www.w3schools.com/html/">Visit our HTML tutorial</a></p>
		//<p><a href=\\\"http://localhost:8080/jdbcAndServlet/testForHyperlink\\\"
		int flag=0;
		int yearFlag=0;
		//String arrayID = UUID.randomUUID().toString();
		request.getSession().setAttribute("mydata", yearMonthDate);
		
		//response.sendRedirect("/jdbcAndServlet/testForHyperlink?arrayID=" + arrayID);
		int yy,mm,dd;
		for(yy=0;yy<100;yy++)
		{
			for(mm=0;mm<12;mm++)
			{
				for(dd=0;dd<31;dd++)
				{
					if(yearMonthDate[yy][mm][dd]==10)
					{
						flag=1;
						break;
					}
					
					
				}
				if(flag==1)
				{
					if(yearFlag==0)
					{
						out.write("<tr><th>"+Integer.toString(yy+2001)+"</th><td> Months: </td>");
						yearFlag=1;
					}
					
				
					out.write("<td><p><a href=\"monthPage?arrayID=mydata&yearID="+Integer.toString(yy)+"&monthID="+Integer.toString(mm)+"\">"+Integer.toString(mm+1)+"</a></p></td>");//""-"+Integer.toString(mm+1)+"-"+Integer.toString(dd+1));

					//out.write("<tr><td><p><a href=\"monthPage?arrayID=mydata\">"+Integer.toString(mm+1)+"</a></p></td></tr>");//""-"+Integer.toString(mm+1)+"-"+Integer.toString(dd+1));
					flag=0;
					
				}
				
				
			}
			out.write("</tr>");
			yearFlag=0;
		}
		out.write("</table></body></html>");
		
	}
}
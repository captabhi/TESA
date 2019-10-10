

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class monthPage
 */
@WebServlet("/monthPage")
public class monthPage extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getWriter().append("Served at: ").append(request.getContextPath());
		PrintWriter out=response.getWriter();
		
		String arrayID = request.getParameter("arrayID");
		
		int[][][] array = (int[][][]) request.getSession().getAttribute(arrayID);
		//request.getSession().removeAttribute(arrayID);
		
		String year= request.getParameter("yearID");
		
		//request.getSession().removeAttribute(year);

		String month= request.getParameter("monthID");
		
		//request.getSession().removeAttribute(month);
		int yy,mm;
		yy=Integer.parseInt(year);
		mm=Integer.parseInt(month);
		out.write("<html><h1>Select any date to display its data:</h1>");
		out.write("<body>Selected year:20"+Integer.toString(yy+1)+"<br>Selected month:"+Integer.toString(mm+1));
		out.write("<h2>Dates available:</h2><table style=\\\\\\\"width:80%\\\\\\\">\"<tr>");
		for(int dd=0;dd<31;dd++)
		{
			if(array[yy][mm][dd]==10)
			{
				String s="<td><p><a href=\"displayDataOfTheDay?yearID="+Integer.toString(yy)+"&monthID="+Integer.toString(mm)+"&dateID="+Integer.toString(dd)+"\">"+Integer.toString(dd+1)+"</a></p></td>";//""-"+Integer.toString(mm+1)+"-"+Integer.toString(dd+1));
				System.out.println(s);
				out.write(s);
				
			}
			
		}
		
		out.write("</tr></body></html>");
	}

}

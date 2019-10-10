

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class testForHyperlink
 */
@WebServlet("/testForHyperlink")
public class testForHyperlink extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType("text/html");
		PrintWriter out=response.getWriter();
		String arrayID = request.getParameter("arrayID");
		int[][][] array = (int[][][]) request.getSession().getAttribute(arrayID);
		request.getSession().removeAttribute(arrayID);
		
		out.write("<html>");
		out.write("<h1>Hello to my hyperlink</h1>");
		out.write("<body>"+Integer.toString(array[16][1][1])+"</body></html>");
	}

}

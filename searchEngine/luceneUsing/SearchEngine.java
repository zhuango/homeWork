package searchEngine;

import java.util.LinkedList;

public class SearchEngine {
	  public static void main(String[] args) throws Exception 
	  {
		  //-index /home/laboratory/weblech/index -docs /home/laboratory/weblech/sites/www.jmlr.org/
		  //String usage = "[-index INDEX_PATH] [-docs DOCS_PATH] [-update]";
		  //IndexFiles.Do(args);
		  
		  //-index /home/laboratory/weblech/index
//		  String usage =
//			      "Usage: [-index dir] [-field f] [-repeat n] [-queries file] [-query string] [-raw] [-paging hitsPerPage]";
		  String[] command = {	"-index", "/home/laboratory/weblech/index", 
				  				"-query", "小驴佳佳",
				  				"-paging", "9",
				  				"-pageNumber", "1"};
		  
		  QueryResult results = SearchFiles.DoOne(command);
		  
		  System.out.println("####################");
		  System.out.println(results.getUrls().get(0));
//		  for (int i = 0; i < urls.size(); i++)
//		  {
//			  System.out.println((i+1) + ". " + urls.get(i));
//		  }
	  }
}
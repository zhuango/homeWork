
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package searchEngine;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Date;
import java.util.LinkedList;
import java.util.List;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.cn.smart.SmartChineseAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.search.highlight.Highlighter;
import org.apache.lucene.search.highlight.InvalidTokenOffsetsException;
import org.apache.lucene.search.highlight.QueryScorer;
import org.apache.lucene.search.highlight.SimpleFragmenter;
import org.apache.lucene.search.highlight.SimpleHTMLFormatter;
import org.apache.lucene.store.FSDirectory;

public class SearchFiles {

  private SearchFiles() {}

  public static QueryResult DoOne(String[] args) throws Exception {
	    String index = "index";
	    String field = "contents";
	    String queries = null;
	    int repeat = 0;
	    boolean raw = false;
	    String queryString = null;
	    int hitsPerPage = 10;
	    int pageNumber = 1;
	    
	    for(int i = 0;i < args.length;i++) {
	      if ("-index".equals(args[i])) {
	        index = args[i+1];
	        i++;
	      } else if ("-field".equals(args[i])) {
	        field = args[i+1];
	        i++;
	      } else if ("-queries".equals(args[i])) {
	        queries = args[i+1];
	        i++;
	      } else if ("-query".equals(args[i])) {
	        queryString = args[i+1];
	        i++;
	      } else if ("-repeat".equals(args[i])) {
	        repeat = Integer.parseInt(args[i+1]);
	        i++;
	      } else if ("-raw".equals(args[i])) {
	        raw = true;
	      } else if ("-paging".equals(args[i])) {
	        hitsPerPage = Integer.parseInt(args[i+1]);
	        if (hitsPerPage <= 0) {
	          System.err.println("There must be at least 1 hit per page.");
	          System.exit(1);
	        }
	        i++;
	      } else if ("-pageNumber".equals(args[i])) {
	    	  pageNumber = Integer.parseInt(args[i+1]);
		        if (pageNumber <= 0) {
		          System.err.println("There must be at least 1 hit per page.");
		          System.exit(1);
		        }
		        i++;
	      }
	    }
	    QueryResult urls;
	    IndexReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(index)));
	    IndexSearcher searcher = new IndexSearcher(reader);
	    //Analyzer analyzer = new StandardAnalyzer();
	    Analyzer analyzer = new SmartChineseAnalyzer();
	    
	    BufferedReader in = null;
	    if (queries != null) {
	      in = Files.newBufferedReader(Paths.get(queries), StandardCharsets.UTF_8);
	    } else {
	      in = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
	    }
	    QueryParser parser = new QueryParser(field, analyzer);

	      if (queries == null && queryString == null) {
	        System.out.println("Enter query: ");
	      }

	      String line = queryString != null ? queryString : in.readLine();

	      if (line == null || line.length() == -1) {
	        return  new QueryResult();
	      }

	      line = line.trim();
	      if (line.length() == 0) {
	    	  return new QueryResult();
	      }
	      
	      Query query = parser.parse(line);
	      System.out.println("Searching for: " + query.toString(field));
	            
	      if (repeat > 0) {
	        Date start = new Date();
	        for (int i = 0; i < repeat; i++) {
	          searcher.search(query, 100);
	        }
	        Date end = new Date();
	        System.out.println("Time: "+(end.getTime()-start.getTime())+"ms");
	      }

	      urls = doPagingSearch(in, searcher, query, hitsPerPage, pageNumber, raw, queries == null && queryString == null);
//
//		    List<String> ursl = urls.getUrls();
//		    for(int i = 0; i < ursl.size(); i++)
//		    {
//		    	ursl.set(i, ursl.get(i).replace("clean", ""));
//		    }
	      if (queryString != null) {
	    	  return urls;
	      }
	    reader.close();
	    return urls;
	  }

  public static QueryResult doPagingSearch(BufferedReader in, IndexSearcher searcher, Query query, 
                                     int hitsPerPage, int pageNumber, boolean raw, boolean interactive) throws IOException, InvalidTokenOffsetsException {
 
	QueryResult queryResults = new QueryResult();
    TopDocs results = searcher.search(query, pageNumber * hitsPerPage);
    ScoreDoc[] hits = results.scoreDocs;
    
    int numTotalHits = results.totalHits;
    System.out.println(numTotalHits + " total matching documents");
    
    Highlighter highlighter = new Highlighter(new SimpleHTMLFormatter("<font color=\"red\">", "</font>"),new QueryScorer(query));
    highlighter.setTextFragmenter(new SimpleFragmenter(20));

    int start = 0;
    int end = Math.min(numTotalHits, pageNumber * hitsPerPage);
      for (int i = start; i < end; i++) {
        if (raw) {
          System.out.println("doc="+hits[i].doc+" score="+hits[i].score);
          continue;
        }

        Document doc = searcher.doc(hits[i].doc);
        Analyzer analyzer = new SmartChineseAnalyzer();
        String text = doc.get("contents");
        TokenStream tokenStream = analyzer.tokenStream("contents", new StringReader(text));
        String highlighterResult = highlighter.getBestFragments(tokenStream, text, 2, "");
        System.out.println("########### " + highlighterResult);
            
        String path = doc.get("path");
        if (path != null) {
          System.out.println((i+1) + ". " + path + " Score: " + hits[i].score);
          //System.out.println(results[i].)
          queryResults.addUrl(path);
          String title = doc.get("title");
          queryResults.addTitle(title);
          queryResults.addContent(highlighterResult);
        } else {
          System.out.println((i+1) + ". " + "No path for this document");
        }
      }
    return queryResults;
  }
  
}

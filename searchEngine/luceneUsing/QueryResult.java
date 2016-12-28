package searchEngine;

import java.util.ArrayList;
import java.util.List;

public class QueryResult {
	private List<String> urls = new ArrayList<>();
	private List<String> titles = new ArrayList<>();
	private List<String> contents = new ArrayList<>();
	
	public List<String> getUrls() {
		return urls;
	}
	public List<String> getTitiles()
	{
		return this.titles;
	}
	public List<String> getContents()
	{
		return this.contents;
	}
//	public void setUrls(List<String> urls) {
//		this.urls = urls;
//	}
//	public void setTitles(List<String> titles) {
//		this.titles = titles;
//	}
	
	public void addUrl(String url){
		this.urls.add(url);
	}
	public void addTitle(String title){
		this.titles.add(title);
	}
	public void addContent(String content)
	{
		this.contents.add(content);
	}
}
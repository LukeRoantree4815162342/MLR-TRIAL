#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import numpy as np
import cherrypy
from cherrypy.lib.static import serve_file
import DemoForGCD as scripttorun
import HTMLParser
path   = os.path.abspath(os.path.dirname(__file__))
config = {
  'global' : {
    'server.socket_host' : '127.0.0.1',
    'server.socket_port' : 8086,
    'server.thread_pool' : 8
  }
}

class App:

  @cherrypy.expose
  def index(self):
    return serve_file(os.path.join(path, 'htmltrialpage.html')) 


  @cherrypy.expose
  def GET(self, luke=None):
      return luke
  
  @cherrypy.expose
  @cherrypy.tools.json_out()
  def getData(self):
    #arr = ['test', 'luke1234', 'another random string1234', 'will this bee seen']
    testvar = scripttorun.maketestvar()
    return {
      'foo' : HTMLParser.HTMLParser().unescape(scripttorun.returnthis),
      'baz' : ['array1', 'array2'],
      'buckfast' : 'just a test to return this string',
      'piechart_value' :  HTMLParser.HTMLParser().unescape('''
          <script type="text/javascript">
	        google.charts.load('current', {'packages':['corechart']});
		      google.charts.setOnLoadCallback(drawChart);
		            function drawChart() {
			    
			            var data = google.visualization.arrayToDataTable([
				              ['Task', 'Hours per Day'],
					                ['Work',     ''' + str(testvar) + '''],
							          ['Eat',      2],
								            ['Commute',  2],
									              ['Watch TV', 2],
										                ['Sleep',    7]
												        ]);
													
													        var options = {
														          title: 'My Daily Activities'
															          };
																  
																          var chart = new google.visualization.PieChart(document.getElementById('piechart_value'));
																	  
																	          chart.draw(data, options);
																		        }</script>''')
      }



if __name__ == '__main__':
  cherrypy.quickstart(App(), '/', config)

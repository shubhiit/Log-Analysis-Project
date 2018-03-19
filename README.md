
<h2>About the Project:</h2>
<ul>
  <li>
    To build an internal reporting tool that will use information from the database to discover what kind of articles the sites readers like. Different queries were to be solved for the given database.
  </li>
  <li>
    Database consists of various tables such as articles, authors and log. The log has a database row for each time a reader loaded a web page.
  </li>
</ul>

<h2> Software and Languages: </h2>
<ul>
<li>
  <h5>
    Softwares required for this project are
  </h5>
    <ul>
    <li>Virtual Box</li>
    <li>Vagrant</li>
    <li>Git Bash</li>
    <ul>
</li>
<li>
  <h5>Languages required:</h5>
  <ul>
    <li>Python3</li>
    <li>PostgreSQL</li>
  </ul>
</li>
</ul>


<h2> Database Details:</h2>
  The database provided consisted of 3 tables named as:
  <ul>
    <li>authors</li>
    <li>articles</li>
    <li>log</li>
  </ul>

  <p>The meaning is same as the name suggests. The log table has a database row for each time a reader loaded a web page.</p>

  <p>Database file is named as newsdata.sql present in the project folder where as database is named as "<strong>news</strong>".</p>

  <h4>Detail about each table:</h4>
   <p>Run the below command to know the detail of each table:</p>
   ` \d table_name`

   <h4>Views created to achieve project goal:</h4>
   <ul>
    <li>
      <h5>article_views</h5>
      `create view article_views as select substring(path,10) as title, count(*) as views from log where path ~ '/article/' group by title order by views desc;`
    </li>
    <li>
      <h5>author_views</h5>
      `create view author_views as select articles.author, articles.title, views from articles, article_views where articles.slug = article_views.title;`
    </li>
    <li>
      <h5>author_viewers</h5>
      `create view author_viewers as select authors.name, views from authors, author_views where authors.id = author_views.author;`
    </li>
    <li>
      <h5>success_loads</h5>
        `create view success_loads as select date(time) as date, count(*) as loads from log where status = '200 OK' group by date;`
    </li>
    <li>
      <h5>unsuccess_loads</h5>
        `create view unsuccess_loads as select date(time) as date, count(*) as unloads from log where not (status = '200 OK') group by date;`
    </li>
    <li>
      <h5>load_view</h5>
        `create view load_view as select success_loads.date, loads, unloads from success_loads, unsuccess_loads where success_loads.date = unsuccess_loads.date;`
    </li>
    <li>
      <h5>percent_errors</h5>
        `create view percent_errors as select date , round ((unloads * 100.0) / loads, 2) as errors from load_view;`
    </li>
   </ul>

   <h2>How to run the project:</h2>
   <ol>
   <li>Install all the softwares mentioned above.</li>
   <li>Open the git bash on your computer and got to the directory in which the Project folder is in.</li>
   <li>Run `vagrant up` on the git bash and wait till you get your command line. To login in the Virtual box run `vagrant ssh`.</li>
   <li>To play with generic PostgreSQL run `psql`. To check everything has been perfectly installed run basic psql commands.</li>
   <li>To load the database file in the database system go to the directory in which file is present i.e. Project folder and run `psql -d news -f newsdata.sql` where news is the database name and newsdata.sql is the database file.</li>
   <li>To modify and know the database run `psql -d news`. You can know about the tables in the database in detail and also can create new views as per your requirements. </li>
   <li>Finally to print the required queries create a python file and write code as required.</li>
   <li>To run the file go the directory and run `python3 file_name.py`</li>
   </ol>

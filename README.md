# first-screening

<h3>Introduction</h3>
<p>This sample task is to demonstrate the skills of an applicant (me).</p>
<p>It is a basic RESTFul API that is developed using Flask micro web framework. It has basic CRUD Functionality.</p>

<h3>Major requirements</h3>
<ul>
  <li>This sample task requires Python 3.8+.</li>
  <li>The database used in this sample task is MySQL, you must create a database namely 'screening' without quote.</li>
</ul>


<br/>
<h3>Package requirements</h3>
<p>Here are the lists of modules that have been used in this sample task:</p>
<ul>
  <li><h4>poetry</h4> - to handle the modules/libraries/packages used in this sample task</li>
  <li><h4>flask</h4> - it is a micro web framework.</li>
  <li><h4>flask_sqlalchemy</h4> - it is an extension for Flask that adds support for SQLAlchemy ORM.</li>
  <li><h4>sqlalchemy</h4> - it is an ORM, to use its exception module.</li>
  <li><h4>sqlalchemy_utils</h4> - a helper tool to handle database, table creation</li>
  <li><h4>factory_boy</h4> - it is a fixture replacement tool that also provides data, etc. for testing.</li>
  <li><h4>PyJWT</h4> - to use json web token feature in auth.</li>
</ul>

<br/>
<h3>Helper tools/modules</h3>
<ul>
  <li><h4>black</h4> - It is a formatter that makes the code elegant.</li>
  <li><h4>mypy</h4> - It is a type checker that thecks the code statically and find potential bugs.</li>
  <li><h4>flake8</h4> - It is a helper tool that identifies the error and/or the violation codes </li>
  <li><h4>bandit</h4> - It is a tool that finds common security issues in Python.</li>
</ul>
<p>All of the package are installed via poetry.</p>
<br/>
<h3>Usage</h3>
<p>To run this program, make sure you already installed the package requirements stated above.</p>
<p>To run the code, type <strong><code>poetry run python run.py</code></strong> when you are in the <strong><code>first-screening</code></strong> directory. Once the program starts, it will automatically created the database tables</p>
<br/>
<p>When the database is created, you can generate the sample data by accessing the url <strong><code>/data/populate-data</code></strong> to generate the required data which are the four values and twelve principles of agile software development.</p>
<p>We can also remove all the data in our database by accesing the url <strong><code>http://localhost:5000/data/remove-data</code></strong>.</p> 
<p>Also, we need to create an admin user. To do that, we'll acess the url <strong><code>/api/generate_user</code></strong>.</p>

<br/>
<h3>End-points</h3>
<p>Below are the end-points of our RESTFul API:</p>
<p><strong><code>/api/topics/ - GET</code></strong>&nbsp;&nbsp;&nbsp;&nbsp;Fetch all the topics stored in the database.</p>
<p><strong><code>/api/topics/{name_id:str} - GET</code></strong>&nbsp;&nbsp;&nbsp;&nbsp;Fetch a specific topic via its required id.</p>
<p><strong><code>/api/topics/ - POST</code></strong>&nbsp;&nbsp;&nbsp;&nbsp;Creates a new topic, to submit -> { "name": str, "description": str }</p>
<p><strong><code>/api/topics/{name_id:str} - PUT</code></strong>&nbsp;&nbsp;&nbsp;&nbsp;Updates a specific topic, to submit -> { "name": str, "description": str }</p>
<p><strong><code>/api/topics/{name_id:str} - DELETE</code></strong>&nbsp;&nbsp;&nbsp;&nbsp;Deletes a specific topic.</p>
<br/>
<p><strong><code>/api/topics/{name_id:str}/{sequence_number:int} - GET</code></strong>&nbsp;&nbsp;&nbsp;&nbsp;Fetch a specific content under a certain topic.</p>
<p><strong><code>/api/topics/{name_id:str} - POST</code></strong>&nbsp;&nbsp;&nbsp;&nbsp;Creates a specific content under a certain topic.</p>
<p><strong><code>/api/topics/{name_id:str}/{sequence_number:int} - PUT</code></strong>&nbsp;&nbsp;&nbsp;&nbsp;Updates a specific content under a certain topic.</p>
<p><strong><code>/api/topics/{name_id:str}/{sequence_number:int} - DELETE</code></strong>&nbsp;&nbsp;&nbsp;&nbsp;Deletes a specific content under a certain topic.</p>
<br/>
<h3>Note</h3>
<p>Only a user that is registered at access POST, PUT, and DELETE request methods. To do that, you must access the <strong><code>/api/login</code></strong> route which it will return a response with a token value, but in this sample task, it is not that really important, it's just for the demo purpose only.</p>
<p>To do the requests, you must attach a header namely <strong><code>'x-access-token'</code></strong> with a value of <strong><code>'example_token'</code></strong> in order for us to grant permission to the said request methods</p>

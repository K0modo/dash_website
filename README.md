This is a multi-page website developed as a portal for customers and corporate managers. It is designed around the needs in the healthcare insurance industry but can be applied in other industries.  

The website is Python based using Plotly_Dash for interactivity on the front-end and SQLite3 on the back-end containing data.  The website data requirements have been partitioned for illustration purposes.  Member (customer) data is loaded via csv files and uses Python_Pandas for data manipulation and aggregation.   Corporate data on the other hand was loaded into a SQLite database.  An engine was used to connect to the database and a combination of SQL queries and Python_Pandas were used to create tables and perform calculations.  SQLite3 entails coding from SQL, Python, Python_Alchemy Object Relational Modeling (ORM).

The data visualization blends Dash_Plotly, Python_Pandas, AG Grid using callbacks to interact between filters/dropdowns and charts and tables.

The website layout uses Bootstrap Grid methodology (Row/Columns) and is styled predominantly with Dash_Bootstrap.  Overall, standard HTML elements and CSS classes were used to contain Bootstrap features.

The website home page shows 3 entry points:
- Members
- Corporate 
- Analytic - In development

Members Tab:
- Peronalized Dashboard visualization of healthcare activity
- Interactive Dropdowns By Healthcare Specialties
- Dynamic Grid for All Member Healthcare Insurance Claims

Corporate Tab:
- Corporate level Dashboard visualization of claims and charges
- Interactive Dropdowns by Healthcare Metric

Analytics Tab:
- Statistical Analysis of members, claims and charges


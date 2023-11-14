This is a multi-page website developed as a portal for customers and corporate managers. It is designed around the needs of the healthcare insurance industry but can be applied to other industries.  

The website is built with Flask and utilitized SQLAlchemy-ORM, Dash_Plotly, Pandas and PostgreSQL. Data for the Members is extracted from csv and manipulated with Pandas.  The Corporate portal on the otherhand uses a comprehensive SQLAlchemy approach by building data tables using SQL-Object Relational Mapping and querying the data for Dash_Plotly components and charts/graphs.

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


Hello!

This is _HoosBuying_ -- a platform made by, and built for college students who want to trade, barter, or give away their belongings as they go through college. 

I worked on this project with my roommate, Vlad, as a final project for our Databases class at the University of Virginia.

I am really proud of this project because it was immensely satisfying to build a full-stack application like this from the ground up. The project is made using Vue.js, Flask, and MySQL. We hosted our database on Google Cloud, and it was my first time working with a database that was not hosted locally. Setting up our database in Google Cloud was a great experience in growing accustomed to developing on cloud-based infrastructure, and definitely was a helpful lesson as I moved onto using AWS later. 

It was also both Vlad and my first time working with Vue.js, but we chose to use it because we wanted to challenge ourselves to diversify the tools we are comfortable with, and I knew it would be helpful to get more comfortable working with Javascript and Javascript-based frameworks.

***

Since I worked with a partner, I provided a breakdown of the features I was responsible for:
* Connecting the Flask API and our Google Cloud-hosted MySQL database to the Vue.js front-end
* Routing & NavBar 
* Platform Features
  * Set-up Search Page and supporting API Calls and SQL Scripts so Users could search Listings
  * Set-up Listing Page so Users could create their own and view others' listings and wrote the supporting API Calls and SQL Scripts
  * Set-up Tags so Users could look through classes of products at a time  


Vlad worked on:
* Ensured Images could be uploaded and viewed as a part of our lsitings
* Set-up Conversations between Users and saved the Messages between Users  


We both worked on a 1 feature together as well:
* Authentication
  * Devang
    * Set up Tables like User and Token
    * We made an in-house JWT authentication flow, and I wrote the SQL scripts and stored procedures that updated token tables as user's logged in and later had their tokens expire.
  * Vlad
    * Log-in and Sign-up flow
      * Encrypting and Decrypting passwords as they were compared to saved values from SQL

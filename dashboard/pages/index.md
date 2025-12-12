---
title: Sakila Dashboard
---

# Sakila Rental Dashboard

Welcome to the analytical dashboard for the **Sakila** database.  
Use the dropdown menu below to navigate between insights.

---

##  Navigation Menu

<style>
.dropdown {
  position: relative;
  display: inline-block;
  margin-top: 1rem;
}

.dropdown-button {
  background-color: #22262fff;
  color: white;
  padding: 10px 16px;
  font-size: 16px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: white;
  min-width: 220px;
  box-shadow: 0px 6px 12px rgba(255, 241, 241, 0.15);
  border-radius: 6px;
  z-index: 5;
}

.dropdown-content a {
  color: #22262cff;
  padding: 10px 14px;
  text-decoration: none;
  display: block;
  font-size: 15px;
}

.dropdown-content a:hover {
  background-color: #606574ff;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropdown-button {
  background-color: #070808ff;
}
</style>

<div class="dropdown">
  <button class="dropdown-button"> Open Dashboard Sections</button>
  <div class="dropdown-content">
    <a href="/film"> Film Analysis</a>
    <a href="/customer"> Customer Analysis</a>
    <a href="/rental"> Rental Analysis</a>
    <a href="/overview"> Database Overview</a>
  </div>
</div>

---


## Entity Relationship Diagram (ERD) on sakila database

![Sakila ERD](/sakila_erd.png)


The **ERD** diagram helps us understand the structure of the dataset, clarifying the relationships, joins, and selection paths used to extract information.
It also provides a solid foundation for further analysis, enabling us to efficiently retrieve any additional insights required.


import os
from flask import Flask, render_template
from selenium import webdriver

# Requirements Gathering
# Define the purpose and requirements for the website
purpose = "A simple website to display information about a software development process"
requirements = ["Home page","Model page"," Example page"]

# Design
# Create the layout for the website using HTML and CSS
layout = """
<!DOCTYPE html>
  <head>
    <meta charset ="UTF-8">
    <title>Model</title>
  </head>
  <body>
  <header>
    <img src="https://www.thensomehow.com/wp-content/uploads/2021/01/waterfall-model.png"
    <br>
    <p>
    "One of the many prescriptive software models, Waterfall model is the oldest, easily understandable and manageable model. It is sequential in nature which means it finishes one phase completely before another phase begins. The stages in waterfall models are communication, planning, modeling, construction and deployment. The process starts with communication or interaction during which the requirements of the customers are gathered and documented. This is followed by the planning stage wherein the cost and time constraints are estimated, a timetable is outlined and project tracking variable are established. This is achieved by keeping the requirements in mind. After it has been approved, it goes to the next phase which is modeling. Modeling is where the requirements and project constraints are kept in mind and created. The design consists of logical design and physical design. The logical design is the abstract presentation of how the data flows and the physical design determines the hardware such as storage which will make the logical design in the reality. Ater the design completes, the project team review it and approves the design. The code is generated and the building of the project into actual software starts in the construction phase. Software is then tested against the requirements. If the software does not meet the requirements, it is sent back to the previous phase for further implementation. Once all the verification actions are done and complete it is moved to the next and final phase. The deployment phase is the actual release of the software into the information technology environment. It involves delivering the product, receiving client feedback and provide support and maintenance for the product. 
    </p>
    </header>
  </body>
</html>
<!DOCTYPE html>
  <head>
    <meta charset ="UTF-8">
    <title>Waterfall Model</title>
    <link rel = "stylesheet" href="{{
        url_for('static',filename='css/main1.css')
    }}">
  </head>
  <body>
    <header>
        <img src="https://www.hivedesk.com/wp-content/uploads/2020/08/waterfall-1.jpg"
        <br>
      <h1>Welcome to the KnowledgeIsPower</h1>
      <p>What is a waterfall model?</p>
      
    </header>
    
</body>
</html>
<!DOCTYPE html>
  <head>
    <meta charset ="UTF-8">
    <title>Waterfall Model</title>
    <link rel = "stylesheet" href="{{
        url_for('static',filename='css/main2.css')
    }}">
  </head>
  <body>
    <section id="example">
      <h1>Examples of Waterfall Model</h1>
      <p1>In the olden days, Waterfall model was used to develop enterprise applications like,</p1>
      <br>
      <p2>Customer Relationship Management,
        Human Resource Management Systems,
        Supply Chain Management Systems and so on..
      </p2>
    </section>
  </main>
</body>
</html>
"""

# Implementation
# Create the Flask app and define the routes for the pages
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/model")
def waterfall():
   return render_template("contact.html")


@app.route("/example")
def example():
   return render_template("example.html")

@app.route("/login")
def login():
   return render_template("Not found")



# Testing
# Test the routes to make sure they display the correct pages
if __name__ == "__main__":
    app.run(debug=True)



# Create a list of web browsers to test(selenium testing)
browsers = ['chrome', 'firefox', 'safari']

# Loop through each web browser and URL combination
for browser in browsers:
    # Set up the web driver for the current browser
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
        
    # Close the browser window
    driver.quit()


# Deployment
# Deploy the website to a web server for public access
# You can use a cloud platform like Heroku to host website

# Maintenance
# Continuously monitor and update the website to ensure it remains functional
# This includes fixing bugs, adding new features, and updating dependencies

# User Experience Design

Welcome! In this assignment, you will work on designing the user experience of an imaginary web site consisting of no less than 5 pages. In particular, you will...

- draft wireframe diagrams that are the equivalent of a blueprint to be used when designers and engineers design and develop the site, respectively.
- draft a site map that shows the grouping and hierarchy of the various sections of the site
- create a clickable prototype of the site, so stakeholders who want to understand your plans can get a visceral sense of what it will feel like to use the site as you have designed it.

You will add a new page to your personal web site that shows the wireframe diagrams you have drafted and links to the clickable prototype you have created.

## Requirements

Some rules about the minimum work required to complete this assignment.

On top of these requirements, you are welcome to add any additional work that you believe will make your plans for this site compelling and stimulating to someone finding it on the web.

### Wireframes

Use [draw.io](https://draw.io) to draft **mobile wireframes** for the **mobile version** your imaginary site.

- create one wireframe for each distinct page of the site
- if there are interactive behaviors you are proposing for the site, such as content that appears dynamically on a page when the user hovers or clicks on something, be sure to create a version of the wireframess for those pages without the dynamic content displayed, and another version with the dynamic content displayed.
- the exact width of the wireframes is not important, but make sure every wireframe has the same width and looks suitable laid out for mobile devices.

Export each wireframe diagram as a `.png` file - you will post these to your personal web site later.

### Site map

Use draw.io to create a simple site map of your imaginary web site.

Export the site map diagram as a `.png` file - you will post it to your personal web site later.

### Clickable prototype

Use the Prototype feature of [InvisionApp](https://invision.com/) to create a clickable **mobile** prototype.

When creating a clickable prototype, meet the following minimal requirements:

- upload the `.png` images of your wireframes to an InvisionApp project
- set hotspots on each wireframe such that a viewer can click on the wireframes to see an approximation of how the real web site will function.
- everything that you are intending to be clickable on the final site should be clickable on the prototype.
- all buttons, links or other user interface components that allow a user to navigate from one screen to another must be functional in the prototype
- create as many variations of your existing wireframe diagrams as you need in order to make the prototype look "believable"; give a real sense of how the application flow might work... don't take shortcuts.
- your prototypes must be designed to clearly show the way in which a user navigates from one screen to another, as well as how they solve the core use cases and needs your web site is designed to solve.

Copy a link to your prototype. You will publish this link later to your personal web site.

### Update your personal web site

Create a new HTML document named `user_experience_design.html`. This page will display each of the wireframe diagrams, the site map, and a link to the clickable prototype of your imaginary site.

## Before updating, copy your current site

Before updating your personal site, copy all files from your existing personal web site, **except the `README.md` and `settings.json` files**, into this new project directory. This way, you will have a complete set of files for your web site in this new project directory and will not have to worry about accidentally deleting anything when you publish your updated web site later on.

#### Page heading

This page must have the general heading, `<h1>Use Exeperience Design</h1>`.

#### Prototype section

Create a `<section class='prototype'>` element with an `<h2>` heading that says, "`Clickable Prototype`".

- use an `<a>` element to take visitors to your clickable prototype on InvisionApp when the link is clicked.

#### Wireframe section

Create a `<section class='wireframes'>` element with an `<h2>` heading that says, "`Wireframes`".

- use `<img>` elements to publish each of your imaginary site's wireframe diagrams to this page. Style them so that they fit comfortably onto the page yet are eassy to view when viewed on a typical desktop web browser.

#### Site Map section

Create a `<sectionclass='site_map'>` element with an `<h2>` heading that says, "`Site Map`".

- use an `<img>` element to publish your imaginary site's site map diagram to this page. Style it so that it fits comfortably onto the page yet is eassy to view when viewed on a typical desktop web browser.

## Submit your work

In order to submit this assignment, you must publish all modified files to the web and upload the code to GitHub.

### Upload the web page to a web server

Upload all files you have created to a web server. Your instructor will have given you instructions for how to do this.

Take note of the web address (URL) of your web page - this is the address that can be plugged into the address bar of any web browser for the web browser to load and display your web page.

### Update the settings.json file

In the file named `settings.json`, update your name, Net ID, and URL of your personal site. Also add the URL of your clickable prototype into the appropriate field.

### Submit your work on GitHub

You are now ready to submit this assignment. You can do so directly from Visual Studio Code with the following steps, in the indicated order:

1. Switch to the Source Control view in Visual Studio Code - this view will show you a list of the files you have modified.
1. In the "`Message`" text field towards the top-left, enter a unique message to yourself about what you have changed and, while still with the text field selected, type `Command`-`Enter` on Mac OS X, or `Control`-`Enter` on Windows, to "commit" the changes you've made with this custom message. If you forget to hit `Command`-`Enter` after typing the message, you can instead click the "`...`" button above the message field and click the "`Commit all`" option in the menu that appears.
1. Now, click the "`...`" button above the message field and click the "`Push`" option in the menu that appears - this will upload your changes to your personal code repository on GitHub.

You have now submitted your completed assignment. Your changes are now posted to GitHub.com, where the instructor and graders can access it. Your `settings.json` file has information about who you are and where we can view your page on the web.

You can verify all this yourself manually by visiting your repository on GitHub.com and making sure the code displayed there is what you submitted.
